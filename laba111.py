n= int(input())
A= []
for i in range(n):
    A.append(list(map(int,input().split())))
    count=0
for i in range(n):
    for j in range(n):
        ok = True
        for x in range(max(0, i-1), min(n, i+2)):
            for y in range(max(0, j -1), min(n, j+2)):
                if x ==i and y ==j:
                    if A[i][j]>= A[x][y]:
                        ok= False
        if ok:
            count +=1
print(count)
