n= int(input("Введите n:"))
arr= list(map(float, input("Введите числа через пробел").split()))
bi=0
md=float('inf')
for i in range(len(arr)):
    df = abs(sum(arr[:i]) - sum(arr[i+1:]))
    if df<md:
        md=df
        bi=i
print(bi)
