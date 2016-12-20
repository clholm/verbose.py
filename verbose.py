from lxml import html, etree
import requests

# functions

# turns a string into individual, all lowercase words and places 
# them into a dictionary to count them
def build_dictionary(string): 
    word_dictionary = dict()
    append_string = ""
    j = 0

    for i in range (len(string)):

        if string[i].isalnum(): 
            append_string = append_string + string[i].lower()
        else: 
            if append_string != "": 
                
                if append_string in word_dictionary: 
                    word_dictionary[append_string] += 1
                else: 
                    word_dictionary[append_string] = 1

                append_string = ""

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

    repeated_list = []

    # loop through the dictionary 
    for key, value in word_dictionary.items(): 
        repeated_list.append([value, key]) 

    # sort list in descending order of frequency 
    repeated_list.sort(reverse=True)

    i = 0
    frequent_words = [] 

    if repeated_list != []:
        while i < number_of_words:
            frequent_words.append(repeated_list[i][1])
            i += 1 

    return frequent_words

