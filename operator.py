
#( c) A certain grade of steel is graded according to the following conditions:
#    (i) Hardness must be greater than 50
#    (ii) Carbon content must be less than 0.7
#    (iii) Tensile strength must be greater than 5600
#The grades are as follows:
#    Grade is 10 if all three conditions are met
#    Grade is 9 if conditions (i) and (ii) are met
#    Grade is 8 if conditions (ii) and (iii) are met Grade is 7 if conditions (i) and (iii) are met
#    Grade is 6 if only one condition is met
#    Grade is 5 if none of the conditions are met. .Write a program, which will require the user to give values of hardness, 
#    carbon content and tensile strength of the steel under consideration and output the grade of the steel.


hardness=float(input("Enter the hardness of material :-- "))
carbon_content= float(input("Enter the carbon Content :- "))
tensile_strength=float(input("Enter the tensile strength of material :- "))

condition1= hardness>50
condition2= carbon_content<0.7
condition3= tensile_strength > 5600

if(condition1 and condition2 and condition3):
    print("Grade is 10")
elif(condition1 and condition2):
    print("Grade is 9")
elif(condition2 and condition3):
    print("Grade is 8")
elif(condition1 and condition3):
    print("Grade is 7")
elif(condition1 or condition2 or condition3):
    print("Grade is 6")
else:
    print("Grade is 5")

