# verbose.py
A Python module that returns a list of the most frequently used words of a webpage
(requires lxml and requests) 

### Example: 
```
from verbose import verbose_counter

array = verbose_counter("http://clholm.com/", 2)
print(array)
``` 
array = ['connor', 'holm']

To use, simply import the module and call the verbose_counter function. 
Function parameters: 
1. Website URL
2. Number of frequent words to return
3. Whether or not duplicates are allowed in the returned list (default True). 
   Edit this in the function call with "duplicates_allowed=(True/False)"
4. Whether or not stopwords are allowed in the returned list. Uses English 
   Stopwords from the NLTK (default False). Edit this in the function call with 
   "stopwords_allowed=(True/False")

If there is a tie for the last word to return, allowing duplicates will return 
every word that is tied, and not allowing duplicates will break the tie in 
alphabetic order. 
If stopwords are not allowed, they will be omitted from the entire frequency
count, and as a result will not be in the returned list

This code is provided under the MIT License. Do whatever you want with it! 

If you have any questions, suggestions, or other comments feel free to email me at
clholm@umich.edu (or visit my website at [clholm.com](http://clholm.com/))
