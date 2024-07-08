import sys
# 再起回数の上限を上げる
sys.setrecursionlimit(10**6)
from collections import defaultdict

n, m = map(int, input().split())
node = defaultdict(list)

for _ in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  node[a].append(b)
  node[b].append(a)
  
def dfs(s):
  used[s] = True
  for e in node[s]:
    if not used[e]:
      dfs(e)

used = [False for _ in range(n)]
dfs(0)
