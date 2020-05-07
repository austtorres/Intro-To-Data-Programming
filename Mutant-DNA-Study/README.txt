Program Skills
Practice converting between lists and strings
Practice with counter-controlled loops
Exploring (intentional!) Python error creation

Summary
You are a scientist working in the laboratory with Professor X on the DNA sequences of mutants. You are observing key genes in the DNA sequences to find how similar/dissimilar they are. If the two sequences of DNA are same, the two mutant species are considered to be closer to each other.

Consider the two strings of DNA below (mismatches in red):

Species 1: AATAACGAAA

Species 2: AAAACGAAAA

You have been advised by Professor X to try insertion or deletion of one of the bases to change alignment. You are observing the alignment of DNA sequences and making changes to the sequences to see if the alignment improves. Such a change is called an indel (represented by -)

Species 1: AATAACGAAA-

Species 2: AA-AACGAAAA

Assuming two indels, marked as two dashes (-), the alignment is greatly improved. We can then assume that only two mutations occurred, one change in each species.

Your task is to write the program below and help researchers in studying DNA sequence alignment.

Program Requirements
For this assignment, you will write at least four (4) functions with the following names and behaviors (Please ensure that the names match EXACTLY as is):

is_valid_sequence(seq) – this helper function takes in a DNA sequence as a string and returns True if and only if its characters are acceptable DNA bases; if it contains invalid characters, it should raise a ValueError instead of returning False (see below for details).
add_indel(seq, pos) – takes in a sequence as a string and an index in the string to add an indel ("-"), and returns the modified sequence as a string. Raises an IndexError if the position is out of bounds (see below for details).
delete_indel(seq, pos) – takes in a sequence as a string and an index in the string to remove an indel ("-"), and returns the modified sequence as a string. Raises a ValueError if there is not an indel at the specified position, or an IndexError if the position is out of bounds (see below for details).
align_sequences(seq1, seq2) – takes in two sequences as strings, adds indels to the end of the shorter one until they are of equal length, and prints the matches and mismatches. (No return value.)
Be careful to match these names and behaviors exactly. You may implement additional helper functions if you like, but you must have the specified functions.

Side Note: Converting from strings to lists and back again
As you know, strings are immutable (cannot be changed) and lists are mutable (can be changed, added to, removed from, etc). You may want the mutability of a list in many of these functions! Remember that you can use the list type conversion function to convert a string to a list:

>>> list("parrot")
=> ['p', 'a', 'r', 'r', 'o', 't']
But if you try to use the string type conversion function to get back to a string, you'll notice you get a bunch of extra characters:

>>> str(["p", "a", "r", "r", "o", "t"])
=> "['p', 'a', 'r', 'r', 'o', 't']"
What you can do instead is use the str.join() function as follows, which joins every character in your list with the empty string ("") and then the next character in the list, until you get a normal string again!

>>> "".join(["p", "a", "r", "r", "o", "t"])
=> 'parrot'
You're also welcome to use string slicing and concatenation if you want to, but I definitely found it easier to use str.join().

1. Is valid sequence
None of your functions should assume that the sequences provided are valid DNA sequences, so this function will help you verify your sequences.

If you find a character in the sequence which is not A, C, G, T, or - (only capital letters allowed), you should create (in Python terminlogy, "raise") a ValueError:

raise ValueError("This is the message that will be displayed if this happens")
Yes, this will crash your program! But as you've seen so far this semester, sometimes it's good to have an error happen, so you know to fix your code.

When you raise the ValueError, your error message should display the first invalid character and the message " is not a valid DNA character!" See the sample output below for what this will look like.

If all of the characters are valid, your function should return True. Note: this means there are no cases in which it returns False!

>>> is_valid_sequence("aabbbcccc")
Traceback (most recent call last):
  [a stack trace that will be unique to your implementation]
ValueError: a is not a valid DNA character!
>>> is_valid_sequence("AAAUGH")
Traceback (most recent call last):
  [a stack trace that will be unique to your implementation]
ValueError: U is not a valid DNA character!
>>> is_valid_sequence("AA-CCGGTT")
=> True
2. Add indel
This function takes a DNA sequence as a string and the index at which you want to place the indel and returns the string after indel addition with a dash(-) added. Placement of the indel is at the given index. So, for example, if you give 2 as an input index, the indel will be placed before the character at index 2 in the string.

The ValueError from the previous function should be raised if the sequence contains invalid characters. If all characters are valid but the index provided is out of range, an IndexError should be raised (with the message "Index [invalid index] is out of range!").

>>> add_indel("aabbbcccc", 2)
Traceback (most recent call last):
  [a stack trace that will be unique to your implementation]
ValueError: a is not a valid DNA character!
>>> add_indel("AACCCGGGG", 2)
=> 'AA-CCCGGGG'
>>> add_indel("AACCCGGGG", 9)
=> 'AACCCGGGG-'
>>> add_indel("AACCCGGGG", 10)
Traceback (most recent call last):
  [a stack trace that will be unique to your implementation]
IndexError: Index 10 is out of range!
3. Delete indel
This function takes a DNA sequence and the index to delete the indel and returns the string after indel deletion.

The ValueError from the first function should be raised if the sequence contains invalid characters. As in the previous function, if all characters are valid but the index is out of range, an IndexError should be raised (same error message). If all characters are valid but there is no indel at the provided valid index (i.e. it is any other character), a ValueError should be raised (with the message "No indel at index [index]!").

>>> delete_indel("AA-CCCGGGG", 2)
=> 'AACCCGGGG'
>>> delete_indel("AA-CCCGGGG", 9)
Traceback (most recent call last):
  [a stack trace that will be unique to your implementation]
ValueError: No indel at index 9!
>>> delete_indel("AA-CCCGGGG", 10)
Traceback (most recent call last):
  [a stack trace that will be unique to your implementation]
IndexError: Index 10 is out of range!
4. Match sequences
This function will report the number of matches and the number of mismatches between the two DNA sequences.

If either string contains invalid characters, the ValueError from the first function should be raised and the program should crash.
If one string is shorter than the other, add indels to the end of the shorter string until they are the same length.
Any indel is automatically a mismatch.
After you count matches and mismatches, print both strings:
Matching characters are printed in lower case.
Mismatched characters are printed in upper case.
Indels are printed as dashes ("-").
Note that this function does not return any value, so it is critical that you match the printed output format EXACTLY.

>>> align_sequences("AATAACGAAA", "AAAACGAAAA")
Matches: 6
Mismatches: 4
Str1: aaTaACGaaa
Str2: aaAaCGAaaa
>>> align_sequences("AATAACGAAA", "AA-AACGAAAA")
Matches: 9
Mismatches: 2
Str1: aaTaacgaaa-
Str2: aa-aacgaaaA
