'''
def computepay(h,r):
    return 42.37

hrs = input("Enter Hours:")
p = computepay(10,20)
print("Pay",p)
'''
def computepay(hours,rate):
 if hours>40.0:
  p = rate * 40.0
  p = p+(1.5*rate*(hours-40))
 elif hours < 40.0:
  p = rate*hours

hours = float(raw_input("Enter worked hours: "))
rate = float(raw_input("Enter Pay rate per hour: "))
print(p)
'computepay(hours,rate)'
