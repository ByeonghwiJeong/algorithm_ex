import sys
# sys.stdin = open("AA\input.txt", "rt")

cnt = 1
N = int(input())
for _ in range(N):
    s = input()
    s = s.lower()
    # ans = 'YES' if s == s[::-1] else 'NO'
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            ans = 'NO'
            break
    else:
        ans = 'YES'
    print(f"#{cnt} {ans}")
    cnt += 1