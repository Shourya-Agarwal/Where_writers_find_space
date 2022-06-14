import nltk
import string
nltk.download('stopwords')
from nltk.corpus import stopwords
s=stopwords.words('english')
keyword=[]
def filter(data):

    # convert everything in lower case
    data=data.lower()
    # delete all punctutations 
    data=data.translate(str.maketrans('','',string.punctuation))
    print(data)
    words=data.split(" ")

    # remove all stopwords
    for i in words:
        if i not in keyword and i not in s:
            keyword.append(i)
    return keyword

