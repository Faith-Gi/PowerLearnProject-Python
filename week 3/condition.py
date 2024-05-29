#if statement

num = 10
if num >=10:
    print("the number is ten")

    #if else statement

weekday = ['Monday' ,'Tuesday','Wednesday','Thursday','Friday']
if weekday:
        print("wake up at 6:30")

else:
    print("sleep")

#if..elif..else statement

grade = 78

if grade>=90:
     print('A')

elif grade>= 80:
     print('B')
elif grade>=70:
     print('C')
elif grade>=60:
     print('D')
else:
     print('F')

     #for loop
     names = ['becky','hannah','talia','rosa']
     for name in names:
          print(name)

#range function for loops
welcome_message ='Welcome'
for i in range(10):
     print(welcome_message)

     #while loop
     count=0
     while count<=2:
          print(count)
          count+=1

          #using for loop
          colors=['blue','white','yellow','purple']
          color_i_want='purple'
          for color in colors:
               if color==color_i_want:
                    print("I have it")
                    break
               print(color)

               #using while loop
               colors=['blue','white','yellow','purple']
          color_i_want='purple'
          length=len(colors)
          count=0
          while count< length:
               print(colors[count])

               if colors[count]==color_i_want:
                    print('I have it')
                    break
               count+=1
               #continue statement

               ages=[12,25,21,35]
               for age in ages:
                    if age<21:
                         continue
                    print(age)
#nested loops
groups=[['paul','skinny'],['ahmed','gregory']]
for group in groups:
     for name in group:
          print(name)