# Task 1

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

keywords = ['good', 'excellent', "bad", "poor", "average"]

for change in python_reviews:
    for word in keywords:
        if word in change:
            change = change.replace(word, word.upper())
    print(change)

# # Task 2

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def counting_pos_and_negs():
    positive_counts = 0
    negative_counts = 0
    for output in python_reviews:
        for words in positive_words:
            if words in output:
                positive_counts += 1
        for words in negative_words:
                if words in output:
                     negative_counts += 1
                    
    print(f"Positive word count: {positive_counts} \nNegative word count: {negative_counts}.\n")

counting_pos_and_negs()


# Task 3

def summary():
    for reviews in python_reviews:
        short_end = reviews[0:30]
        
        print(short_end + "...")

print('Product review summarys:\n')

summary()

                              
           


