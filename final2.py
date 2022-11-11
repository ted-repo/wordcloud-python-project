
#checking if all seems as is

# create a word cloud
#made up of different sized words which is based on how many times the word appear in a specific text

#create a script that would go through a text and count how many times each word appears 
#use a dic

#ensure there are no punctuation marks in the word being counted. therefore cleanup the text before putting words in the dictionary

#keep the word cloud interesting and don't include uninteresting words such as uh, the, er... Ignore words that are not relevent to the overal message.
#there exclude irrelevant words when processing the text

#upload a text file for the input. choose a text file.

###### rewatch the final project overview if something isn't clear. ###### 

##1. understand the problem statement
#A script that concatenates relevant words together. The more no of times these words appear the bigger they are.

#2. research available options

#### this is the order I have decided to solve this problem :)


### - need a filter string method (to remove punctuation marks, spaces, irrelevant words etc.) ---1

#could use the isalpha() method to chewck if a text has puntuation marks
string = "This is a boy, he has a pet!"
string.isalpha()

#removing punctuation marks from the text.
import string

#print(string.punctuation) #checking the punctuation marks present

    
string_text = "This is a boy, he has a pet!"  
processed_string_text = string_text.translate(str.maketrans('', '', string.punctuation))
print(processed_string_text)

#spliting the processed text with space
processed_string_text.split()

#remove uninteresting words before storing them into the dictionary
    #i can reference the previous example code for tips on this section as we would be sotring the date
    #in a dictionary of sets







#3. write the code to create an interesting dictionary
#3.1 first iteration of the script receives a text input and remove some uninteresting words
# and returns the result.


#words = open('demo2.txt','r').read() #pass the input file


import string

def calculate_frequencies(words):
    frequency_words = {} #dictionary to store the words
    words = open('words','r').read() #pass the input file
    if words.isalpha() == False: #check if the words contain puntuation marks
        processed_words = words.translate(str.maketrans('', '', string.punctuation)) #remove puntuation marks
        split_processed_words = processed_words.split() #split processed words.
        for word in split_processed_words: #iterate through each word
            frequency_words[word] = set()
            if word == "a":
                frequency_words[word].remove(word) #remove uniteresting words
        return frequency_words #return all words that make the interesting dict.

#need to figure out a way to get output from the script above?
calculate_frequencies(demo2.txt)

#3.2 iteration 2: the script needs to be able to count the frequencies of the word.

#4. execute it



