N = int(input()) # 전체 상담 개수
T = [] # 각 상담을 완료하는데 걸리는 기간
P = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (N + 1) # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
max_value = 0

for _ in range(N):
    x, y = map(int, input().split())
    T.append(x)
    P.append(y)

result = 0

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(N):
    time = 0
    res = 0
    for j in range(i, N):
        if j < time:
            continue
        else:
            time = T[j] + j
            print("time : ", time)
            if time > N:
                break
            else:
                res = P[j] + res
                print("res : ", res)
    result = max(result, res)
    print("result : ", result)

print(result)