def floyd_warshall(distance_matrix):
  n=len(distance_matrix)
  distance=[[0]*n for _ in range(n)]
  path=[[0]*n for _ in range(n)]#store the nearest vertex to destination
  #initialization
  for i in range(n):
    for j in range(n):
      distance[i][j]=distance_matrix[i][j]
      if distance_matrix[i][j]!=sys.maxsize and i!=j:
        path[i][j]=i
      else:
        path[i][j]=-1
  #update      
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if distance[i][k]==sys.maxsize or distance[k][j]==sys.maxsize:
          continue
        if distance[i][j]>distance[i][k]+distance[k][j]:
          distance[i][j]=distance[i][k]+distance[k][j]
          path[i][j]=path[k][j]
  #checck negative weight:
    for i in range(n):
      if distance[i][i]<0:
        #negative weight!!!
  #def printPath(self, path, i, j):
      stack=[]
      stack.append(j)
      while True:
        j=path[i][j]
        if j==-1:
          return
        stack.append(j):
          if j==i:
            break
