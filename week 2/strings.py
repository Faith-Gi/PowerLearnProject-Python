#string

string1 = 'programming'
string1 ='programming'

name ='python'
print(name)
message = 'I love python'
print(message)

#indexing
greet='hello'
print(greet[1])

#negative indexing
greet='hello'
print(greet[-4])

#slicing
greet='hello'
print(greet[1:4])

message='hola'

print(message)

message='hello friends'
print(message)


#multiline string
message = """
Never give up
Never let you down
"""
print(message)

#compare 2 strings
str1 ='Hello world'
str2='I love java'
str3='Evening'
print(str1==str2)
print(str1==str3)

#join 2 or more strings
greet = 'hello'
name = 'sasha'
result=greet + name
print(result)
#iterate string
greet='hello'
for letter in greet:
    print(letter)

    #len string
    greet='hello'
    print(len(greet))

    #membership test
    print('a' in 'program')
    print('at' not in 'battle')

    #escape sequences
    example="He said, what is there" " "
    print(example)

    example="He said, \Whats there?\""
    example="He said,Whats\ there?"

    print(example)

    #f-strings
    name='Sarah'
    country='UK'
    print(f'{name} is from {country}')
