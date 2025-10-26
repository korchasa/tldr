#!/usr/bin/env python3
"""
Script for testing tokenization of various language models via OpenRouter.ai API
"""

import requests
import time
from typing import Dict, List, Tuple
import os
from dataclasses import dataclass

@dataclass
class ModelResult:
    model: str
    language: str
    input_tokens: int

class OpenRouterTester:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://openrouter.ai/api/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        # List of models for testing
        self.models = [
            "anthropic/claude-sonnet-4.5",
            "deepseek/deepseek-chat-v3-0324",
            "google/gemini-2.5-flash",
            "meta-llama/llama-4-maverick",
            "microsoft/phi-4-reasoning-plus",
            "mistralai/mistral-medium-3.1",
            "nvidia/llama-3.3-nemotron-super-49b-v1.5",
            "openai/gpt-4o-mini",
            "openai/gpt-oss-120b",
            "qwen/qwen3-235b-a22b-2507",
            "x-ai/grok-code-fast-1",
        ]

        # Texts in different languages
        self.test_texts = {
            "English": "As machine learning algorithms process numbers rather than text, the text must be converted to numbers. In the first step, a vocabulary is decided upon, then integer indices are arbitrarily but uniquely assigned to each vocabulary entry, and finally, an embedding is associated to the integer index. Algorithms include byte-pair encoding (BPE) and WordPiece. There are also special tokens serving as control characters, such as [MASK] for masked-out token (as used in BERT), and [UNK] (\"unknown\") for characters not appearing in the vocabulary. Also, some special symbols are used to denote special text formatting. For example, \"Ġ\" denotes a preceding whitespace in RoBERTa and GPT and \"##\" denotes continuation of a preceding word in BERT. Tokenization also compresses the datasets. Because LLMs generally require input to be an array that is not jagged, the shorter texts must be \"padded\" until they match the length of the longest one. The average number of words per token depends on the language. In English, the ratio is typically around 0.75 words per token, with 4 characters per token on average.",

            "Russian": "Поскольку алгоритмы машинного обучения обрабатывают числа, а не текст, текст должен быть преобразован в числа. На первом этапе выбирается словарь, затем каждому элементу словаря произвольно, но уникально присваивается целочисленный индекс, и, наконец, к целочисленному индексу привязывается векторное представление (эмбеддинг). Алгоритмы включают кодирование пар байтов (BPE) и WordPiece. Также существуют специальные токены, служащие управляющими символами, такие как [MASK] для замаскированного токена (как используется в BERT) и [UNK] («неизвестный») для символов, не входящих в словарь. Кроме того, некоторые специальные символы используются для обозначения особого форматирования текста. Например, \"Ġ\" обозначает предшествующий пробел в RoBERTa и GPT, а \"##\" обозначает продолжение предыдущего слова в BERT. Токенизация также сжимает наборы данных. Поскольку большие языковые модели (LLM) обычно требуют, чтобы входные данные были массивом без «зазубрин», более короткие тексты должны быть «дополнены» до длины самого длинного. Среднее количество слов на токен зависит от языка. В английском языке это соотношение обычно около 0,75 слова на токен, при среднем количестве 4 символов на токен.",

            "Ukrainian": "Оскільки алгоритми машинного навчання обробляють числа, а не текст, текст повинен бути перетворений у числа. На першому етапі вибирається словник, потім кожному елементу словника випадково, але унікально присвоюється цілий індекс, і, нарешті, до цілочисельного індексу прив'язується векторне представлення (ембеддинг). Алгоритми включають кодування пар байтів (BPE) та WordPiece. Також існують спеціальні токени, які служать керуючими символами, такі як [MASK] для замаскованого токена (як використовується в BERT) та [UNK] («невідомий») для символів, що не входять до словника. Крім того, деякі спеціальні символи використовуються для позначення особливого форматування тексту. Наприклад, \"Ġ\" позначає попередній пробіл у RoBERTa та GPT, а \"##\" позначає продовження попереднього слова в BERT. Токенізація також стискає набори даних. Оскільки великі мовні моделі (LLM) зазвичай вимагають, щоб вхідні дані були масивом без «зазубрин», коротші тексти повинні бути «доповнені» до довжини найдовшого. Середня кількість слів на токен залежить від мови. В англійській мові це співвідношення зазвичай близько 0,75 слова на токен, при середній кількості 4 символів на токен.",

            "Finnish": "Koska koneoppimisalgoritmit käsittelevät numeroita tekstin sijaan, teksti täytyy muuntaa numeroiksi. Ensimmäisessä vaiheessa päätetään sanasto, sitten jokaiselle sanaston merkinnälle annetaan mielivaltaisesti mutta yksilöllisesti kokonaislukuihin perustuvat indeksit, ja lopuksi indeksiin liitetään upotus (embedding). Algoritmeihin kuuluvat muun muassa byte-pair encoding (BPE) ja WordPiece. On myös erikoistokenoita, jotka toimivat ohjausmerkkeinä, kuten [MASK] piilotetulle tokenille (käytössä mm. BERTissä) ja [UNK] (\"tuntematon\") merkeille, joita ei esiinny sanastossa. Lisäksi käytetään erityisiä symboleita spesiaalin tekstin muotoilun ilmaisemiseen. Esimerkiksi \"Ġ\" merkitsee edeltävää välilyöntiä RoBERTassa ja GPT:ssä, ja \"##\" tarkoittaa sanan jatkumista BERTissä. Tokenisointi myös pakkaa tietoaineistot. Koska suurten kielimallien (LLM) syötteiden täytyy yleensä olla ei-epäsäännöllinen taulukko, lyhyemmät tekstit täytyy \"täyttää\" pisimmän tekstin mittaisiksi. Sanojen keskimääräinen määrä per token riippuu kielestä. Englannissa tämä suhdeluku on tyypillisesti noin 0,75 sanaa per token ja keskimäärin 4 kirjainta per token.",

            "Korean": "머신러닝 알고리즘은 텍스트가 아니라 숫자를 처리하므로, 텍스트는 숫자로 변환되어야 합니다. 첫 번째 단계에서는 어휘집을 결정하고, 각 어휘 항목에 임의적이지만 고유한 정수 인덱스를 할당한 다음, 해당 정수 인덱스에 임베딩(embedding)이 연결됩니다. 알고리즘에는 바이트-쌍 인코딩(Byte Pair Encoding, BPE)과 WordPiece 등이 포함됩니다. 또한 [MASK](BERT에서 사용된 마스킹 토큰)나 [UNK](어휘집에 없는 문자를 나타내는 \"unknown\" 토큰) 같은 제어 문자 역할을 하는 특수 토큰들도 존재합니다. 그 외에도, 특수 문자들이 특별한 텍스트 서식을 나타내는 데 사용됩니다. 예를 들어, RoBERTa와 GPT에서 \"Ġ\"는 앞에 오는 공백을, BERT에서는 \"##\"가 이전 단어의 연속임을 나타냅니다. 토크나이즈(Tokenization) 과정은 데이터셋을 압축하기도 합니다. 대형 언어 모델(LLM)에서는 입력이 '비정방 배열(jagged array)'이 아니어야 하므로 짧은 텍스트는 가장 긴 텍스트의 길이에 맞추어 '패딩'되어야 합니다. 토큰당 평균 단어 수는 언어에 따라 다릅니다. 영어의 경우, 일반적으로 토큰당 약 0.75 단어, 토큰당 평균 4개의 문자 비율을 보입니다."
        }

    def make_request(self, model: str, text: str, language: str) -> ModelResult:
        """Makes API request and returns result"""
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": f"Count the number of tokens in the following {language} text: {text}"
                }
            ],
            "max_tokens": 1,
            "temperature": 0.1
        }

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()

            data = response.json()

            # Extract token information
            usage = data.get('usage', {})
            input_tokens = usage.get('prompt_tokens', 0)
            output_tokens = usage.get('completion_tokens', 0)
            total_tokens = usage.get('total_tokens', 0)

            return ModelResult(
                model=model,
                language=language,
                input_tokens=input_tokens,
            )

        except requests.exceptions.RequestException as e:
            print(f"Error requesting {model} for {language}: {e}", flush=True)
            return ModelResult(
                model=model,
                language=language,
                input_tokens=0,
            )

    def test_all_combinations(self) -> List[ModelResult]:
        """Tests all combinations of models and languages"""
        results = []
        total_combinations = len(self.models) * len(self.test_texts)
        current = 0

        print(f"Starting testing of {total_combinations} combinations...", flush=True)
        print("=" * 60, flush=True)

        for model in self.models:
            for language, text in self.test_texts.items():
                current += 1
                print(f"[{current}/{total_combinations}] Testing {model} on {language}...", flush=True)

                result = self.make_request(model, text, language)
                results.append(result)

                # Show result immediately
                if result.input_tokens > 0:
                    print(f"  ✓ Completed: {result.input_tokens} input tokens", flush=True)
                else:
                    print(f"  ✗ Failed", flush=True)

                # Small pause between requests
                time.sleep(1)

        # Show final summary
        successful = len([r for r in results if r.input_tokens > 0])
        failed = len(results) - successful
        print(f"\nTesting completed: {successful} successful, {failed} failed out of {total_combinations} tests", flush=True)

        return results

    def print_results(self, results: List[ModelResult]):
        """Prints results in a convenient format"""
        print("\n" + "=" * 80)
        print("TOKENIZATION TESTING RESULTS")
        print("=" * 80)

        # Group results by language
        by_language = {}
        for result in results:
            if result.language not in by_language:
                by_language[result.language] = []
            by_language[result.language].append(result)

        # Calculate language statistics
        language_stats = {}
        for language, lang_results in by_language.items():
            successful_results = [r for r in lang_results if r.input_tokens > 0]
            if successful_results:
                # Get the original text for this language
                original_text = self.test_texts.get(language, "")
                text_length = len(original_text)

                # Calculate average tokens and characters per token
                avg_tokens = sum(r.input_tokens for r in successful_results) / len(successful_results)
                avg_chars_per_token = text_length / avg_tokens if avg_tokens > 0 else 0

                language_stats[language] = {
                    'text_length': text_length,
                    'avg_tokens': avg_tokens,
                    'avg_chars_per_token': avg_chars_per_token,
                    'successful_models': len(successful_results)
                }

        for language, lang_results in by_language.items():
            print(f"\n{language.upper()}:")
            print("-" * 60)
            print(f"{'Model':<40} {'Tokens':<8}")
            print("-" * 60)

            for result in sorted(lang_results, key=lambda x: x.input_tokens, reverse=True):
                if result.input_tokens > 0:  # Show only successful requests
                    print(f"{result.model:<40} {result.input_tokens:<8}")

            # Show language statistics
            if language in language_stats:
                stats = language_stats[language]
                print("-" * 60)
                print(f"Text length: {stats['text_length']} characters")
                print(f"Average tokens: {stats['avg_tokens']:.1f}")
                print(f"Characters per token: {stats['avg_chars_per_token']:.2f}")
                print(f"Successful models: {stats['successful_models']}")

        # General statistics
        print(f"\n{'='*80}")
        print("GENERAL STATISTICS")
        print(f"{'='*80}")

        successful_results = [r for r in results if r.input_tokens > 0]
        failed_count = len(results) - len(successful_results)

        print(f"Successful requests: {len(successful_results)}")
        print(f"Failed requests: {failed_count}")

        if successful_results:
            avg_input_tokens = sum(r.input_tokens for r in successful_results) / len(successful_results)

            print(f"Average input tokens: {avg_input_tokens:.1f}")

        # Language comparison
        if language_stats:
            print(f"\n{'='*80}")
            print("LANGUAGE COMPARISON")
            print(f"{'='*80}")
            print(f"{'Language':<12} {'Chars':<8} {'Avg Tokens':<12} {'Chars/Token':<12} {'Models':<8}")
            print("-" * 60)

            for language, stats in language_stats.items():
                print(f"{language:<12} {stats['text_length']:<8} {stats['avg_tokens']:<12.1f} {stats['avg_chars_per_token']:<12.2f} {stats['successful_models']:<8}")

    def save_results_to_file(self, results: List[ModelResult], filename: str = "token_results.md"):
        """Saves results to Markdown file"""
        # Group results by language for statistics
        by_language = {}
        for result in results:
            if result.language not in by_language:
                by_language[result.language] = []
            by_language[result.language].append(result)

        # Calculate language statistics
        language_stats = {}
        for language, lang_results in by_language.items():
            successful_results = [r for r in lang_results if r.input_tokens > 0]
            if successful_results:
                original_text = self.test_texts.get(language, "")
                text_length = len(original_text)
                avg_tokens = sum(r.input_tokens for r in successful_results) / len(successful_results)
                avg_chars_per_token = text_length / avg_tokens if avg_tokens > 0 else 0

                language_stats[language] = {
                    'text_length': text_length,
                    'avg_tokens': avg_tokens,
                    'avg_chars_per_token': avg_chars_per_token,
                    'successful_models': len(successful_results)
                }

        # Use results directory if specified
        results_dir = os.getenv('RESULTS_DIR', '.')
        os.makedirs(results_dir, exist_ok=True)
        filepath = os.path.join(results_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("# GOAL\n\n")
            f.write("Your goal is to write a report about tokenization test results. You need to analyze the results and create two graphs, selecting the most and least efficient languages and models, along with all other useful information about the results. Do not include any other information(about tests itself, or any other information) in your response. \n\n")
            f.write("## Tokenization Testing Results\n\n")


            # Summary
            successful_tests = len([r for r in results if r.input_tokens > 0])
            failed_tests = len(results) - successful_tests
            f.write(f"**Total tests:** {len(results)} | **Successful:** {successful_tests} | **Failed:** {failed_tests}\n\n")

            # Table 1: Results by Model and Language
            f.write("## Results by Model and Language\n\n")
            f.write("| Model | Language | Tokens |\n")
            f.write("|-------|----------|--------|\n")

            for result in sorted(results, key=lambda x: (x.model, x.language)):
                if result.input_tokens > 0:
                    f.write(f"| {result.model} | {result.language} | {result.input_tokens} |\n")
                else:
                    f.write(f"| {result.model} | {result.language} | ❌ Failed |\n")

            f.write("\n")

            # Table 2: Language Statistics
            f.write("## Language Statistics\n\n")
            f.write("| Language | Characters | Avg Tokens | Chars/Token | Models |\n")
            f.write("|----------|------------|------------|-------------|--------|\n")

            for language, stats in language_stats.items():
                f.write(f"| {language} | {stats['text_length']} | {stats['avg_tokens']:.1f} | {stats['avg_chars_per_token']:.2f} | {stats['successful_models']} |\n")

            f.write("\n")

            # Additional analysis
            f.write("## Analysis\n\n")
            if language_stats:
                # Find most efficient language (highest chars per token)
                most_efficient = max(language_stats.items(), key=lambda x: x[1]['avg_chars_per_token'])
                f.write(f"- **Most efficient tokenization:** {most_efficient[0]} ({most_efficient[1]['avg_chars_per_token']:.2f} chars/token)\n")

                # Find least efficient language (lowest chars per token)
                least_efficient = min(language_stats.items(), key=lambda x: x[1]['avg_chars_per_token'])
                f.write(f"- **Least efficient tokenization:** {least_efficient[0]} ({least_efficient[1]['avg_chars_per_token']:.2f} chars/token)\n")

                # Average across all languages
                avg_chars_per_token = sum(stats['avg_chars_per_token'] for stats in language_stats.values()) / len(language_stats)
                f.write(f"- **Average chars per token:** {avg_chars_per_token:.2f}\n")

        print(f"\nResults saved to file: {filepath}")

def main():
    # Get API key from environment variable
    api_key = os.getenv('OPENROUTER_API_KEY')

    if not api_key:
        print("Error: OpenRouter.ai API key not found", flush=True)
        print("Set the OPENROUTER_API_KEY environment variable", flush=True)
        print("Example: export OPENROUTER_API_KEY='your-api-key-here'", flush=True)
        return

    # Create tester and run testing
    tester = OpenRouterTester(api_key)

    print("Tokenization testing script via OpenRouter.ai API", flush=True)
    print("=" * 60, flush=True)

    results = tester.test_all_combinations()
    tester.print_results(results)
    tester.save_results_to_file(results)

if __name__ == "__main__":
    main()
