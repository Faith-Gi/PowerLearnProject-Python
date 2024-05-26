#same type
numbers= [1,2,3]
print(numbers)

#int,str,float
my_list =[]
my_list=[1,'Night',2.3]
print(my_list)

#list index
languages= ['python', 'java', 'C++']
print(languages[2])

letters=['a','b','c','d','e','f','g','h']
print(letters[2:5])
print(letters[4:])
print(letters[:])
print(languages[-3])

#append(add items at end of the list)
numbers = [30, 45,12,78,51]
print('Before Append:' ,numbers)
numbers.append(12)
print('After Append:' ,numbers)

#extend list items
prime_numbers =[2,3,5]
print('List1:' ,prime_numbers)

even_numbers =[2,6,8]
print('List2:' ,even_numbers)

prime_numbers.extend(even_numbers)
print('list after extend:' ,prime_numbers)

#change list items
languages =['python','swift','java','ruby','angular','vue','javascript']
languages[2] = 'C'
print(languages)
#remove /delete items from a list
del languages[1]
print(languages)
del languages[-1]
print(languages)
del languages[0:2]
print(languages)

#using remove
languages.remove('ruby')
print(languages)

#languages.insert('rails')

#languages.pop('python')


#languages.index('python')

#languages.sort('')

#languages.count('')

#languages.reverse('')

#languages.sort('')

#languages.copy('')

#loop to iterate the list
languages=['python','swift','C']

for language in languages:
    print(language)

    #list comprehension
    numbers= [number*number for number in range(1,6)]
    print(numbers)

#tuple with one element
var1=('hello')
print(type(var1))

var2=('hello')
print(type(var2))

var3='hello'
print(type(var3))

my_tuple = ('a','b','c','d')
print(my_tuple.count('b'))
print(my_tuple.index('d'))