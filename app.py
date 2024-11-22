#python
#Gym Membershiping by using decisions
print("Welcome to our membership page")
age=eval(input("Enter your age:"))
attendence=eval(input("Enter, how many time do you visit the gym per week?"))
if age<18:
    print("You are eligible for youth membership")
elif age>=18 and attendence<=3:
    print("You are eligible for basic membership")
elif age>=18 and attendence>=3:
    print("You are eligible for premium membership")
else:
    print("Not Eligible")