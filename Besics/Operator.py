# Operators in python are special symbols that carry out arithmetic or logical computation. 
# The value that the operator operates on is called the operand.

# Arithemetic Operators: Used to perform mathematical operations on numeric values.

# + (Addition), 
Addnum1=int(input("Enter the first number: "))
Addnum2=int(input("Enter the second number: "))
AddResult=Addnum1+Addnum2
print("The sum is:", AddResult)

# - (Subtraction), 
Subnum1=int(input("Enter the first number: "))
Subnum2=int(input("Enter the second number: "))
SubResult=Subnum1-Subnum2
print("The difference is:", SubResult)

# * (Multiplication), 
Mulnum1=int(input("Enter the first number: "))
Mulnum2=int(input("Enter the second number: "))
MulResult=Mulnum1*Mulnum2
print("The product is:", MulResult)

# / (Division)
Divnum1=int(input("Enter the first number: "))
Divnum2=int(input("Enter the second number: "))
DivResult=Divnum1/Divnum2
print("The quotient is:", DivResult)

# // (Floor Division: discards decimal remainder)% 
floor1=int(input("Enter the first number: "))
floor2=int(input("Enter the second number: "))
floorResult=floor1//floor2
print("The floor division result is:", floorResult)

# (Modulus: returns division remainder)
mod1=int(input("Enter the first number: "))
mod2=int(input("Enter the second number: "))
modResult=mod1%mod2
print("The modulus result is:", modResult)

# ** (Exponentiation: power)
exp1=int(input("Enter the first number: "))
exp2=int(input("Enter the second number: "))
expResult=exp1**exp2
print("The exponentiation result is:", expResult)


# Comperation operators are used to combine conditional statements.

 
# == (Equal to),
Equalnum1=int(input("Enter the first number: "))
Equalnum2=int(input("Enter the second number: "))
if Equalnum1==Equalnum2:
    print("The numbers are equal.")

#  != (Not equal to), 
NotEqualnum1=int(input("Enter the first number: "))
NotEqualnum2=int(input("Enter the second number: "))
if NotEqualnum1!=NotEqualnum2:
    print("The numbers are not equal.")

# > (Greater than), 
GreaterNum1=int(input("Enter the first number: "))
GreaterNum2=int(input("Enter the second number: "))
if GreaterNum1>GreaterNum2:
    print("The first number is greater.")

# < (Less than),
LessNum1=int(input("Enter the first number: "))
LessNum2=int(input("Enter the second number: "))
if LessNum1<LessNum2:
    print("The first number is less.")

#  >= (Greater than or equal to),
GreaterEqualNum1=int(input("Enter the first number: "))
GreaterEqualNum2=int(input("Enter the second number: "))
if GreaterEqualNum1>=GreaterEqualNum2:
    print("The first number is greater than or equal to the second number.")

#  <= (Less than or equal to)
LessNum1=int(input("Enter the first number: "))
LessNum2=int(input("Enter the second number: "))
if LessNum1<=LessNum2:
    print("The first number is less than or equal to the second number.")



# Logical Operators: Used to combine


#  conditional statements.and (Returns True if both statements are true)
Logicnum1=int(input("Enter the first number: "))
Logicnum2=int(input("Enter the second number: "))
if Logicnum1>=0 and Logicnum2==Logicnum1:
    print("Both numbers are same.")
else:
    print("At least one number is not same.")

# or (Returns True if at least one statement is true)
Logicnum1=int(input("Enter the first number: "))
Logicnum2=int(input("Enter the Second number: "))
if Logicnum1>=0 or Logicnum2==Logicnum1:
    print("Both numbers are same.")
else:
    print("At least one number is not same.")

# not (Reverses the logical state)
Logicnum1=int(input("Enter the first number: "))
Logicnum2=int(input("Enter the Second number: "))
if Logicnum1>=0 and not Logicnum2<0:
    print("Both numbers are same.")
else:
    print("At least one number is not same.")
