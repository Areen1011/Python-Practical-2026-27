physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
maths = int(input("Enter Maths marks: "))

total = physics + chemistry + maths

if (physics >= 60 and chemistry >= 60 and maths >= 65 and total >= 200) or (physics + maths >= 150):
    print("Admitted")
else:
    print("Not Admitted")