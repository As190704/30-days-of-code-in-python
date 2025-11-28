#q1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age=  int(input("Enter your age"))

if age>= 18:
    print ("You are eligible for learn how to drive.")
else :
    missingyears = 18 -age
    print (f"please wait {missingyears} more to drive.")