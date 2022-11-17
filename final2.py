


###############. Problem Statement ###############
# Create a word cloud made up of different sized words which is based on how many times the word appear in a specific text.



####breaking down the problem statement and writing the solution function
#0 save the open in a dictionary
#1 open a text file and print the contents
#2 remove puntuations
#3 remove uniteresting words
#4 count the frequencies of each word
#5 testing the code to ensure all aspects has been covered


#############final working code###############
import string

def calculate_frequencies(file_contents):

    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    frequency_words = {} #dictionary to store the words which is the expected output
    
    #file_contents = open('demo.txt','r').read()  # Asinput file already passed

    if file_contents.isalpha() == False: #check if the words contain puntuation marks
        processed_words = file_contents.translate(str.maketrans('', '', string.punctuation)) #remove puntuation marks
        split_processed_words = processed_words.split() #split processed words
    for word in split_processed_words: #filtering uniteresting words out using a for loop.
        if word not in uninteresting_words:
            if word not in frequency_words: #counting the no of times each word appear and storing it as the value for the keys in the dictionary
                frequency_words[word] = 1
            else:
                frequency_words[word] += 1
    #return frequency_words #outputing the frequency_words dictionary #commenting this out as it was preventing the wordcloud module below from working.
    
    
        #wordcloud 
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequency_words)
    return cloud.to_array()


#calculate_frequencies(file_contents) #testing the function before integrating into the wordcloud module.