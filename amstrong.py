sum1 = 0
temp1 = num1
while temp1 > 0:
   digit = temp1 % 10
   sum1 += digit ** 3
   temp1 //=10
   if num1 == sum1:
   print(num1,"is an Armstrong number")
else:
   print(num1,"is not an Armstrong number")
