'''
n = 30
while n > 0:
    print(n)
    n = n - 1

print('Lift off!')
'''

'''
while True:
    line = raw_input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
'''

'''
while True:
    line = raw_input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
'''
'''
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    print(num)

print("Maximum", largest)
'''

largest = None
smallest = None

while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue
    if smallest is None:
        smallest = num 
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num

def done(largest,smallest):
    print "Maximum is", int(largest)  
    print "Minimum is", int(smallest)

done(largest,smallest)
