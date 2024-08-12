import sys
input = sys.stdin.readline

N = int(input().rstrip())
li = sorted([int(input().rstrip()) for _ in range(N)])
print('\n'.join(map(str,li)))
