Program Skills
Practice with lists
Algorithms

Summary
When students fill out the weekly surveys, they will not-infrequently misspell their own names (or their partner's name). 
For example, in our database there might be a student named “Adam” but someone types it in as “Adqm”. 
Given a name and a list of candidate names, you'll be trying to figure out the most similar names based on a distance function.

Definition of distance function, given name_A and name_B​:

If the two names have the same number of letters, the distance between name_A and name_B is their Hamming Distance (Links to an external site.).
If name_A is longer than name_B, the distance between name_A and name_B is the minimum Hamming Distance between name_B and any substring of name_A with the same length, plus the number of extra characters in name_A.
For example: “cob” and “Jacob”. Then the name_distance(“cob”, “Jacob”) = min(hamming_distance(“cob”, “Jac”), hamming_distance(“cob”, “aco”), hamming_distance(“cob”, “cob”)) + 2
If name_A is shorter than name_B, follow the same procedure as in 2 but with the names swapped.
Program Requirements
For this assignment, you will write at least three (3) functions with the following names and behaviors (Please ensure that the names match EXACTLY as is):

hamming_distance(name_A, name_B) – Calculate and return the Hamming Distance between name_A and name_B (you may assume these names have the same length).
name_distance(name_A, name_B) – Calculate and return the distance between name_A and name_B where these names may be different lengths.
name_matching(filename, target, k) – Load in a list of names from a file, compare the target name to each name, and return a list of all names within a distance of k from the target name.
Be careful to match these names and behaviors exactly. You may implement additional helper functions if you like, but you must have the specified functions.

1. Hamming distance
Hamming distance is quite simply the number of mismatches between two strings of equal length. (Think: where have you done something like this recently???)

>>> hamming_distance('David', 'Davod')
=> 1
>>> hamming_distance('Adam', 'Tddm')
=> 2
2. Name distance
If two names are the same length, their distance is their Hamming distance. Otherwise, their distance is the minimum Hamming distance between the shorter name and any substring of the longer name with that length, plus the number of extra characters left over in the longer name.

For example, "cob" and "Jacob":

Find the minimum Hamming distance between "cob" and any of "Jac", "aco", "cob"
Find the difference in length between "cob" and "Jacob"
Add those two quantities together
>>> name_distance('Jacob', 'aco')
=> 2
>>> name_distance('Frank', 'bank')
=> 2
3. Name matching
First, add this function to your code:

def get_name_lists(file_name):
    with open(file_name, 'r') as fr:
        return [name[:-1] for name in fr]
This will open up a file named file_name, read in the contents, and return the contents to you in a list.

Note: while it is possible to accomplish this in the repl.it environment, this is a great opportunity for you to try out your local Python installation, so you don't have to transfer our sample name lists to repl.it, you can just download them.

Here are some test files for you to use:

names1.txtPreview the document
names2.txtPreview the document
These files contain lists of some names beginning with A.

In this function, you are looking for all of the names in the resulting name list that are within a distance of k (not including k) of your target name. Use your other functions to get these distances, and return a list of the qualifying names.

>>> name_matching('names1.txt', 'Adam', 2)
=> ['Adam','Adams','Aram']
>>> name_matching('names2.txt', 'Adam', 2)
=> ['Ada', 'Adah']
>>> name_matching('names1.txt', 'Adpm', 2)
=> ['Adam']
>>> name_matching('names2.txt', 'Adpm', 2)
=> []
