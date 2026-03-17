#!/usr/bin/env python3
"""
Pre-commit hook to detect PII in staged files using configurable AI providers.
Prevents commits that contain personally identifiable information.

Supported providers: openai, anthropic
Set via environment variable: AI_PROVIDER=openai or AI_PROVIDER=anthropic
"""

import subprocess
import sys
import os
from pathlib import Path


def load_env_file():
    """Load environment variables from .env file in repo root."""
    repo_root = Path(__file__).parent.parent
    env_file = repo_root / ".env"
    
    if not env_file.exists():
        return
    
    try:
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                # Skip comments and empty lines
                if not line or line.startswith("#"):
                    continue
                # Parse KEY=VALUE
                if "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip()
                    # Only set if not already in environment (env vars take precedence)
                    if key not in os.environ and value:
                        os.environ[key] = value
    except Exception as e:
        # Silently fail if .env file can't be read
        pass


# Load .env file first (env variables take precedence)
load_env_file()
AI_PROVIDER = os.getenv("AI_PROVIDER", "anthropic").lower()
AI_MODEL = os.getenv("AI_MODEL", "")

# Track if we can actually run PII checks
PII_CHECK_AVAILABLE = True
SETUP_WARNING = ""

if AI_PROVIDER == "openai":
    try:
        from openai import OpenAI
    except ImportError:
        PII_CHECK_AVAILABLE = False
        SETUP_WARNING = "⚠️  OpenAI package not installed (pip install openai)"
elif AI_PROVIDER == "anthropic":
    try:
        import anthropic
    except ImportError:
        PII_CHECK_AVAILABLE = False
        SETUP_WARNING = "⚠️  Anthropic package not installed (pip install anthropic)"
else:
    PII_CHECK_AVAILABLE = False
    SETUP_WARNING = f"⚠️  Unknown AI provider '{AI_PROVIDER}'. Use 'openai' or 'anthropic'"


def get_staged_files():
    """Get list of staged files."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip().split("\n") if result.stdout.strip() else []
    except subprocess.CalledProcessError as e:
        print(f"Error getting staged files: {e}")
        sys.exit(1)


def get_file_content(filepath):
    """Get content of a staged file."""
    try:
        result = subprocess.run(
            ["git", "show", f":{filepath}"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError:
        # File might be deleted
        return ""


def check_pii_with_ai(file_content, filepath):
    """Use configured AI provider to detect PII in file content."""
    if not file_content.strip():
        return None

    # Return None if we can't check - will be handled gracefully
    if not PII_CHECK_AVAILABLE:
        return None

    prompt = f"""Analyze the following file content for Personally Identifiable Information (PII) that should not be committed to a public Git repository.

Look for ANY of the following:
- Full names or personal identifiers tied to a specific person
- Email addresses
- Phone numbers
- Physical addresses
- Social Security numbers or ID numbers
- Personal qualifications and credentials tied to a person
- Job application details and employer names
- CV/Resume content (education, experience)
- Cover letter content
- Interview preparation notes with personal context
- Dates of birth
- Company names (if identifying the person's employer)
- URLs with personal accounts

File: {filepath}

Content:
---
{file_content}
---

Respond with:
1. "PII_DETECTED" if any PII is found, followed by specific details
2. "SAFE" if no concerning PII found (generic tips and templates are ok)

Be strict - if content could identify the applicant, flag it."""

    try:
        if AI_PROVIDER == "openai":
            return _check_with_openai(prompt)
        else:  # anthropic
            return _check_with_anthropic(prompt)
    except Exception as e:
        # Gracefully handle API errors
        global SETUP_WARNING
        SETUP_WARNING = f"⚠️  API Error: {str(e)[:80]}"
        return None


def _check_with_openai(prompt):
    """Use OpenAI API to check for PII."""
    client = OpenAI()
    
    model = AI_MODEL or "gpt-4o-mini"
    
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
    )
    
    return response.choices[0].message.content


def _check_with_anthropic(prompt):
    """Use Anthropic API to check for PII."""
    client = anthropic.Anthropic()
    
    model = AI_MODEL or "claude-3-5-sonnet-20241022"
    
    message = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    
    return message.content[0].text


def main():
    """Main pre-commit check."""
    staged_files = get_staged_files()

    if not staged_files or not staged_files[0]:
        # No staged files
        sys.exit(0)

    # If PII check is not available, warn and allow commit
    if not PII_CHECK_AVAILABLE:
        print("⚠️  PII Detection is not available")
        print(f"   {SETUP_WARNING}")
        print("   Install dependencies and set up API keys to enable PII checks")
        print("   See .githooks/README.md for setup instructions")
        print("\n✅ Commit allowed (PII check skipped)")
        sys.exit(0)

    pii_detected_files = []

    print("🔍 Scanning staged files for PII...")

    for filepath in staged_files:
        if not filepath or filepath.startswith("."):
            continue

        # Skip binary files and common non-text files
        if any(
            filepath.endswith(ext)
            for ext in [".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".tar"]
        ):
            continue

        file_content = get_file_content(filepath)
        if not file_content.strip():
            continue

        print(f"  Checking: {filepath}")

        result = check_pii_with_ai(file_content, filepath)

        # If result is None due to an error, skip this file
        if result is None:
            continue

        if "PII_DETECTED" in result:
            pii_detected_files.append((filepath, result))
            print(f"  ⚠️  PII detected in {filepath}")

    if pii_detected_files:
        print("\n❌ Pre-commit check FAILED - PII detected:\n")
        for filepath, result in pii_detected_files:
            print(f"File: {filepath}")
            print(result)
            print("-" * 80)

        print("\n💡 Tips:")
        print("  - Remove personal information before committing")
        print("  - Use .gitignore to exclude sensitive directories")
        print("  - Consider using placeholders or generic examples")
        print("\nTo bypass (NOT recommended): git commit --no-verify")
        sys.exit(1)

    print("✅ No PII detected. Safe to commit!")
    sys.exit(0)


if __name__ == "__main__":
    main()
