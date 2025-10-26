## English

As machine learning algorithms process numbers rather than text, the text must be converted to numbers. In the first step, a vocabulary is decided upon, then integer indices are arbitrarily but uniquely assigned to each vocabulary entry, and finally, an embedding is associated to the integer index. Algorithms include byte-pair encoding (BPE) and WordPiece. There are also special tokens serving as control characters, such as [MASK] for masked-out token (as used in BERT), and [UNK] ("unknown") for characters not appearing in the vocabulary. Also, some special symbols are used to denote special text formatting. For example, "Ġ" denotes a preceding whitespace in RoBERTa and GPT and "##" denotes continuation of a preceding word in BERT.

Tokenization also compresses the datasets. Because LLMs generally require input to be an array that is not jagged, the shorter texts must be "padded" until they match the length of the longest one. The average number of words per token depends on the language. In English, the ratio is typically around 0.75 words per token, with 4 characters per token on average.


## Russian

Поскольку алгоритмы машинного обучения обрабатывают числа, а не текст, текст должен быть преобразован в числа. На первом этапе выбирается словарь, затем каждому элементу словаря произвольно, но уникально присваивается целочисленный индекс, и, наконец, к целочисленному индексу привязывается векторное представление (эмбеддинг). Алгоритмы включают кодирование пар байтов (BPE) и WordPiece. Также существуют специальные токены, служащие управляющими символами, такие как [MASK] для замаскированного токена (как используется в BERT) и [UNK] («неизвестный») для символов, не входящих в словарь. Кроме того, некоторые специальные символы используются для обозначения особого форматирования текста. Например, "Ġ" обозначает предшествующий пробел в RoBERTa и GPT, а "##" обозначает продолжение предыдущего слова в BERT.

Токенизация также сжимает наборы данных. Поскольку большие языковые модели (LLM) обычно требуют, чтобы входные данные были массивом без «зазубрин», более короткие тексты должны быть «дополнены» до длины самого длинного. Среднее количество слов на токен зависит от языка. В английском языке это соотношение обычно около 0,75 слова на токен, при среднем количестве 4 символов на токен.

## Ukrainian

Оскільки алгоритми машинного навчання обробляють числа, а не текст, текст повинен бути перетворений у числа. На першому етапі вибирається словник, потім кожному елементу словника випадково, але унікально присвоюється цілий індекс, і, нарешті, до цілочисельного індексу прив'язується векторне представлення (ембеддинг). Алгоритми включають кодування пар байтів (BPE) та WordPiece. Також існують спеціальні токени, які служать керуючими символами, такі як [MASK] для замаскованого токена (як використовується в BERT) та [UNK] («невідомий») для символів, що не входять до словника. Крім того, деякі спеціальні символи використовуються для позначення особливого форматування тексту. Наприклад, "Ġ" позначає попередній пробіл у RoBERTa та GPT, а "##" позначає продовження попереднього слова в BERT.

Токенізація також стискає набори даних. Оскільки великі мовні моделі (LLM) зазвичай вимагають, щоб вхідні дані були масивом без «зазубрин», коротші тексти повинні бути «доповнені» до довжини найдовшого. Середня кількість слів на токен залежить від мови. В англійській мові це співвідношення зазвичай близько 0,75 слова на токен, при середній кількості 4 символів на токен.

## Finnish

Koska koneoppimisalgoritmit käsittelevät numeroita tekstin sijaan, teksti täytyy muuntaa numeroiksi. Ensimmäisessä vaiheessa päätetään sanasto, sitten jokaiselle sanaston merkinnälle annetaan mielivaltaisesti mutta yksilöllisesti kokonaislukuihin perustuvat indeksit, ja lopuksi indeksiin liitetään upotus (embedding). Algoritmeihin kuuluvat muun muassa byte-pair encoding (BPE) ja WordPiece. On myös erikoistokenoita, jotka toimivat ohjausmerkkeinä, kuten [MASK] piilotetulle tokenille (käytössä mm. BERTissä) ja [UNK] ("tuntematon") merkeille, joita ei esiinny sanastossa. Lisäksi käytetään erityisiä symboleita spesiaalin tekstin muotoilun ilmaisemiseen. Esimerkiksi "Ġ" merkitsee edeltävää välilyöntiä RoBERTassa ja GPT:ssä, ja "##" tarkoittaa sanan jatkumista BERTissä.

Tokenisointi myös pakkaa tietoaineistot. Koska suurten kielimallien (LLM) syötteiden täytyy yleensä olla ei-epäsäännöllinen taulukko, lyhyemmät tekstit täytyy "täyttää" pisimmän tekstin mittaisiksi. Sanojen keskimääräinen määrä per token riippuu kielestä. Englannissa tämä suhdeluku on tyypillisesti noin 0,75 sanaa per token ja keskimäärin 4 kirjainta per token.

## Korean

## English

머신러닝 알고리즘은 텍스트가 아니라 숫자를 처리하므로, 텍스트는 숫자로 변환되어야 합니다. 첫 번째 단계에서는 어휘집을 결정하고, 각 어휘 항목에 임의적이지만 고유한 정수 인덱스를 할당한 다음, 해당 정수 인덱스에 임베딩(embedding)이 연결됩니다. 알고리즘에는 바이트-쌍 인코딩(Byte Pair Encoding, BPE)과 WordPiece 등이 포함됩니다. 또한 [MASK](BERT에서 사용된 마스킹 토큰)나 [UNK](어휘집에 없는 문자를 나타내는 "unknown" 토큰) 같은 제어 문자 역할을 하는 특수 토큰들도 존재합니다. 그 외에도, 특수 문자들이 특별한 텍스트 서식을 나타내는 데 사용됩니다. 예를 들어, RoBERTa와 GPT에서 "Ġ"는 앞에 오는 공백을, BERT에서는 "##"가 이전 단어의 연속임을 나타냅니다.

토크나이즈(Tokenization) 과정은 데이터셋을 압축하기도 합니다. 대형 언어 모델(LLM)에서는 입력이 '비정방 배열(jagged array)'이 아니어야 하므로 짧은 텍스트는 가장 긴 텍스트의 길이에 맞추어 '패딩'되어야 합니다. 토큰당 평균 단어 수는 언어에 따라 다릅니다. 영어의 경우, 일반적으로 토큰당 약 0.75 단어, 토큰당 평균 4개의 문자 비율을 보입니다.