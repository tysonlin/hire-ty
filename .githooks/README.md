# PII Detection Pre-Commit Hook

This directory contains a pre-commit hook that uses AI to detect Personally Identifiable Information (PII) before commits are made to the repository.

Supports multiple AI providers: **OpenAI**, **Anthropic** (Claude), or others via configuration.

## What it detects

The hook scans for any content that could identify you:
- Names, email addresses, phone numbers
- Physical addresses
- Personal qualifications and credentials
- Job application details
- CV/Resume content
- Cover letters and interview prep notes
- Employment information
- And more...

## Setup

The hook is already active! It takes effect immediately on your next commit.

**However:** If dependencies aren't set up, the hook will gracefully skip PII checks and allow your commit with a warning message. This means you can commit now if you want, but for real protection, set up your dependencies first.

### Quick Start (Recommended)

Copy the example env file and fill in your API keys:

```bash
cp .env.example .env
# Edit .env and add your actual API keys
nano .env  # or use your preferred editor
```

Then install dependencies:

```bash
pip install anthropic  # or: pip install openai
```

That's it! The hook will load your configuration from `.env` automatically.

### 1. Install Dependencies

Choose your AI provider:

**For OpenAI (GPT-4, GPT-4o, etc.):**
```bash
pip install openai
```

**For Anthropic (Claude):**
```bash
pip install anthropic
```

**For both providers:**
```bash
pip install openai anthropic
```

### 2. Set up your API keys

Add your API key(s) to your environment:

**OpenAI:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

**Anthropic:**
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Or add them to your `.zshrc`/`.bashrc`:
```bash
echo 'export OPENAI_API_KEY="your-openai-key"' >> ~/.zshrc
echo 'export ANTHROPIC_API_KEY="your-anthropic-key"' >> ~/.zshrc
### 2. Set up your API keys

You have two options:

**Option A: Using `.env` file (Recommended)**

```bash
cp .env.example .env
# Edit .env with your actual API keys
nano .env
```

The hook automatically loads from `.env` if it exists. The file is gitignored so your keys never commit.

**Option B: Environment variables**

If you prefer not to use a `.env` file, set environment variables directly:

```bash
export OPENAI_API_KEY="your-api-key-here"
export ANTHROPIC_API_KEY="your-api-key-here"
```

Or add to your `.zshrc`/`.bashrc`:
```bash
echo 'export OPENAI_API_KEY="your-openai-key"' >> ~/.zshrc
echo 'export ANTHROPIC_API_KEY="your-anthropic-key"' >> ~/.zshrc
source ~/.zshrc
```

Get API keys from:
- OpenAI: https://platform.openai.com/account/api-keys
- Anthropic: https://console.anthropic.com/account/keys

### 3. Choose your provider (optional)

The hook defaults to **Anthropic (Claude)**. To switch providers or models:

**In `.env` file (Recommended):**
```
AI_PROVIDER=openai
AI_MODEL=gpt-4o
```

**Or using environment variables:**
```bash
export AI_PROVIDER=openai
export AI_MODEL=gpt-4o
```

### 4. Verify Setup

Try making a commit:

```bash
git add .
git commit -m "test commit"
```

You should see the PII check running.

## Behavior

### With dependencies installed & configured:
- ✅ Scans all staged files for PII
- ❌ **Blocks commits** if PII is detected
- ✅ Allows commits if no PII found

### Without dependencies installed or API keys set:
- ⚠️ Shows warning message
- ✅ **Allows commits** (graceful fallback)
- 💡 Reminds you to set up dependencies for real protection

This way you can commit your work immediately, but once you configure the hook, it will actively protect you from accidentally committing sensitive information.

## How it works

1. When you run `git commit`, the hook intercepts the commit
2. It scans all staged files using your configured AI provider
3. If PII is detected, the commit is blocked with details
4. If safe, the commit proceeds normally

## Bypassing the check (NOT recommended)

If you absolutely need to bypass for some reason:

```bash
git commit --no-verify
```

⚠️ Use only if you're absolutely certain the content is safe.

## Testing the hook

To test without committing, you can run directly:

```bash
.githooks/pre-commit-pii-check.py
```

Or with a specific file:

```bash
git add path/to/file.md
.githooks/pre-commit-pii-check.py
```

To test with a different provider:
```bash
AI_PROVIDER=openai .githooks/pre-commit-pii-check.py
```

## Supported Providers & Models

### OpenAI
- `gpt-4o` - Most capable, recommended
- `gpt-4o-mini` - Faster, cheaper (default if using OpenAI)
- `gpt-4-turbo`
- Others available via OpenAI API

### Anthropic
- `claude-3-5-sonnet-20241022` - Recommended (default)
- `claude-3-opus-20250219`
- Others available via Anthropic API

## Hook Files

- `pre-commit` - Main hook script (bash)
- `pre-commit-pii-check.py` - PII detection logic (Python)
- `README.md` - This file
- `.env.example` - Example configuration file (in repo root, copy to `.env` and fill in your keys)

## Troubleshooting

**"openai/anthropic package not found"**
- Install: `pip install openai` or `pip install anthropic`

**"API key not found"**
- If using `.env`: Verify the file exists and keys are set (`cat .env`)
- If using env vars: Verify: `echo $OPENAI_API_KEY` or `echo $ANTHROPIC_API_KEY`
- If empty, set it in your `.env` file or shell profile

**`.env` file not being loaded**
- Verify file exists: `ls -la .env` (should be in repo root, not in `.githooks/`)
- Check format: `cat .env` (should be `KEY=VALUE` format, one per line)
- Environment variables take precedence over `.env` file

**Hook not running**
- Verify configuration: `git config core.hooksPath`
- Should show: `.githooks`

**Want to see which provider/model is being used:**
```bash
# From .env file
cat .env | grep AI_

# From environment
echo $AI_PROVIDER
echo $AI_MODEL
```
