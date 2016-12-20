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
def verbose_counter(website, number_of_words, duplicates_allowed = True): 

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

    # sort list in descending order of frequency first 
    # and then alphabetically
    repeated_list.sort(key=lambda x: (-x[0], x[1]))

    i = 0
    frequent_words = [] 

    if repeated_list != []: 
             
        if duplicates_allowed: 
            while i < number_of_words:

                # if this is the last word to append to the list, 
                # check to see if there are multiple words with the same 
                # frequency
                if i < len(repeated_list): 
                    if i == number_of_words - 1:
                        # initialize variable j 
                        j = i
                        while j < len(repeated_list): 
                            # if the word has the same frequency, append it to
                            # frequent_words, otherwise break
                            if (repeated_list[i][0] == repeated_list[j][0]): 
                                frequent_words.append(repeated_list[j][1])
                            else: 
                                break

                            j += 1
                    else: 
                        frequent_words.append(repeated_list[i][1])
                else: 
                    break 

                i += 1
        else: 
            while i < number_of_words:

                if i < len(repeated_list):
                    frequent_words.append(repeated_list[i][1])

                i += 1 

    return frequent_words

