mywords = {}
total_words = 0
with open("countries.txt") as file_reader:
    for each_row in file_reader:
        words = each_row.split() # create separate list for each row.
        total_words += len(words)
        print(words)

    print("The file has",total_words, "words")

    for each_word in words:
            mywords[each_word] = mywords.get(each_word, 0) + 1

    print("The number of times each word appears in a sentences is",mywords)
    print("Total number of words in the file are", total_words)   


