# GOAL

Your goal is to write a report about tokenization test results. You need to analyze the results and create a report with the following parts:
  - chart: model+language on the horizontal axis, number of tokens in text on the vertical axis, group bars by models, bar colors by language
  - chart: model+language on the horizontal axis, number of characters in a token on the vertical axis, group bars by models, bar colors by language
  - table: model/language/text tokens/token characters
  - unexpected insights
  - hidden patterns
  - summary: average number of tokens in text, average number of characters in a token
  - summary: most and least efficient languages and models

Charts should not be separate files.

## Tokenization Testing Results

| Model | Language | Tokens |
|-------|----------|--------|
| anthropic/claude-sonnet-4.5 | English | 275 |
| anthropic/claude-sonnet-4.5 | Finnish | 484 |
| anthropic/claude-sonnet-4.5 | Korean | 623 |
| anthropic/claude-sonnet-4.5 | Russian | 472 |
| anthropic/claude-sonnet-4.5 | Ukrainian | 475 |
| deepseek/deepseek-chat-v3-0324 | English | 250 |
| deepseek/deepseek-chat-v3-0324 | Finnish | 422 |
| deepseek/deepseek-chat-v3-0324 | Korean | 391 |
| deepseek/deepseek-chat-v3-0324 | Russian | 349 |
| deepseek/deepseek-chat-v3-0324 | Ukrainian | 471 |
| google/gemini-2.5-flash | English | 241 |
| google/gemini-2.5-flash | Finnish | 368 |
| google/gemini-2.5-flash | Korean | 384 |
| google/gemini-2.5-flash | Russian | 315 |
| google/gemini-2.5-flash | Ukrainian | 370 |
| meta-llama/llama-4-maverick | English | 251 |
| meta-llama/llama-4-maverick | Finnish | 361 |
| meta-llama/llama-4-maverick | Korean | 302 |
| meta-llama/llama-4-maverick | Russian | 294 |
| meta-llama/llama-4-maverick | Ukrainian | 356 |
| microsoft/phi-4-reasoning-plus | English | 253 |
| microsoft/phi-4-reasoning-plus | Finnish | 460 |
| microsoft/phi-4-reasoning-plus | Korean | 527 |
| microsoft/phi-4-reasoning-plus | Russian | 523 |
| microsoft/phi-4-reasoning-plus | Ukrainian | 634 |
| mistralai/mistral-medium-3.1 | English | 253 |
| mistralai/mistral-medium-3.1 | Finnish | 382 |
| mistralai/mistral-medium-3.1 | Korean | 353 |
| mistralai/mistral-medium-3.1 | Russian | 357 |
| mistralai/mistral-medium-3.1 | Ukrainian | 396 |
| nvidia/llama-3.3-nemotron-super-49b-v1.5 | English | 264 |
| nvidia/llama-3.3-nemotron-super-49b-v1.5 | Finnish | 468 |
| nvidia/llama-3.3-nemotron-super-49b-v1.5 | Korean | 394 |
| nvidia/llama-3.3-nemotron-super-49b-v1.5 | Russian | 392 |
| nvidia/llama-3.3-nemotron-super-49b-v1.5 | Ukrainian | 397 |
| openai/gpt-4o-mini | English | 254 |
| openai/gpt-4o-mini | Finnish | 358 |
| openai/gpt-4o-mini | Korean | 363 |
| openai/gpt-4o-mini | Russian | 326 |
| openai/gpt-4o-mini | Ukrainian | 399 |
| openai/gpt-oss-120b | English | 321 |
| openai/gpt-oss-120b | Finnish | 425 |
| openai/gpt-oss-120b | Korean | 430 |
| openai/gpt-oss-120b | Russian | 393 |
| openai/gpt-oss-120b | Ukrainian | 466 |
| qwen/qwen3-235b-a22b-2507 | English | 254 |
| qwen/qwen3-235b-a22b-2507 | Finnish | 459 |
| qwen/qwen3-235b-a22b-2507 | Korean | 409 |
| qwen/qwen3-235b-a22b-2507 | Russian | 402 |
| qwen/qwen3-235b-a22b-2507 | Ukrainian | 555 |
| x-ai/grok-code-fast-1 | English | 254 |
| x-ai/grok-code-fast-1 | Finnish | 358 |
| x-ai/grok-code-fast-1 | Korean | 363 |
| x-ai/grok-code-fast-1 | Russian | 326 |
| x-ai/grok-code-fast-1 | Ukrainian | 399 |
