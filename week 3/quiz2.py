#for i in range(0,5):
    #print(i)

    #for j in [0,1,2,3,4]:
       # print(j)

        #for k in [0,1,2,3,4,5]:
           # print(k)

            #for l in range(0,5,1):
               # print(l)

list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]



sum = 0



sum1 = 0



for elem in list1:



 if (elem % 2 == 0):



  sum = sum + elem



 continue



if (elem % 3 == 0):



 sum1 = sum1 + elem







print(sum , end=" ")