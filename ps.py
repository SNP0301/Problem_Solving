N, M = map(int,input().split())
pocketmon_name_dct = dict()
pocketmon_num_dct = dict()

for i in range(1,N+1):
    name = input()
    pocketmon_name_dct[i] = name
    pocketmon_num_dct[name] = i

for i in range(M):
    quiz = input()
    if 60<=ord(quiz[0])<=90:
        print(pocketmon_num_dct[quiz])
    else:
        quiz = int(quiz)
        print(pocketmon_name_dct[quiz])



