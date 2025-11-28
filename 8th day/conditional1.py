#q1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age=  int(input("Enter your age"))

if age>= 18:
    print ("You are eligible for learn how to drive.")
else :
    missingyears = 18 -age
    print (f"please wait {missingyears} more to drive.")

#q2Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

age =  int(input("Enter your age"))
my_age = 21

if my_age > age 
   diff =my_age-age
   if diff==1:
    print("you are one year older .")
   else:
    print(f"you are {diff} years older.")

elif age > my_age
    diff = age -my_age
    if diff == 1:
        print ("I am one year older.")
    else:
        print(f"you are {diff} years younger old.")

else:
    print("You are as old as me !\n")
    print("What are you doing.")