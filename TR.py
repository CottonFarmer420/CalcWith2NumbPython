print("Hello")

ui = int(input("1 für +, 2 für -, 3 für *, 4 für /"))
if ui > 4:
        print("Error")
        exit()

x = float(input("Choose your first number!"))
y = float(input("Choose your second number!"))

if ui == 1:
        print(x + y)

elif ui == 2:
        print(x - y)

elif ui == 3:
        print(x * y)

elif ui == 4:
        print(x / y)

else:
    print("Error")
    exit()
