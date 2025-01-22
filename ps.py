"""
*조건을 만족하는 방청객이 두 명 이상이라면 그 중 번호가 가장 작은 방청객의 번호를 출력

[배운 점]
1. index()를 사용해 내가 알고 있는 값의 index를 돌려받을 수 있다.
2. 그림으로 그리지 않고 풀면 어지간하면 틀린다. 문제를 어느 정도 이해했다면 그림도 그려볼 수 있었을 것.
3. 실전 경험이 많이 부족하다. 느슨한 자세로 풀면 언젠가 풀리겠지만 시험 때는 그럴 수 없다.
    3-1. 알고리즘 공부 목적, 실전 경험 목적 등을 구분할 것.
    3-2. 퇴근 후, 주말 등 시간 재고 문제 풀 것 --> 시간 견적 프로님들께 여쭤볼 것.

[입력값 받은 이후 풀이]
1. 기대한 방청객, 실제로 가장 많이 받은 방청객의 인덱스를 알기 위해, 총 2개의 리스트를 선언한다.
    1-1. P-K+1개를 기대하므로, 이 값을 first_max에 저장 -> first_max를 n-1부터 0까지 역순으로 돌면서 first 갱신, 갱신 즉시 break
2. 롤케이크에 번호를 적는다. 이 때, 방청객 번호가 양의 정수임을 감안해서 적는다.
3. 실제로 받은 조각 수를 count()를 활용해 final_max에 저장
    3-1. final_max의 max값을 0부터 n-1까지 찾고, 일치하는 순간 final을 갱신하고 break
4. first, final 출력

[확인할 것]
1. 왜 first, final을 구하는 방법이 다르게 나타나는지 -> 입력값만으로 알 수 있고, 
2. [89032451]에서 IndexError 뜬 이유 --> line 42에서 방청객 번호 입력할 때 한 칸씩 옆으로 밀려서 줬다. 테케만 잘 넘어간 이유도 여기에 해당.

"""
L = int(input())
N = int(input())

first_max = list() ## 방청객들이 기대한 조각수 per 방청객
final_max = list() ## 방청객들이 실제로 받은 조각수 per 방청객

first = -1 ## 기대한 방청객
final = -1 ## 실제로 많이 받은 방청객
final_pieces = -1 ## 실제로 받은 조각

cakes = list()

for _ in range(L):
    cakes.append(0)

for i in range(N):
    p,k = map(int,input().split())
    first_max.append(k-p+1)
    for j in range(p-1,k):
        if cakes[j] == 0:
            cakes[j] = i+1 ## 번호가 안 적혀있을 때만 입력

##print(cakes)

for i in range(N):
    if(max(first_max)==first_max[i]):
        first = i+1
        break

for i in range(N):
    final_max.append(cakes.count(i+1))
    final_pieces = max(final_pieces,cakes.count(i+1))

final = final_max.index(final_pieces)+1

print(first)
print(final)

