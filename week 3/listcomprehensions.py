#for loop doubled
nums=[5,-9,45,20]
doubled=[]

for num in nums:
    doubled.append(num*2)

    print(doubled)

    nums=[5,-9,45,20]
doubled=[num*2 for num in nums]
print(doubled)
