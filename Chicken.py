from itertools import combinations

N, m = map(int, input().split())
data, house, chicken = [], [], []

for i in range(N):
    data.append(list(map(int, input().split())))
    for j in range(N):
        if data[i][j] == 1:
            house.append([i, j])
        elif data[i][j] == 2:
            chicken.append([i, j])

# 모든 치킨 집 중에서 m개의 치킨 집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))


# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨 집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨 집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result


# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
