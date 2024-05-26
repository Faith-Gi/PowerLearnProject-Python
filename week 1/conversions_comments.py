integer_number = 20
float_number = 10.90
now_number= integer_number + int(float_number)
print('value:',now_number)
print('Data Type:',type(now_number))
#explicit type conversion
num_string='20'
num_integer= 29
print('Data type of num_string before Type Casting:',type(num_string))
num_string = type(num_string)
print('Data type of num_string after Type Casting:',type(num_string))

num_sum= num_integer + num_string
print('sum:',num_sum)
print('Data type of num_sum:' ,type(num_sum))
