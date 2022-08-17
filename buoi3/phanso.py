#import fractions as f
from fractions import  Fraction as F
#a = f.Fraction(2, 5) #2/5
#b = f.Fraction("0.1")
a = F(2, 5) #2/5
b = F("0.1")
print("Tong 2 phan so la", a + b)
print("Hieu 2 phan so la", a - b)
print("Tich 2 phan so la", a * b)
print("Thuong 2 phan so la", a / b)