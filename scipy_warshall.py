import time,random

n = 10**3
edge_p = [[0]*n for _ in range(n)]
edge_q = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        edge_p[i][j] = edge_q[i][j] = random.randrange(1,10**9)

#自前実装
s_p = time.time()
for k in range(n):
    for i in range(n):
        for j in range(n):
            edge_p[i][j] = min(edge_p[i][j],edge_p[i][k] + edge_p[k][j])
t_p = time.time()

#scipy
from scipy.sparse.csgraph import csgraph_from_dense,floyd_warshall
s_q = time.time()
G = csgraph_from_dense(edge_q)
edge_q = floyd_warshall(G)
t_q = time.time()


if edge_p[0][1] == int(edge_q[0][1]):
    print("じゅっぴー実装：",t_p-s_p)
    print("scipy:",t_q-s_q)
else:
    print("Error")