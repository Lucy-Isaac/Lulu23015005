age = int(input("please enter age: "))
gender = input("please enter your gender: ")

if age >= 18:
    if gender == "male":
        print("You're a man")
    else:
        print("you're a woman")
else:
    print("you're a minor")

