fileName = input("Choose thew file to work with: \n")
print("Choose the operation: \n")
print("1. Write smth in file \n")
print("2. Read file \n")
nuOfOper = input()
if (int(nuOfOper) == 1):
    with open(fileName, "w") as f:
        text = input("enter some text: \n")
        f.write(text)
elif (int(nuOfOper) == 2):
    with open(fileName, "r") as f:
        print(f.read())
else:
    print("Sorry I'm too stupid to do somthing else :3")
 
