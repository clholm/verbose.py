from lxml import html, etree
import requests


# functions


def build_dictionary_stopwords(string, word_dictionary):
    """ turns a string into individual, all lowercase words and places
     them into a dictionary to count them. Includes stopwords"""

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


def build_dictionary_no_stopwords(string, word_dictionary):
    """ turns a string into individual, all lowercase words and places
    them into a dictionary to count them. Doesn't include stopwords"""

    append_string = ""
    j = 0

    # set that includes every english stopword as defined by NLTK
    stopwords = set(["i", "me", "my", "myself", "we", "our",
                    "ours", "ourselves", "you", "your", "yours",
                    "yourself", "yourselves", "he", "him", "his",
                    "himself", "she", "her", "hers", "herself",
                    "it", "its", "itself", "they", "them",
                    "their", "theirs", "themselves", "what",
                    "which", "who", "whom", "this", "that",
                    "these", "those", "am", "is", "are",
                    "was", "were", "be", "been", "being",
                    "have", "has", "had", "having", "do",
                    "does", "did", "doing", "a", "an",
                    "the", "and", "but", "if", "or",
                    "because", "as", "until", "while", "of",
                    "at", "by", "for", "with", "about",
                    "against", "between", "into", "through", "during",
                    "before", "after", "above", "below", "to",
                    "from", "up", "down", "in", "out",
                    "on", "off", "over", "under", "again",
                    "further", "then", "once", "here", "there",
                    "when", "where", "why", "how", "all",
                    "any", "both", "each", "few", "more",
                    "most", "other", "some", "such", "no",
                    "nor", "not", "only", "own", "same",
                    "so", "than", "too", "very", "s",
                    "t", "can", "will", "just",
                    "don", "should", "now"])

    for i in range (len(string)):

        if string[i].isalnum():
            append_string = append_string + string[i].lower()
        else:
            if append_string != "":
                # if append_string isn't a stopword, add it to word_dictionary
                if append_string not in stopwords:
                    if append_string in word_dictionary:
                        word_dictionary[append_string] += 1
                    else:
                        word_dictionary[append_string] = 1
                append_string = ""

    return (word_dictionary)


# driver function that pulls data from the website, calls the build dictionary
# function, and retrieves the most frequently used words
def verbose_counter(website, number_of_words,
                    duplicates_allowed=True,
                    stopwords_allowed=False):
    """ returns a list of a website's most frequently used words.

    keyword args:
    website -- the website url
    number_of_words -- the number of frequently used words to return
    duplicates_allowed -- if there is a tie for the last word to return,
    allowing duplicates will return every word that is tied, and not
    allowing duplicates will break the tie in alphabetic order
    (default True)
    stopwords_allowed -- whether or not stopwords are allowed in the
    final list. Uses English stopwords from the NLTK. (default False) """

    # retrieve html from website (5s timeout) and make tree
    r = requests.get(website, timeout=5)
    tree = html.fromstring(r.content)
    tags = tree.xpath('//body')

    # if there is text content in the body of the page, save it to the 
    # 'text' string. otherwise make text blank
    if tags:
        body = tags[0]
        text = body.text_content()
    else:
        text = ""
    
    # intialize the word dictionary and call one of the build_dictionary 
    # functions
    word_dictionary = dict()

    if stopwords_allowed:
        build_dictionary_stopwords(text, word_dictionary)
    else:
        build_dictionary_no_stopwords(text, word_dictionary)

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
