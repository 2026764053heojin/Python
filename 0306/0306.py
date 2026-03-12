from collections import Counter

f = open("d;//mobydick.txt", encoding="utf-8")
count = counter(f.read().split())
print("단어 출현 횟수 :", count)