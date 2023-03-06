def naiveSearch(pat, txt):
    m = len(pat)
    n = len(txt)

    for i in range(n-m+1): # 19 - 4 + 1
        j = 0
        
        while j < m:
            if txt[i+j] != pat[j]:
                break
            j += 1

        if j == m:
            print('Pattern Found at',i)


txt = "AABAACAADAABCAAABAA" # 19
pat = "AABA" # 4

naiveSearch(pat, txt)
