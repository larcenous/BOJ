import sys
input = sys.stdin.readline

def DFS(num, i) :
    if num == 6 :
        print(*ans)
        return
    for j in range(i,k) : # 현재 i 보다 큰 값을 전달해 주기 위해 range(i,k)를 사용
        ans.append(s[j]) # 추가-실행-삭제를 반복하며 현재 단계의 상태를 유지 (백트래킹)
        DFS(num+1,j+1)
        ans.pop()

while True :
    t = list(map(int,input().split()))
    k = t[0]
    if k == 0 :
        break
    s = t[1:]
    ans = []
    DFS(0,0)
    print()