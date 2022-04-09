"""
1. 아이디어
- 2중 for => 값 1 && 방문X => BFS
- BFS 돌면서 그림 개수 +1, 최대값을 갱신
2. 시간복잡도
- BFS : O(V+E)
- V : 500 * 500
- E : 4 * 500 * 500
- V+E : 5 * 250000 = 100만 < 2억 >> 가능!
3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""

import sys
input = sys.stdin.readline
# 가로 m 세로 n , map[n][n]
n, m = map(int, input())
map = [list(map(int, input().split())) for _ in range(n)] 
chk = [[False] * m for _ in range(n)]
 
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y, x) 


cnt = 0
maxv = 0

for i in range(m):
  for j in range(n):
    if map[i][j] == 1 and chk[i][j] == False:
        chk[j][i] = True
        cnt += 1
        maxv = max(maxv, bfs(i, j))

print(cnt)
print(maxv)