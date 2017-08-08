print "Let's build a Calculator"
a = int(raw_input("Enter your first number here: "))
b = int(raw_input("Enter your second number here: "))
print "Type 1 for adding the numbers"
print "Type 2 for subtracting the numbers"
print "Type 3 for multiplying the numbers"
print "Type 4 for dividing the numbers"
c = raw_input("Enter your option here: ")

if c == "1":
    print "Addition of the numbers gives" + str(a+b)
elif c == "2":
    print "Subtraction of the numbers gives" + str(a-b)
elif c == "3":
    print "Multiplying the numbers we get" + str(a*b)
elif c == "4":
    print "Dividing the numbers we get" + str(a/b)
else:
    print "No such option"