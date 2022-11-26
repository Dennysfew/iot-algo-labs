def search(pat, txt):
    i = 0
    j = 0
    alphabet_size = 256
    prime_num = 101
    pattern_hash = 0
    text_hash = 0
    first_index_hash = 1
    result_list = []

    for i in range(len(pat) - 1):
        first_index_hash = (first_index_hash * alphabet_size) % prime_num

    for i in range(len(pat)):
        pattern_hash = (alphabet_size * pattern_hash + ord(pat[i])) % prime_num
        text_hash = (alphabet_size * text_hash + ord(txt[i])) % prime_num

    for i in range(len(txt) - len(pat) + 1):
        if pattern_hash == text_hash:

            for j in range(len(pat)):
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1

            if j == len(pat):
                print("Pattern found at index " + str(i))
                result_list.append(i)
        if i < len(txt) - len(pat):
            text_hash = (alphabet_size * (text_hash - ord(txt[i]) * first_index_hash) + ord(txt[i + len(pat)])) % prime_num
            if text_hash < 0:
                text_hash = text_hash + prime_num

    return result_list


if __name__ == '__main__':
    txt = "hevevhjbevvevvddfvbvne"
    pat = "vevvddf"


    search(pat, txt)

