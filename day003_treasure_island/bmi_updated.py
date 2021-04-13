weight = input("Enter your weight in kilograms: \n")
height = input("Enter your height in meters: \n")

print("Entered weight: "+weight+ " kgs")
print("Entered height: "+height+ " meter(s)")

bmi = float(weight) / float(height) ** 2

interpretation = ""

if bmi > 35:
    interpretation = "you are clinically obese."
elif bmi > 30:
    interpretation = "you are obese."
elif bmi > 25:
    interpretation = "you are slightly over weight."
elif bmi >= 18.5:
    interpretation = "you are normal weight."
else:
    interpretation = "you are under weight."

print(f"Calculated BMI value is {int(bmi)}, {interpretation}")