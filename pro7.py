#through bmi we are finding that the whther the person comes under the underweight,obese,normalweight,underweight
weight=int(input("enter the weight of a person in the kg"))
height=float(input("enter the height of a person in meter"))
bmi=weight/(height**2)
print(f"The BMI of a particular person is {bmi}")
if bmi < 18.5:
    print(f"Your  BMI is {bmi} and you are  underweight.")
elif 18.5 <= bmi < 24.9:
    print(f" Your BMI is {bmi} and you are normal weight.")
elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi} and you are   overweight.")
else:
    print(f"Your BMI is {bmi} and you are  obese.")