import string

try:
    fname = open("Macbeth.txt")

    print(fname)


    fill_in_words = ["and", "or", "i", "the", "a", "an", "but", "however", "thou", "tis", "thee","of","yet","did", "shall", ]
   
    counts = dict()

    for line in fname:
        line = line.rstrip().translate(line.maketrans("", "", string.punctuation))
        line = line.lower()
        words = line.split()

        for word in words:
            if word not in fill_in_words:
                if word not in counts:
                    counts[word] = 1
                else:

                    counts[word] += 1
        
        for word in fill_in_words:
            if word in counts:
                del counts[word]


    
    #print(counts)
    sorted_dictionary = dict(sorted(counts.items()), key=lambda item: item[1])
    print(sorted_dictionary)




except Exception as e:
    print(e)
    exit()


