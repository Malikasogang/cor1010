string1="First Sting.\nSecond String."
string2="""First Sting.
econd String."""
print(string1)
print(string2)
string3="First Sting.\
Second String.\
Third String"
print(string3)

print("Jesnny's text")
print('Jenny\'s text')
print('Jenny\'s \text')
print('Jenny\'s \\text')

str1="Sogang"
str2="UNiversity"
newStr=str1+str2
print(newStr)
newStr=str1*3
print(newStr)
print("S" in newStr)
print("S" not in newStr)

s1="Hi there!"
length=len(s1)
c1=s1[3]
c2=s1[length-1]
print(length)
print(c1)
print(c2)

s="My score is 89. That's good!"
score=s[12:14:]
print(score)
s1=s[:12:]
newS=s1+str(100)+s[14::]
reverseS=newS[::-1]
print(newS)
print(reverseS)

score=89
s="My score is %d. That's %s" %(score, "good")
print(s)
print("rate is %s"%3.456)
print("rate is %d"%3.456)
print("rate is %f"%3.456)
print("rate is %d%%"%75)

print("average=%10.2f"%57.467657)
print("average=%10.2f"%12345678.923)
print("average=%10.2f"%57.4)
print("average=%10.2f"%57)

a=1/3
print("1/3=", a, "(too many digits).")
print("a=%.3f"%a)
print("average=%10d"%59832)


