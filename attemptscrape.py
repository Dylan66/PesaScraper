#Write an application which, when given a web page will download the text on it and output a sorted list of the unique words on the page, with counts of the occurrences.
import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

page = requests.get("https://pesapal.freshteam.com/jobs/")#issues a HTTP get request


soup = BeautifulSoup(page.content, "html.parser")
#beautifulsoup object that takes all html content as input and specifies the correct parser to be used

#converts the iterable to string
text = (''.join(s.findAll(text=True))
#crawls through the website for all content in  html p tags 
for s in soup.findAll('p'))

#counter counts items from a string
#this line eliminates punctuation from the content and makes the words lower case
c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))

print ("These are the unique words" )

print(sorted(c))#prints out all the unique words in the page


print("These are the most common words",end="\n")

print(c.most_common)# prints most common words in descending order
