"""
단위 작업 내용 및 순서를 아직 잘 모르는 것 같다.
반복문, 조건문 등이 각각 언제/무엇을/언제까지 하는 것인지 명확하게 이해하고 구현할 것.


* K*2로 두거나, 반복문으로 앞으로 갔다가 뒤로 갔다면 못 풀었던 이유 찾아내기
"""

from collections import deque

test = deque()

test.append(1)
print(test)

test.append(2)
print(test)

test.append(3)
print(test)

test.popleft()
print(test)
test.appendleft(1)
print(test)
test.pop()
print(test)