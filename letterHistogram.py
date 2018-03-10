
def letter_histogram(str):
    tally_dict = {}
    for char in str:
        if tally_dict.get(char):
            tally_dict[char] += 1
        else: 
            tally_dict[char] = 1
    print tally_dict        
    
letter_histogram('Brendon')