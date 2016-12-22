from verbose import verbose_counter

# retrieve the 5 most frequently used words from this wikipedia article.
# default settings: duplicates allowed and no stopwords
# returns 7 words as of 12/2016
array = verbose_counter("https://en.wikipedia.org/wiki/Free_Throw_(band)", 5)
print("default settings:\n")
print(array)


# retrieve the 5 most frequently used words from the same wikipedia article,
# settings: duplicates allowed and stopwords allowed
# returns 6 words as of 12/2016
array = verbose_counter("https://en.wikipedia.org/wiki/Free_Throw_(band)", 
                         5, stopwords_allowed=True)
print("\nduplicates allowed and stopwords allowed:\n")
print(array)

# retrieve the 5 most frequently used words from the same wikipedia article,
# settings: duplicates not allowed and no stopwords
# will always return 5 words
array = verbose_counter("https://en.wikipedia.org/wiki/Free_Throw_(band)",
                         5, duplicates_allowed=False)
print("\nduplicates not allowed and no stopwords:\n")
print(array)

# retrieve the 5 most frequently used words from the same wikipedia article,
# settings: duplicates not allowed and stopwords allowed
# will always return 5 words
array = verbose_counter("https://en.wikipedia.org/wiki/Free_Throw_(band)",
                         5, duplicates_allowed=False, stopwords_allowed=True)
print("\nduplicates not allowed and stopwords allowed:\n")
print(array)