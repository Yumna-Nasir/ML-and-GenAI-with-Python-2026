#ASSIGNMENT 3

#1. Create a function to print first 10 natural numbers.
def printNaturalNumbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")
if __name__ == "__main__":
    n = 10
    printNaturalNumbers(n)

#2. Create a function to calculate sum of first N natural numbers.
def findSum(n):
    sum = 0
    i = 1
    # Iterating over all the numbers between 1 to n
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum
if __name__ == "__main__":
    n = 5
    print(findSum(n))

#3. Create a function to reverse a number.
def rev_num(n):
    if n < 10:
        return n
    return int(str(n % 10) + str(rev_num(n // 10)))
n = 987654
print(rev_num(n))

#4. Create a function to count digits in a number
def countDigit(n):
    if n == 0:
        return 1
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count
if __name__ == "__main__":
    n = 58964
    print(countDigit(n))

#5. Create a function to check palindrome number.
import math
def rev(num):
    return int(num != 0) and ((num % 10) * \
            (10**int(math.log(num, 10))) + \
                        rev(num // 10))
test_number = 9669669
print ("The original number is : " + str(test_number))
res = test_number == rev(test_number)
print ("Is the number palindrome ? : " + str(res))

#6. Create a function to generate Fibonacci series.
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
for i in range(7):
    print(fib(i), end=" ")

#7. Calculator Using Functions that contains the following features;
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")
sel = int(input("Select operation (1-4): "))
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if sel == 1:
    print(n1, "+", n2, "=", add(n1, n2))
elif sel == 2:
    print(n1, "-", n2, "=", sub(n1, n2))
elif sel == 3:
    print(n1, "*", n2, "=", mul(n1, n2))
elif sel == 4:
    print(n1, "/", n2, "=", div(n1, n2))
else:
    print("Invalid input")

#8. Create a text file and store student details. 
def write_student_data(num_students):
 with open("pythonml.txt", "w") as file: 
   for i in range(num_students):
     roll_number = int(input("Enter roll number for student {}: ".format(i+1)))
     name = input("Enter student {}'s name: ".format(i+1))
     marks = float(input("Enter student {}'s marks: ".format(i+1)))
     student_data = "Roll Number: {}, Name: {}, Marks: {}".format(roll_number, name, marks)
     file.write(student_data)
num_students = int(input("Enter the number of students (maximum 3): "))
if num_students > 3:
 print("Error: Maximum of 3 students allowed.")
else:
 write_student_data(num_students)
 print("Student data written to student.txt successfully!")

#9. Read data from a file.
file = open("pythonml.txt", "r")
content = file.read()
print(content)
file.close()

#10. Handle division by zero using exception handling.
a = 16.0
b = 0
try:
    res = a / b
except ZeroDivisionError:
    res = 0
print(res)

#11. Create a Student class with name and marks. 
class Student():
    id = 0
    name = ""
    gender = ""
    total = ""
    per = 0	
    def setData(self,id,name,gender,total,per):	
        self.id = id
        self.name = name
        self.gender = gender
        self.total = total
        self.per = per	
    def showData(self):	
        print("Id :",self.id)
        print("Name :", self.name)
        print("Gender :", self.gender)
        print("Total :", self.total)
        print("Percentage :", self.per)
s = Student()
s.setData(1,'Sam Kumar','Male',422,84.44)
s.showData()
