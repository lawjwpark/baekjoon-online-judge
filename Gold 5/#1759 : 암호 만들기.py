from itertools import combinations

def solution(L, C, characters):
    characters.sort()
    for comb in combinations(characters, L):
        cnt_vowel = 0
        for c in comb:
            if c in 'aeiou':
                cnt_vowel += 1
        if 1 <= cnt_vowel <= L - 2:
            print(*comb, sep='')
    
L, C = map(int, input().split())
characters = input().split()

solution(L, C, characters)