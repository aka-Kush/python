print("Hello World");
# this is a comment
a = 2;
print(a);

# example of a multiline statement
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a);

# conditional operation
if(5>2):
    print("5 is greater than 2.");

# different data-types
x,y,z = 5,3.2,"Hello";
print(x," = ",type(x));
print(y," = ",type(y));
print(z," = ",type(z));

# concatenation (string to string)
strType = "awesome";
print("Python is " + strType);

# concatenation (string to int) == error
intType = 12;
# print("I'm " + intType + " years old")

# alternative
print("I'm " + str(intType) + " years old");

# binary Literal (0b)
print(0b1010);
# ocatal Literal (0o)
print(0o310);
# decimal Literal
print(100);
# Hexadecimal Literal (0x)
print(0x12c);
# float literal 
print(10.5);
print(1.5e2);
# complex literal
comLit = 3.14j;
print(comLit);
print(comLit.imag, comLit.real);

string = "This is a string";
print(string);
characterType = 'C';
print(characterType);
multilineStr = """This is a multiline
string""";
print(multilineStr);

# bool
isIttrue = (1 == True);
isItfalse = (1 == False);
x = True + 4;
y = False + 10;
print("isIttrue is ", isIttrue);
print("isItfalse is ", isItfalse);
print("x is ", x);
print("y is ", y);















