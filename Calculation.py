n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())
a, b, c, d = 0, 0, 0, 0

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색 (DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            print("i :", i)
            add -= 1
            print("add1 : ", add)
            dfs(i + 1, now + data[i])
            add += 1
            print("add2 : ", add)
        if sub > 0:
            print("i :", i)
            print("add3 : ", add)            
            sub -= 1
            print("sub1 : ", sub)
            dfs(i + 1, now - data[i])
            sub += 1
            print("sub2 : ", sub)
        if mul > 0:
            mul -= 1
            print("mul1 : ", mul)
            dfs(i + 1, now * data[i])
            mul += 1
            #print("mul2 : ", mul)
        if div > 0:
            div -= 1
            print("div1 : ", div)
            dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
            div += 1
            #print("div2 : ", div)

# DFS 메서드 호출
dfs(1, data[0])