import time
start = int(input())
end = int(input())
list1=[]
if(start <= 0 or end <=0):
    print("enter valid start and end values")
else:
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                res=i
                list1.append(res)

    for i in list1:
        print(i)
        time.sleep(5)
