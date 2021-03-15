T = int(input())
 
for t in range(T):
    N, K = map(int, input().split())
    pwline = list(map(str, input().strip()))
    rotations = N // 4 # 총 회전수
    pwset = [] # 16진수 str이 담길 리스트, 중복제거
    for i in range(rotations):
        for j in range(4):
            pwset.append(''.join(pwline[j*rotations : (j+1)*rotations]))
        tt = pwline.pop(N-1)        
        pwline.insert(0,tt) # 회전

        temp = set(pwset)
        pwset = list(temp)
    
    dec_list = []
    for pwds in pwset:
        dec_list.append(int(pwds, 16)) # 10진수로 변경
    dec_list.sort(reverse=True) # 내림차순 정렬
     
    print('#%s %s'%(t+1, dec_list[K-1]))