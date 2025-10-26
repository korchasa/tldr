# GOAL

Your goal is to write a report about tokenization test results. You need to analyze the results and create two graphs, selecting the most and least efficient languages and models, along with all other useful information about the results. Do not include any other information(about tests itself, or any other information) in your response. Overall efficiency is the number of tokens per text. Tokenizer efficiency is the number of characters in a token. 

- chart: model+language on the horizontal axis, number of tokens in text on the vertical axis, group bars by models, bar colors by languages
- chart: model+language on the horizontal axis, number of characters in a token on the vertical axis, group bars by models, bar colors by languages
- table: model/language/text tokens/token characters
- unexpected insights
- hidden patterns
- summary: average number of tokens in text, average number of characters in a token
- summary: most and least efficient languages and models
## Tokenization Testing Results

| Model | Language | Text Length (chars) | Tokens | Token/Chars |
|-------|----------|-------------------|--------|-------------|
| anthropic/claude-sonnet-4.5 | English | 1106 | 275 | 0.2486 |
| anthropic/claude-sonnet-4.5 | Finnish | 1138 | 484 | 0.4253 |
| anthropic/claude-sonnet-4.5 | Korean | 628 | 623 | 0.9920 |
| anthropic/claude-sonnet-4.5 | Russian | 1196 | 472 | 0.3946 |
| anthropic/claude-sonnet-4.5 | Ukrainian | 1166 | 475 | 0.4074 |
| deepseek/deepseek-chat-v3-0324 | English | 1106 | 250 | 0.2260 |
| deepseek/deepseek-chat-v3-0324 | Finnish | 1138 | 422 | 0.3708 |
| deepseek/deepseek-chat-v3-0324 | Korean | 628 | 391 | 0.6226 |
| deepseek/deepseek-chat-v3-0324 | Russian | 1196 | 349 | 0.2918 |
| deepseek/deepseek-chat-v3-0324 | Ukrainian | 1166 | 471 | 0.4039 |
| google/gemini-2.5-flash | English | 1106 | 241 | 0.2179 |
| google/gemini-2.5-flash | Finnish | 1138 | 368 | 0.3234 |
| google/gemini-2.5-flash | Korean | 628 | 384 | 0.6115 |
| google/gemini-2.5-flash | Russian | 1196 | 315 | 0.2634 |
| google/gemini-2.5-flash | Ukrainian | 1166 | 370 | 0.3173 |
| meta-llama/llama-4-maverick | English | 1106 | 251 | 0.2269 |
| meta-llama/llama-4-maverick | Finnish | 1138 | 361 | 0.3172 |
| meta-llama/llama-4-maverick | Korean | 628 | 302 | 0.4809 |
| meta-llama/llama-4-maverick | Russian | 1196 | 294 | 0.2458 |
| meta-llama/llama-4-maverick | Ukrainian | 1166 | 356 | 0.3053 |
| microsoft/phi-4-reasoning-plus | English | 1106 | 253 | 0.2288 |
| microsoft/phi-4-reasoning-plus | Finnish | 1138 | 460 | 0.4042 |
| microsoft/phi-4-reasoning-plus | Korean | 628 | 527 | 0.8392 |
| microsoft/phi-4-reasoning-plus | Russian | 1196 | 523 | 0.4373 |
| microsoft/phi-4-reasoning-plus | Ukrainian | 1166 | 634 | 0.5437 |
| mistralai/mistral-medium-3.1 | English | 1106 | 253 | 0.2288 |
| mistralai/mistral-medium-3.1 | Finnish | 1138 | 382 | 0.3357 |
| mistralai/mistral-medium-3.1 | Korean | 628 | 353 | 0.5621 |
| mistralai/mistral-medium-3.1 | Russian | 1196 | 357 | 0.2985 |
| mistralai/mistral-medium-3.1 | Ukrainian | 1166 | 396 | 0.3396 |
| nvidia/llama-3.3-nemotron-super-49b-v1.5 | English | 1106 | 264 | 0.2387 |
| nvidia/llama-3.3-nemotron-super-49b-v1.5 | Finnish | 1138 | 468 | 0.4112 |
| nvidia/llama-3.3-nemotron-super-49b-v1.5 | Korean | 628 | 394 | 0.6274 |
| nvidia/llama-3.3-nemotron-super-49b-v1.5 | Russian | 1196 | 392 | 0.3278 |
| nvidia/llama-3.3-nemotron-super-49b-v1.5 | Ukrainian | 1166 | 397 | 0.3405 |
| openai/gpt-4o-mini | English | 1106 | 254 | 0.2297 |
| openai/gpt-4o-mini | Finnish | 1138 | 358 | 0.3146 |
| openai/gpt-4o-mini | Korean | 628 | 363 | 0.5780 |
| openai/gpt-4o-mini | Russian | 1196 | 326 | 0.2726 |
| openai/gpt-4o-mini | Ukrainian | 1166 | 399 | 0.3422 |
| openai/gpt-oss-120b | English | 1106 | 321 | 0.2902 |
| openai/gpt-oss-120b | Finnish | 1138 | 425 | 0.3735 |
| openai/gpt-oss-120b | Korean | 628 | 430 | 0.6847 |
| openai/gpt-oss-120b | Russian | 1196 | 393 | 0.3286 |
| openai/gpt-oss-120b | Ukrainian | 1166 | 466 | 0.3997 |
| qwen/qwen3-235b-a22b-2507 | English | 1106 | 254 | 0.2297 |
| qwen/qwen3-235b-a22b-2507 | Finnish | 1138 | 459 | 0.4033 |
| qwen/qwen3-235b-a22b-2507 | Korean | 628 | 409 | 0.6513 |
| qwen/qwen3-235b-a22b-2507 | Russian | 1196 | 402 | 0.3361 |
| qwen/qwen3-235b-a22b-2507 | Ukrainian | 1166 | 555 | 0.4760 |
| x-ai/grok-code-fast-1 | English | 1106 | 254 | 0.2297 |
| x-ai/grok-code-fast-1 | Finnish | 1138 | 358 | 0.3146 |
| x-ai/grok-code-fast-1 | Korean | 628 | 363 | 0.5780 |
| x-ai/grok-code-fast-1 | Russian | 1196 | 326 | 0.2726 |
| x-ai/grok-code-fast-1 | Ukrainian | 1166 | 399 | 0.3422 |

