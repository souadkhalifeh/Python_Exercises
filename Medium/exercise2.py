# Exrecise 2
# Build a simple text analyzer. 
# Problem: Write a function count_words(text) that:

# Accepts a paragraph of text
# Returns a dictionary where keys are words 
# and values are how many times they appeared (case-insensitive)
# Example input: | text = "AI is the future. The future is now."

# Expected Output: {'ai': 1, 'is': 2, 'the': 2, 'future': 2, 'now.': 1}
import string

def text_analyzer(text):
    text=text.lower()
    
    for punct in string.punctuation:
        text = text.replace(punct, "")
    words=text.split()
    word_count={}
     
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word] = 1
            
    return word_count
    
text = "AI is the future. The future is now."
print(text_analyzer(text))            

