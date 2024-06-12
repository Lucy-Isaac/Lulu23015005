name = input("Enter a text Pls: ")
with open("new_text.txt","w")as file:
    new = file.write(name)
    print(f"Total words in the file:{new}:")
