largest = num >= 10
smallest = num <= 2
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    print(num)

print("Maximum", largest)
print("Minimum", smallest)
