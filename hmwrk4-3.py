list1=[1, 1, 2, 3, 4, 5, 5, 7, 8, 8, 9, 12]
result_list=[]
def element_exist (ind, x, mylist):
    flag=False
    for i in range (0, len(mylist)):
        if (x == mylist[i]) & (ind != i):
            flag=True
            break
    return flag
def main_task(list1, result_list):
    for i in range (0, len(list1)):
        if not element_exist(i, list1[i], list1):
            result_list.append(list1[i])
main_task(list1, result_list)
print (result_list)


