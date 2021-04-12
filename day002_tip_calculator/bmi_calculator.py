weight = input("Enter your weight in kilograms: \n")
height = input("Enter your height in meters: \n")

print("Entered weight: "+weight+ " kgs")
print("Entered height: "+height+ " meter(s)")

bmi = int(float(weight) / float(height) ** 2)

print("Calculated BMI value is "+str(bmi))