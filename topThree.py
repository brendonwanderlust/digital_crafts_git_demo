
def word_histogram(sentence):
    tally = {}
    wordsList = sentence.split()
    for word in wordsList:
        if tally.get(word):
            tally[word] += 1
        else: 
            tally[word] = 1
    
    def 
    print tally        


def top_three(tally):
     = sorted()
    
word_histogram('Brendon, it is what it is')  