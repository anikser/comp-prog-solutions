import sys
input = sys.stdin.readline

g = {(7, 3): [(5, 4), (6, 5), (5, 2), (6, 1)], (4, 7): [(2, 6), (3, 5), (6, 6), (5, 5)], (1, 3): [(3, 4), (2, 5), (0, 5), (0, 1), (3, 2), (2, 1)], (6, 4): [(7, 6), (4, 5), (5, 6), (4, 3), (5, 2), (7, 2)], (3, 0): [(5, 1), (4, 2), (1, 1), (2, 2)], (5, 4): [(7, 5), (6, 6), (3, 5), (4, 6), (3, 3), (4, 2), (7, 3), (6, 2)], (0, 7): [(2, 6), (1, 5)], (5, 6): [(7, 7), (3, 7), (3, 5), (4, 4), (7, 5), (6, 4)], (0, 0): [(2, 1), (1, 2)], (1, 6): [(3, 7), (0, 4), (3, 5), (2, 4)], (5, 1): [(7, 2), (6, 3), (3, 2), (4, 3), (3, 0), (7, 0)], (3, 7): [(1, 6), (2, 5), (5, 6), (4, 5)], (0, 3): [(2, 4), (1, 5), (2, 2), (1, 1)], (2, 5): [(4, 6), (3, 7), (0, 6), (1, 7), (0, 4), (1, 3), (4, 4), (3, 3)], (7, 2): [(5, 3), (6, 4), (5, 1), (6, 0)], (4, 0): [(6, 1), (5, 2), (2, 1), (3, 2)], (1, 2): [(3, 3), (2, 4), (0, 4), (0, 0), (3, 1), (2, 0)], (6, 7): [(4, 6), (5, 5), (7, 5)], (3, 3): [(5, 4), (4, 5), (1, 4), (2, 5), (1, 2), (2, 1), (5, 2), (4, 1)], (0, 6): [(2, 7), (2, 5), (1, 4)], (7, 6): [(5, 7), (5, 5), (6, 4)], (4, 4): [(6, 5), (5, 6), (2, 5), (3, 6), (2, 3), (3, 2), (6, 3), (5, 2)], (6, 3): [(7, 5), (4, 4), (5, 5), (4, 2), (5, 1), (7, 1)], (1, 5): [(3, 6), (2, 7), (0, 7), (0, 3), (3, 4), (2, 3)], (3, 6): [(5, 7), (1, 7), (1, 5), (2, 4), (5, 5), (4, 4)], (0, 4): [(2, 5), (1, 6), (2, 3), (1, 2)], (7, 7): [(5, 6), (6, 5)], (5, 7): [(3, 6), (4, 5), (7, 6), (6, 5)], (5, 3): [(7, 4), (6, 5), (3, 4), (4, 5), (3, 2), (4, 1), (7, 2), (6, 1)], (4, 1): [(6, 2), (5, 3), (2, 2), (3, 3), (2, 0), (6, 0)], (1, 1): [(3, 2), (2, 3), (0, 3), (3, 0)], (0, 1): [(2, 2), (1, 3), (2, 0)], (3, 2): [(5, 3), (4, 4), (1, 3), (2, 4), (1, 1), (2, 0), (5, 1), (4, 0)], (2, 6): [(4, 7), (0, 7), (0, 5), (1, 4), (4, 5), (3, 4)], (6, 6): [(4, 7), (4, 5), (5, 4), (7, 4)], (5, 0): [(7, 1), (6, 2), (3, 1), (4, 2)], (7, 1): [(5, 2), (6, 3), (5, 0)], (4, 5): [(6, 6), (5, 7), (2, 6), (3, 7), (2, 4), (3, 3), (6, 4), (5, 3)], (2, 2): [(4, 3), (3, 4), (0, 3), (1, 4), (0, 1), (1, 0), (4, 1), (3, 0)], (5, 5): [(7, 6), (6, 7), (3, 6), (4, 7), (3, 4), (4, 3), (7, 4), (6, 3)], (1, 4): [(3, 5), (2, 6), (0, 6), (0, 2), (3, 3), (2, 2)], (6, 0): [(7, 2), (4, 1), (5, 2)], (7, 5): [(5, 6), (6, 7), (5, 4), (6, 3)], (0, 5): [(2, 6), (1, 7), (2, 4), (1, 3)], (2, 1): [(4, 2), (3, 3), (0, 2), (1, 3), (0, 0), (4, 0)], (4, 2): [(6, 3), (5, 4), (2, 3), (3, 4), (2, 1), (3, 0), (6, 1), (5, 0)], (1, 0): [(3, 1), (2, 2), (0, 2)], (6, 5): [(7, 7), (4, 6), (5, 7), (4, 4), (5, 3), (7, 3)], (3, 5): [(5, 6), (4, 7), (1, 6), (2, 7), (1, 4), (2, 3), (5, 4), (4, 3)], (2, 7): [(0, 6), (1, 5), (4, 6), (3, 5)], (7, 0): [(5, 1), (6, 2)], (4, 6): [(6, 7), (2, 7), (2, 5), (3, 4), (6, 5), (5, 4)], (3, 4): [(5, 5), (4, 6), (1, 5), (2, 6), (1, 3), (2, 2), (5, 3), (4, 2)], (6, 1): [(7, 3), (4, 2), (5, 3), (4, 0)], (3, 1): [(5, 2), (4, 3), (1, 2), (2, 3), (1, 0), (5, 0)], (2, 4): [(4, 5), (3, 6), (0, 5), (1, 6), (0, 3), (1, 2), (4, 3), (3, 2)], (7, 4): [(5, 5), (6, 6), (5, 3), (6, 2)], (2, 0): [(4, 1), (3, 2), (0, 1), (1, 2)], (6, 2): [(7, 4), (4, 3), (5, 4), (4, 1), (5, 0), (7, 0)], (4, 3): [(6, 4), (5, 5), (2, 4), (3, 5), (2, 2), (3, 1), (6, 2), (5, 1)], (1, 7): [(0, 5), (3, 6), (2, 5)], (2, 3): [(4, 4), (3, 5), (0, 4), (1, 5), (0, 2), (1, 1), (4, 2), (3, 1)], (5, 2): [(7, 3), (6, 4), (3, 3), (4, 4), (3, 1), (4, 0), (7, 1), (6, 0)], (0, 2): [(2, 3), (1, 4), (2, 1), (1, 0)]}

start = tuple(map(lambda x: x-1, map(int, input().split())))
end = tuple(map(lambda x: x-1, map(int, input().split())))

#visited = []
q=[[tuple(start)]]

shortest = float('inf')
#visitednodes = []
while(q):
  node = q[0]
  del q[0]
  if node[-1] == end:
    if len(node)<shortest:
      shortest = len(node)
      #print(node)
  #if node not in visited:
  #visited.append(node)
  #visitednodes.append(node[-1])
  if len(node)+1<shortest:
    for child in g[node[-1]]:
      if child not in node:
        q.append(node+[child])
      
print shortest-1