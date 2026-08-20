import string
# allowing thonny to connect to the bridges server and ccess BRIDGES Shakespeare data source
from bridges.bridges import Bridges
from bridges.data_src_dependent.data_source import get_shakespeare_data

# my BRIDGES credentials
bridges = Bridges(5, "howardwilliams108", "1628069107419")

# 


# this retrieve Shakespeare's works from database
works = get_shakespeare_data()

# Select one story from Shakespeare's works
story = works[0]

print("Title:", story.title)
print()

# Get the text
text = story.text

# Remove punctuation using string.punctuation and ensuring words aren't counted differently
text = text.lower()
#It's used the O(n) time complexity

for ch in string.punctuation:
    text = text.replace(ch, " ")

# Splitting words
words = text.split()


frequency = {} #creating an empty dictionary

# this is the recursive function which involves O(n)
# as each word would be processed exactly once.
def count_words(words, index, freq):

    
    if index == len(words):
        
        return

    word = words[index]

    if word in freq: # this checks wheth dictionary already contains the word
        freq[word] += 1 #time complexity: O(1)
    else:
        freq[word] = 1

    
    count_words(words, index + 1, freq)


count_words(words, 0, frequency)

# This would sort the  frequency dictionary
sorted_words = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

print("Top 40 Words")
print("^" * 40)

for word, count in sorted_words[:40]:
    #looping through the first 40 items in the specific list
    print(word, ":", count)
    
    