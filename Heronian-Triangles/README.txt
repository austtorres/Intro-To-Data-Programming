Program Skills
Creating and calling functions
Calling functions from other functions
Basic conditional statements

Summary
Heron of Alexandria is attributed with a super neat formula (Links to an external site.) for calculating the area of a triangle given all three side lengths and nothing else. (There's a mathematical proof at that Wikipedia link of how/why it works, if you're interested.)

A Heronian Triangle is one where all of the side lengths and the area of the triangle are all integers. We're going to write a few functions to determine whether a given triangle is Heronian.

Program Requirements
For this assignment, you will write two (2) functions with the following names and behaviors:

area(a, b, c) – Implements Heron's formula. Expects three (3) side lengths, and returns the calculated area of the triangle.
is_heronian(a, b, c) – Checks whether a given triangle is Heronian (all sides are integers and area is an integer). Expects three (3) side lengths, and returns True if the triangle is Heronian and False otherwise.
Be careful to match these names and behaviors exactly. You may implement additional helper functions if you like, but you must have the specified functions.

1. Area calculation
Heron's formula for the area of a triangle is defined as follows:

LaTeX: A\:=\:\sqrt{s\left(s-a\right)\left(s-b\right)\left(s-c\right)}A = s ( s − a ) ( s − b ) ( s − c )

Where s is the "semi-perimeter", or

LaTeX: s\:=\:\frac{a+b+c}{2}s = a + b + c 2

Your area function should expect the three values a, b, and c as parameters (variables in the function header), and return the calculated area.

Here are some examples you can use to test your function, where the bold, blue text is a function call in the console, and the bold, green text preceded by => is the return value from your function:

>>> area(2,3,4)
=> 2.90473750966
>>> area(3,4,5)
=> 6.0
>>> area(5,12,13)
=> 30.0
You may find it helpful to implement a helper function to calculate s given a, b, and c, but this is not required.

2. Heronian??
In this function, we'll use the function you just wrote to calculate a triangle's area, as well as using a basic conditional statement to test the state of our program.

A Heronian triangle is one where all of the side and area values are integers. Your function should check that all sides are integers, and that the area is an integer, and return True if and only if they are ALL integers.

The syntax for a basic conditional statement is as follows:

if condition:
    code that runs when condition is True
So for example:

if x%2 == 0:
    return "even"
if x%2 == 1:
    return "odd"
There are a couple of different strategies you can employ to test whether numbers are integers:

type(x) – the type() function will tell you what type of value is contained in a variable. If type(x) == int, you know you have an integer. CAREFUL: type(2.0) is not int!
int(x) – the int() function returns an integer version of a value or a variable.
As a hint for using the second function, note that 2 == 2.0 is True.

>>> is_heronian(2,3,4)
=> False
>>> is_heronian(3,4,5)
=> True
>>> is_heronian(5.0,12,13)
=> True
