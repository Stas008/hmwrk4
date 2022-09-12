import random
stepen = ["⁰","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹"]
k=int(input("Введите k: "))
def bigdigit_to_stepen (digit):
    temp_step = ""
    for i in digit:
        temp_step += stepen[int(i)]
    return(temp_step)

def main_task(k):
    result=""
    for i in range(k, 1, -1):
        temp_item=str(random.randint(0,100))+"x"+bigdigit_to_stepen(str(i))+"+"

        result += temp_item
    result += str(random.randint(0,100))+"x"+"+"  
    result += str(random.randint(0,100))  
    return (result)
print(main_task(k))
with open ("result_4_task.txt","w") as data:
    data.write(main_task(k))