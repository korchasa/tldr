# Tokenization Testing via OpenRouter.ai API

This script allows you to test various language models through the OpenRouter.ai API and get statistics on token counts for texts in different languages.

## Installation

1. Install Docker on your system
2. Get API key from OpenRouter.ai at https://openrouter.ai/
3. Set environment variable:
```bash
export OPENROUTER_API_KEY='your-api-key-here'
```

## Usage

Run the automated script:
```bash
./run.sh
```

Results will be saved to `./results/token_results.md` on your host system.

## What the script does

1. **Tests 10 different language models:**
   - GPT-4o and GPT-4o-mini (OpenAI)
   - Claude 3.5 Sonnet and Claude 3 Haiku (Anthropic)
   - Gemini Pro 1.5 (Google)
   - Llama 3.1 8B and 70B (Meta)
   - Phi-3 Medium (Microsoft)
   - Mistral 7B (Mistral AI)
   - Command R+ (Cohere)

2. **Uses texts in 5 languages:**
   - English
   - Russian (Русский)
   - Ukrainian (Українська)
   - Finnish (Suomi)
   - Korean (한국어)

3. **Outputs statistics:**
   - Number of input tokens for each model and language
   - API response time
   - General statistics for all tests

4. **Saves results:**
   - To console in convenient table format
   - To Markdown file `token_results.md` with detailed tables and analysis

## Example output

```
TOKENIZATION TESTING RESULTS
================================================================================

ENGLISH:
----------------------------------------
Model                                  Input    Output   Total    Time
----------------------------------------
openai/gpt-4o                          156      45       201      2.34s
anthropic/claude-3.5-sonnet            142      38       180      1.87s
...

RUSSIAN:
----------------------------------------
Model                                  Input    Output   Total    Time
----------------------------------------
openai/gpt-4o                          198      52       250      2.45s
anthropic/claude-3.5-sonnet            185      41       226      2.12s
...
```

## Features

- **Docker-based execution**: No need to install Python or dependencies on your host
- **Isolated environment**: Runs in a clean container environment
- **Automatic API error handling**: Graceful handling of API failures
- **Rate limiting protection**: Pause between requests to avoid API limits
- **Detailed statistics**: Comprehensive statistics for each language
- **Results persistence**: Results saved to host filesystem via volume mount
- **Multiple model support**: Tests various models with different tokenization algorithms

## File Structure

```
llm/tokens-size/
├── token_test.py          # Main testing script
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker image definition
├── run.sh               # Automated runner script (executable)
├── README.md            # This file
└── results/             # Output directory (created automatically)
    └── token_results.md
```

## Configuration

You can easily change:
- List of models in `self.models` variable
- Test texts in `self.test_texts` dictionary
- Request parameters (temperature, max_tokens)
- Pause between requests
