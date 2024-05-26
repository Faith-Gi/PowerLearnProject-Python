student_id={110,119,120,115,108}
print('Student ID:' ,student_id)

vowel_letters ={'a','e','i','o','u'}
print('vowel letters:' ,vowel_letters)

mixed_set={'hello' , 101,-20,'bye'}
print('set of mixed data types:' ,mixed_set)

#empty set
empty_set=set()
empty_dictionary= {}

print('data type of empty_set:',type(empty_set))
print('data type of empty_dictionary' ,type(empty_dictionary))

#duplicate  of items
numbers={2,3,4,5,6,7,7,8,8}
print(numbers)

#add items
numbers={34,56,12,40}
print('initila set:',numbers)

numbers.add(71)
print('updated set:' ,numbers)

#update items
brands ={'prada' ,'lara','polo','gucci'}
companies={'apple','google','facebook'}
brands.update(companies)
print(companies)

#remove items
languages={'kotlin','html','css'}
print('initial set:' ,languages)
removedValue=languages.discard('html')
print('set after remove():',languages)

#https://lh3.googleusercontent.com/doDj9X9S_CGmk535cO1zVNWf0mL109pQLjcKbR2tH-_WLYuz7r4WMcDbIdhKe8Zm0JRqO18VarUW09yIM81weKH7p4cVV8d83nau6mJmgQiC3l0zrezUCLy_YEMKMZLWDJQ7wxO4AdU0m7R94AoMgAQ

#iterate set
fruits={'kiwi','peach','guava','lemon'}
for fruit in fruits:
    print(fruit)

    even_numbers={2,4,6,8}
    print('set:' ,even_numbers)
    print('total elements:' ,len(even_numbers))

    #set union operation
    a={1,2,3,4}
    b={4,6,9,2}
    print('union using |:',a|b)
    print('union using union():',a.union(b))

    #set intersection operation
    a={1,3,5}
    b={1,2,3}
    print('intersection using &:' ,a&b)
    print('intersection using intersection():',a.intersection(b))

    #set difference
    a={2,3,5}
    b={1,2,6}
    print('difference using &:',a-b)
    print('difference using difference():' ,a.difference(b))

    #set symmetric difference
    a={2,3,5}
    b={1,2,6}
    print('using^:',a^b)
    print('using symmetric_difference():',a.symmetric_difference(b))

    #equal sets
    a={1,3,5}
    b={3,5,1}

    if a == b:
        print('set a and set b are equal')
    else:
        print('set a and set b are not equal')
#https://lh5.googleusercontent.com/nMEvX4blQ1nmjcq7mJHQCOCkwHiSauJlz7dwtyOkTTODgZcCwyN0uqio8en1LWa4b97WB1lV2YYdit-X2m0_RtOi6jyaGZ7LrPjPzlizxPEbNKZ_29TvsV8YSRFEhvqsG4jFYc8XiQ7PGSRGQXTd8Oo
