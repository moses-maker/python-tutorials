occurrence_of_words = {}
total_words = 0
with open("quotes.txt") as file_handler:
    for each_row in file_handler:
        words = each_row.rstrip().split() # splits rows into list
        total_words += len(words)

        for each_word in words:
            occurrence_of_words[each_word] = occurrence_of_words.get(each_word, 0) + 1
        
    print("The number of times each word appears in a sentences is", occurrence_of_words)
    print("Total number of words in the file are", total_words)        
