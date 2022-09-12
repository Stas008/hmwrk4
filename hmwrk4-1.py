import math
k=(input("Введите точность: "))
result=""
temp_str=str(math.pi)
result=temp_str[:-(len(temp_str)-len(k))]
print(result)