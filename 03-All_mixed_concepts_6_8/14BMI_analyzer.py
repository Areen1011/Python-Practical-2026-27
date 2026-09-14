height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight / (height * height)

print("BMI =", bmi)

if bmi < 18.5:
    print("Underweight")
    print("Medical consultation is advised")

elif bmi < 25:
    print("Normal")
    print("Medical consultation is not necessary")

elif bmi < 30:
    print("Overweight")
    print("Medical consultation is advised")

elif bmi < 40:
    print("Obese")
    print("Medical consultation is advised")

else:
    print("Severely obese")
    print("Medical consultation is strongly advised")