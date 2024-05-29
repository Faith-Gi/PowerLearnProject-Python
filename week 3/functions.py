#create a function
#call a function

#function arguments/parameters
def add_nums(a,b):
        answer= a+b
        return answer
    
total=add_nums(2,13)
print('Total :',total)


#arbitrary arguments(args)
def add_nums(*nums):
          sum=0
          for num in nums:
                  sum += num
          return sum
print('Total:',add_nums(2,3,4,5,6,7))

#arbitrary keyword arguments(kwargs)

def add_ages(**ages):
        sum=0
        for k,v in ages.items():
            sum+= v
        return sum
print('Total:',add_ages(julia=20,skinny=19,buli=21))

#local scope

def add_nums(a,b):
        answer=a+b
        return answer
print(add_nums(2,13))

#enclosed scope
def add_nums(a,b):
        answer=a+b
        def double_it():
                double=answer*2
                print(double)
                double_it()
        return answer
print(add_nums(2,13))

#global scope
global_var=13
def add_nums(a,b):
        total=a+b
        print('Global_var in outer function:',global_var)
        def double_it():
                double=total*2
                print('Global_var in inner function:',global_var)

                double_it()
                return total
add_nums(13,5)

#built_in function

#lambda function
snack= lambda:print('peanuts')
snack()

#lambda function with arguments

def num_square(num):
        return num**2
print('Square of num is :',num_square(9))

num_square = lambda num:num**2
print('square of num is',num_square(9))

#palindrome

def isPalindrome(string):
        if(string == string[::-1]):
          return "A Palindrome"
        else:
         return 'Not a Palindrome'
string = input('Enter a string')
print(isPalindrome(string))

isPalindrome = lambda string : 'Palindrome' if string == string[::-1] else 'Not palindrome'
string = input('Enter a string:')
print(isPalindrome(string))

def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)
#
def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)
#
for num in range(1, 5):
    print(num)

    #
    x = 0
for i in range(3):
    x = x + i
    print(x)

    