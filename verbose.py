from lxml import html, etree
import requests

# functions

# turns a string into individual, all lowercase words and places 
# them into a dictionary to count them
def build_dictionary(string): 
    word_dictionary = dict()
    j = 0

    for i in range (len(string)):

        if (string[i].isalnum()) is False:
            append_it = string[j:i].lower()
            if append_it != "": 

                if append_it in word_dictionary: 
                    word_dictionary[append_it] += 1
                else: 
                    word_dictionary[append_it] = 1
                
            j = i + 1

    append_it = string[j:].lower()

    if append_it != "": 
        if append_it in word_dictionary: 
            word_dictionary[append_it] += 1
        else: 
            word_dictionary[append_it] = 1

    return (word_dictionary)

# driver function that pulls data from the website, calls the build dictionary
# function, and retrieves the most frequently used words
def verbose_counter(website, number_of_words): 

    # get the website
    r = requests.get(website, timeout = 5)
    tree = html.fromstring(r.content)
    tags = tree.xpath('//body')

    if tags: 
        body = tags[0]
        text = body.text_content()
    else: 
        text = '' 

    # call the build_dictionary function
    word_dictionary = build_dictionary(text)

    repeatedList = []

    # loop through the dictionary 
    for key, value in word_dictionary.items(): 
        repeatedList.append([value, key]) 

    repeatedList.sort(reverse=True)

    i = 0
    frequent_words = [] 

    if repeatedList != []:
        while i < number_of_words:
            frequent_words.append(repeatedList[i][1])
            i += 1 

    return frequent_words

