first_word, second_word = input(), input()
first_word_bin = ''
second_word_bin = ''
result = ''
if len(first_word) == len(second_word):
    for i in range(len(first_word)):
        char1 = bin(ord(first_word[i]))[2:]
        char1 = '0' * (8 - len(char1)) + char1
        first_word_bin += char1
        char2 = bin(ord(second_word[i]))[2:]
        char2 = '0' * (8 - len(char2)) + char2
        second_word_bin += char2
        char0 = ''
        for j in range(len(char1)):
            char0 += str(int(char1[j])^int(char2[j]))
        result += char0
    print(first_word_bin)
    print(second_word_bin)
    print(result)
else:
    print('слова разной длины')
