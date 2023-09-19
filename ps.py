'''
[BOJ] 2290. LCD Test
T: 2초
M: 128MB
'''
import sys
input = sys.stdin.readline

s, n = map(int,input().split())

n_length = len(str(n))

LCD = list()
LCD_NUMBERS = list()

for _ in range(2*s+3):
    LCD.append([i for i in range(n_length*(s+2))])

for _ in range(2*s+3):
    LCD_NUMBERS.append([" " for _ in range(n_length*(s+2))])


def lcd_test(array):
    for i in array:
        print(i)


lcd_test(LCD_NUMBERS)