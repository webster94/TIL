
# import sys
# sys.stdin = open("sample_input.txt", "r")


def repeated():
    for i in range(len(words)+1):
        if words[i] == words[i+1]:
            return words.pop()


T = int(input())
new_words = []
for tc in range(1, T+1):
    words = list(input())
    for i in range(len(words)+1):
        new_words = new_words.append(words[i])
        print("#{} {}".format(tc, len(new_words)))

repeated()