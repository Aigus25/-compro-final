def group_by_signature(word: list) -> list:
    signature_dict = {}
    for i in word:
        signature = ''.join(sorted(i))
        if signature in signature_dict:
            signature_dict[signature].append(i)
        else:
            signature_dict[signature] = [i]
    return list(signature_dict.values())

if __name__ == "__main__":
    word = ["abc", "king", "bca", "cab", "xyz", "zyx", "yxz" , "zxy" , "dog", "kign","sun", "gink", "inkg"]
    print(group_by_signature(word))
    
    word = ["apple", "pale", "leap", "plea", "papel", "Hello"]
    print(group_by_signature(word))