def word_frequeny(text: str) -> dict:
    wordlist = text.split()
    wordcount = {}
    for i in wordlist:
        wordcount[i.lower()] = wordcount.get(i.lower(), 0) + 1
    return wordcount
print(word_frequeny("Hello World Hello Everyone"))
print(word_frequeny("Hello World This Is Thailand"))
print(word_frequeny("This is a test . The python code Is Easy ."))
print(word_frequeny("This is a test . The python code Is Easy . This is a test . test test test"))