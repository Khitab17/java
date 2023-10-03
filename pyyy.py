a = float(input("Enter 1st intiger : "))
b = float(input("Enter 2nd intiger : "))

print(a)
print("\n")
print(b)

sum = a + b
sub = a - b
mult = a * b
div = a / b 

choice = input("enter your choice : ")
print(choice)
if choice == "+":
    print(sum)
elif choice == "-":
    print(sub)
elif choice == "*":
    print(mult)
elif choice == "/":
    print(div)
else:
    print("\n\nyou have entered an invalid value.")