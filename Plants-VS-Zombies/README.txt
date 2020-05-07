Program Skills
Practice with conditionals
Random numbers
Basic for loops

Summary
Time to save the world from Zombies and guess who is here to save the day: For Loops!! Oh well, I meant Plants.

In the war against Plants and Zombies we have three plant heroes:

Fire Cactus (p)
Fume Shroom (q)
Mystic Petal (r)
Zombie armies are lead by:

Crime Slime (x)
Cone Head (y)
Imp Monk (z)
You need to write a program that will decide who will win the war to save the human race between the plant heroes and the zombie armies. You need to calculate the total strength of the plant powers and the zombie powers, compare them and declare the winner!!

Program Requirements
For this assignment, you will write at least three (3) functions with the following names and behaviors (Please ensure that the names match EXACTLY as is):

plant_power(heroes) – takes in the unique combination of plant heroes and returns their total calculated strength as an integer.
zombie_power(villains) – takes in the unique combination of zombie villains and returns their total calculated strength as an integer.
war_begins(hero, villain, seed) – this function seeds our random number generator (more on that below), calls the other two functions, compares the values of the two returned strengths, and prints a message declaring the Winner. This will be the main function that tests your final results.
Be careful to match these names and behaviors exactly. You may implement additional helper functions if you like, but you must have the specified functions.

1. Plant power
This function takes in the string value that indicates the combination of plant heroes involved. For example “pqpqr” indicates that the heroes have the combined power of Fire Cactus (twice), Fume Shroom (twice) and Mystic Petal.

To begin, randomly generate an integer power level between 1-10 for Fire Cactus (p), then for Fume Shroom (q), then for Mystic Petal (r). It's crucial that you do that in this order, for testing purposes!

When testing this function, try setting Python's random number generator's seed value. This will guarantee that random will generate the same sequence of numbers every time. For example, if you set the seed to 0, you will get p = 9, q = 8, and then r = 5:

>>> random.seed(0)
>>> plant_power('pqpqr') 
# note: printed output here is for debugging
# and should not appear in your final program
# which should just return an integer.
p power: 9
q power: 8
r power: 5
But here is the twist!!!! What is fun if you just do the summation of direct power values. We want you to use loops to calculate the summation of factorials of individual powers.

So now, the value of “pqpqr” will be LaTeX: 9!+8!+9!+8!+5! =8065209 ! + 8 ! + 9 ! + 8 ! + 5 ! = 806520

NOTE: Factorial is the positive, non-zero product of an integer with all the integers lesser than itself.

For example, the factorial of 4 represented as LaTeX: 4! = 4\times 3\times 2\times 1 = 244 ! = 4 × 3 × 2 × 1 = 24, the factorial of 5 is LaTeX: 5! = 5\times 4\times 3\times 2\times 1 = 1205 ! = 5 × 4 × 3 × 2 × 1 = 120, and so on.

(Do not use the python’s built-in math.factorial() function in your code if you want full credit. Our graders will test for the usage of such functions in your code. Additionally, this is the one time we do not permit defining a helper function, since Hobbes solved this with a recursive function in class. Use a loop!!)

>>> random.seed(0)
>>> plant_power('pqpqr')
=> 806520
Note that every time you set the seed back to 0 and generate three random numbers 1-10, you'll get 9, then 8, and then 5! This is why seeded random number generators are great for testing your code.

2. Zombie power
This function is almost exactly the same as plant_power(heroes). It also takes in the string value that indicates the combination of zombie villains involved, except these zombies are Crime Slime (x), Cone Head (y) and Imp Monk (z).

Again you should begin by generating a power level 1-10 for the zombies in that order. Because of how the random number generator's seed works, if we were to set the seed to 0 again, we would get the SAME values as before: x = 9, y = 8, and z = 5.

>>> random.seed(0)
>>> zombie_power('xyz') 
# note: printed output here is for debugging
# and should not appear in your final program
# which should just return the integer.
x power: 9
y power: 8
z power: 5
Again we want you to use loops to calculate the summation of factorials of individual powers, and then return the result.

>>> random.seed(0)
>>> zombie_power('xyz')
=> 403320
3. The war begins!
This function seeds the random number generator ONCE with the provided seed, passes its hero parameter to plant_power(), and then its villain parameter to zombies_power(), compares the total returned strength of each function and declares the team with the greater value as the winner.

If the plants' combined power is higher, please print "Plants save the day!"

If the zombies' combined power is higher, please print "Zombies are here to stay!"

If the plants and zombies combined power somehow ends up being equal, please print "IT'S A DRAW!" in all-caps.

(I cannot stress enough to EXACTLY print the same sentences, with the same punctuation and capitalization (but not the quotes around the strings, see the example below), to aid auto-grading and get a perfect score.)

>>> war_begins('pqr', 'xyz', 0)
# debugging, remove: plants = 403320
# debugging, remove: zombies = 846
Plants save the day!
Other Notes
Both heroes and zombies should have randomly-generated power levels between 1-10. It is critical that you generate these numbers in the order specified so we can test your code.

You may assume that the input strings for plant_power() and zombie_power() will contain at most six (6) characters, but may not be the same lengths. You may NOT assume that they will be only the valid characters for that function – the zombies might try to cheat, after all! Only do your calculations on the valid characters.
