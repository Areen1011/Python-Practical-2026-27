patients = ["Rahul", "Amit", "Sneha"]

add_patient = input("Enter the name of the patient to add: ")
patients.append(add_patient)

emergency_patient = input("Enter the name of the emergency patient: ")
patients.insert(0, emergency_patient)

print("Current list of patients:", patients)