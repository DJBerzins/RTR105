Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> prtint(123)

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    prtint(123)
NameError: name 'prtint' is not defined
>>> print(123)
123
>>> print(Čaviņās)
SyntaxError: invalid syntax
>>> print(cau)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(cau)
NameError: name 'cau' is not defined
>>> print('Čau')
Čau
>>> x = 69
>>> y = 2
>>> x = 50
>>> y = _E

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    y = _E
NameError: name '_E' is not defined
>>> z = olas

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    z = olas
NameError: name 'olas' is not defined
>>> x = x + 16
>>> print(x)
66
>>> x = 10
>>> x + 2.5 * x * ( 1 - x )
-215.0
>>> jj = 500
>>> kk = jj % 23
>>> print(kk)
17
>>> type(kk)
<type 'int'>
>>> print(kk)
17
>>> jj = 23
>>> kk = jj % 5
>>> print(kk)
3
>>> type(x)
<type 'int'>
>>> x = 2.5
>>> type(x)
<type 'float'>
>>> i = 43
>>> type(I)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    type(I)
NameError: name 'I' is not defined
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
43.0
>>> type(f)
<type 'float'>
>>> print(500 / 23)
21
>>> print(9 / 4)
2
>>> print(9 / 2)
4
>>> type(f) <class'float'>
SyntaxError: invalid syntax
>>> nam = input('ķas tu esi?')
ķas tu esi?

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    nam = input('ķas tu esi?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam = input('ķas tu esi?') print('čau')
SyntaxError: invalid syntax
>>> lll = 'kā ' + 'īet'
>>> print(lll)
kā īet
>>> nam = input ('Kas tu esi? ')
print ('Sveiks',nam)
Kas tu esi? Daniels

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    nam = input ('Kas tu esi? ')
  File "<string>", line 1, in <module>
NameError: name 'Daniels' is not defined
>>> am = input ('Kas tu esi? ')
print ('Sveiks', nam)
Kas tu esi? Dan

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    am = input ('Kas tu esi? ')
  File "<string>", line 1, in <module>
NameError: name 'Dan' is not defined
>>> nam = input('ķas tu esi?')
ķas tu esi?Daniels

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    nam = input('ķas tu esi?')
  File "<string>", line 1, in <module>
NameError: name 'Daniels' is not defined
>>> 
>>> 
>>> nam = input('Ķas tu esi? ')
Ķas tu esi? D

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    nam = input('Ķas tu esi? ')
  File "<string>", line 1, in <module>
NameError: name 'D' is not defined
>>> nam = D

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    nam = D
NameError: name 'D' is not defined
>>> print(nam)

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(nam)
NameError: name 'nam' is not defined
>>> nam = 1
>>> type(nam)
<type 'int'>
>>> nam = int
>>> nam = input
>>> D

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    D
NameError: name 'D' is not defined
>>> nam = 'd'
>>> print(d)

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(d)
NameError: name 'd' is not defined
>>> nam = raw_input ('Kas tu esi? ')
print ('Sveiks',nam)
Kas tu esi? Daniels
>>> print ('Sveiks',nam)
('Sveiks', 'Daniels')
>>> print 'Sveiks',nam
Sveiks Daniels
>>> inp = raw_input('Europe floor?')
Europe floor?4
>>> usf = int(inp) + 1
>>> print('ūs floor', usf)
('\xc5\xabs floor', 5)
>>> print('US floor', usf )
('US floor', 5)
>>> print 'ŪS stāvs', usf
ŪS stāvs 5
>>> print ('hw')
hw
>>> print 'hw'
hw
>>> rate = 2.75
hrs = input("Enter Hours:")
pay = hrs * rate
print(Pay:)
>>> float
<type 'float'>
>>> float(hrs)

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    float(hrs)
NameError: name 'hrs' is not defined
>>> hrs = input("Enter Hours:")
Enter Hours:35
>>> rate = input("Enter Rate:")
Enter Rate:2.75
>>> float(hrs)
35.0
>>> float(rate)
2.75
>>> pay = hrs * rate
>>> print(pay)
96.25
>>> print(Pay:(pay))
SyntaxError: invalid syntax
>>> print("Pay:"(pay))

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    print("Pay:"(pay))
TypeError: 'str' object is not callable
>>> print('Pay:'(pay))

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print('Pay:'(pay))
TypeError: 'str' object is not callable
>>> print("pay:"pay)
SyntaxError: invalid syntax
>>> print(pay)
96.25
>>> print("pay:"(pay))

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print("pay:"(pay))
TypeError: 'str' object is not callable
>>> print("pay:%s"%(pay))
pay:96.25
>>> 

