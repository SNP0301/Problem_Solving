'''
[BOJ] 1759. 암호 만들기
T: 2s
M: 128MB
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

l, c = map(int,input().split())
input_character = sorted(list(map(str,input().split())))
vowel = ["a","e","i","o","u"]

def make_password(password, available_character):
    vowel_check = False
    if len(password) == l:
        '''
        for x in vowel:
            if x in password:
                print(password)
                return
        '''
        not_vowel_cnt = 0
        for x in password:
            if x in vowel:
                vowel_check = True
            elif x not in vowel:
                not_vowel_cnt += 1
        if vowel_check and (not_vowel_cnt >= 2):
            print(password)
            return
    for i in available_character:
        if not password:
            next_character_list = [y for y in available_character]
            next_character_list.remove(i)
            make_password(i, next_character_list)
        elif password[-1] < i:
            next_character_list = [y for y in available_character]
            next_character_list.remove(i)
            make_password(password+i, next_character_list)

make_password("",input_character)
