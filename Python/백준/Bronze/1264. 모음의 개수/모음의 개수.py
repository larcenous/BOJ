from collections import Counter
vowel = ['a','e','i','o','u','A','E','I','O','U']
while True :
    vowel_cnt = 0
    string = input().rstrip()
    if string =='#' :
        break
    cnt = Counter(string)
    for element in vowel :
        try :
            vowel_cnt += cnt[element]
        except :
            pass
    print(vowel_cnt)