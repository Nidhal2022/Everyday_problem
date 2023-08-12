N1 = int(input('Enter First number : '))
N2 = int(input('Enter Second number : '))
N3 = int(input('Enter Third number : '))
def largest(num1, num2, num3):
   if (num1 > num2) and (num1 > num3):
       largest_num = num1
   elif (num2 > num1) and (num2 > num3):
       largest_num = num2
   else:
       largest_num = num3
   print("The largest of the 3 numbers is : ", largest_num)
print(largest(N1,N2,N3))