capital_city={'Nepal':'Kathamandu' , 'Italy':'Rome', 'England':'London'}
print(capital_city)

numbers = {1:'one',2:'two',3:'three'}
print(numbers)

#add items
print('initial dictionary:',capital_city)
capital_city['Japan'] ='Tokyo'
print('updated dictionary:',capital_city)

#change value
student_id={111:'Erico',112:'Kyle',113:'Butters'}
print('initial dictionary:' ,student_id)

del student_id[111]
student_id[112]='Stan'
print('updated dictionary',student_id)
print(student_id[112])
print(student_id[113])

print(student_id.keys())
print(student_id.values())
#print(student_id.all())
#print(student_id.any())
#print(student_id.len())
#print(student_id.sorted())
print(student_id.clear())


# https://lh6.googleusercontent.com/RARY5swnJ5Ky6LKi_TKWu7bSwLLrze9b7-20-vq78USD2IOy15i-KKH29QqjOWuQg0ApdzRpBv6ZDdrMzuzin9vNu_keTd1MzvTq16V-5t1iV_k0ZGyjx_-Ed8DV-DSaE1qhdd_eMP2HadyX43wlehc

#dictionary membership test
squares= {1:1,3:9,5:25,7:49,9:81}
print(1 in squares)
print(2 not in squares)
print(49 in squares)

#iterating through dict
for i in squares:
    print(squares[i])

