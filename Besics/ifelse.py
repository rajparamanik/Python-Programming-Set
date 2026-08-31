# ifelse is a conditional statement
#  in Python that allows you to execute different blocks of code based on certain conditions.

# The basic syntax of an ifelse statement is as follows:
# if condition:
if True:
    # code block to be executed if the condition is True
    print("The condition is True.")

else:
    # code block to be executed if the condition is False
    print("The condition is False.")



student_age = input("Enter your age: ") # This will take input from the user
if int(student_age) >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")


# nested ifelse statement example in Python
student_age = input("Enter your age: ") # This will take input from the user
if int(student_age) >= 18:
    print("You are an adult.")
    if int(student_age) >= 21:
        print("You are also eligible to drink alcohol.")
    else:
        print("You are not eligible to drink alcohol.")