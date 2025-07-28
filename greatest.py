a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter anothe number: "))

if a>b and a>c:
    print("The greatest number is",a)

elif b>a and b>c:
    print("The greatest number is",b)

else:
    print("The lowest number is",c)