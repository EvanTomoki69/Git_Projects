#Syntax errors
#Occurs when interpreter is unable to parse the code due to code violating Python language rules

x = "Subaru uwu"
if x == "Subaru uwu":
print("x is Subaru!")

#Solution: think about the indentation

#Runtime errors
#Occurs when the program executed have an unexpected condition that prevents from continuing
#We have several types of runtime errors

#NameError
def calculate_sum(a, b):
    total = a + b
    return total

x = 5
y = 10
z = calculate_sum(x, w)
print(z)


def sum_num(a, b, c):
    total = a + b + c  
    return total

w = 1
x = 5
y = 10
t = 11
d = 12
z = sum_num(w, y, d)
print(z)  

#Solution: check the variables

#TyperError
x = "10"
y = 5
z = x + y
print(z)
#Solution: We cannot sum apples with pears

#Logical errors
#These are tricky because the code is running well, but the function expected is not properly executed
def calculate_factorial(n):
    result = 1
    for i in range(1, n):
          result = result * i
    return result   

print(calculate_factorial(5))
#Just add one smile in the sad range :n
