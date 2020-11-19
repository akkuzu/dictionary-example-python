
stop_number = int(input("Please enter a stop number: "))

result = 0
for i in range(0, stop_number):
    result = result + i
    print(result)
print(result)

start_number = int(input("Please enter a start number: "))
stop_number1 = int(input("Please enter a stop number: "))

result1 = 0
for i in range(start_number, stop_number1):
    result1 += i

print(result1)

start_number2 = int(input("Please enter a start number: "))

if 0 <= start_number2 <= 100:
    stop_number2 = int(input("Please enter a stop number: "))

    if start_number2 <= stop_number2 <= 100:

        result2 = 0
        for i in range(start_number2, stop_number2):
            result2 += i
        print(result2)
    else:
        print("Invalid stop number")


else:
    print("Invalid start number")
