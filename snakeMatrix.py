import math
def snakeMatrix(n):
    matrix=[[0]*n for _ in range(n)]
    n1=math.ceil(n*n/2)
    n2=n*n+1
    isLeft=False
    m=1
    i=0
    while m<n1:
        row=i
        while row>=0:
            col=i-row
            if isLeft:
                matrix[row][col]=m
                matrix[n-1-row][n-1-col]=n2-m
            else:
                matrix[col][row]=m
                matrix[n-1-col][n-1-row]=n2-m
            m+=1
            if m>=n1:
                break
            row-=1
        i+=1
        isLeft=not isLeft
    return matrix
