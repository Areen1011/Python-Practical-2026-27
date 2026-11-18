try:
    f = open("student.txt", "r")

    print("File Name:", f.name)
    print("File Mode:", f.mode)

    print("\nUsing read():")
    print(f.read())

    f.seek(0)
    print("\nUsing readline():")
    print(f.readline())

    f.seek(0)
    print("\nUsing readlines():")
    print(f.readlines())

    print("Current Position:", f.tell())

    f.seek(0)
    print("Position After Seek:", f.tell())

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")

else:
    print("\nFile operations completed successfully")

finally:
    try:
        f.close()
        print("File closed successfully")
    except NameError:
        print("File was not opened")

