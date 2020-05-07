Program Skills
Basic dictionaries
Practice with for loops and files

Summary
In this program you will do some basic text analysis on English text files, using the Python dictionary data structure to track your information.

Program Requirements
For this assignment, you will write at least five (5) functions with the following names and behaviors (Please ensure that the names match EXACTLY as is):

get_alphanum(text) – transforms the argument text string to lowercase, removes all non-alphanumeric characters (letters or numbers), and returns the resulting string.
remove_stopwords(word_list, stopwords) – removes all words in the stopwords list from the word list in place. This function does not return a value.
get_word_freq(word_list) – creates and returns a dictionary of frequencies of words in the word list, with the words as keys and the frequencies as values.
get_keywords_threshold(word_freq, threshold) – creates and returns a dictionary of words and their frequencies from the provided word_freq dictionary, where all frequencies are over the given threshold.
get_top_keywords(word_freq, n) – creates and returns a dictionary of the top n keywords in the provided word_freq dictionary.
Be careful to match these names and behaviors exactly. You may implement additional helper functions if you like, but you must have the specified functions.

Provided Functions
We'll be using files again this week to keep things interesting, so to get you started, here are the files:

Stop words: english.txtPreview the document
English text document: pride_and_prejudice.txtPreview the document
You can get other large text documents from Project Gutenberg (Links to an external site.), if you'd like to test your code on other books.

To read in the stop words file:

def get_stopwords(filename):
    with open(filename, 'r') as f:
        return [word[:-1].replace("'","") for word in f]
To read in the text document and return a list of words for you to remove those stop words from, and then parse into a dictionary later:

def get_text(filename):
    with open(filename, 'r') as f:
        return get_alphanum(f.read()).split() # USES YOUR FUNCTION
Note that this second function uses one of your functions, get_alphanum(text). You'll want to implement that next.

1. Get alphanumeric characters
Returns the input text in lowercase, preserving only alphanumeric characters (letters or numbers) and whitespace.

>>> get_alphanum("Posting Date: August 26, 2008 [EBook #1342]")
=> 'posting date august 26 2008 ebook 1342'
>>> get_alphanum('"_You_ want to tell me, and I have no objection to hearing it."')
=> 'you want to tell me and i have no objection to hearing it'
>>> get_alphanum("You can't tell me what to do!")
=> 'you cant tell me what to do'
If you'd like to see what the get_text() function from above is doing, you can use this function to read in the entirety of a document as a single string, which you can then pass to get_alphanum():

def get_textstring(filename):
    with open(filename, 'r') as f:
        return f.read()
2. Remove stopwords
Removes all words in the input word list that appear in the provided stop words list in place. This function does not return a value.

>>> words = ['you', 'want', 'to', 'tell', 'me', 'and', 'i', 'have', 'no', 'objection', 'to', 'hearing', 'it']
>>> stopwords = get_stopwords('english.txt')
>>> remove_stopwords(words, stopwords)  # note: no return value
>>> print words
['want', 'tell', 'objection', 'hearing']
3. Get word frequency dictionary
Creates and returns a dictionary where the keys are the words from the word list, and the values are the number of times each word appears in the word list.

>>> get_word_freq(["hello", "world", "world", "there", "hello", "world"])
=> {'hello': 2, 'there': 1, 'world': 3}
4. Get keywords over a threshold
Creates and returns a dictionary of the words from the provided word_freq dictionary where their frequency exceeds the provided threshold.

>>> get_keywords_threshold({'hello': 2, 'there': 1, 'world': 3}, 1)
=> {'hello': 2, 'world': 3}
5. Get top N keywords
Creates and returns a dictionary of the top N most frequently occurring words from the provided word_freq dictionary. If you want, you may use the sorted() function as in P6. You may choose how to resolve any ties that occur.

>>> get_top_keywords({'hello': 20, 'there': 13, 'world': 300, 'fruit': 500, 'flower': 3, 'pen': 50, 'apple': 100}, 4)
=> {'apple': 100, 'fruit': 500, 'pen': 50, 'world': 300}
