def word_frequeny(text: str) -> dict:
    result = {}
    check = {}
    
    for i in text:
        if i in check:
            check[i] += 1
        else:
            check[i] = 1
    for a,b in check.items():
        if b > 1:
            result[a] = b
    return result

print(word_frequeny("HelloWo rldThisIsThailand"))
print(word_frequeny("azxcvbnm"))