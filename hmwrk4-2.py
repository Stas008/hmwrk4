k=int(input("Введите k: "))
multipliers=[]
i=2
while (i!=k):
    if k % i == 0:
        multipliers.append(i)
        k = k / i
    else: 
        i +=1
multipliers.append(i)
print (multipliers)