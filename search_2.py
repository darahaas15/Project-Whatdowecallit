import re
import string
from nltk.corpus import stopwords
from nltk import word_tokenize

stopWords = set(stopwords.words('english'))
search_string = input("Enter the string: \n")
print("original string : " + search_string)
res_set = re.sub('[' + string.punctuation + ']', '', search_string).split()
print("words : " + str(res_set))
res_str = ' '.join(res_set)
print("resultant string : " + str(res_str))
words = word_tokenize(res_str)
print(words)
articlesFiltered = ['A', 'a', 'an', 'An', 'the', 'The']
for w in words:
    if w in articlesFiltered:
        words.remove(w)

print(words)


def dtob(n):
    b = 0
    i = 1
    while (n != 0):
        r = n % 2
        b += r * i
        n //= 2
        i = i * 10
    return b


def createList(k):
    a = []
    if (k == 0):
        a.append(0)

    while (k > 0):
        a.append(k % 10)
        k //= 10
    a.reverse()
    return a


def checkb(bin, l):
    tempo = []
    for i in range(len(bin)):
        if (bin[i] == 1):
            tempo.append(l[i])
    return tempo


l = words

binlist = []
subsets = []

n = len(l)

for i in range(2 ** n):

    s = dtob(i)

    arr = createList(s)

    binlist.append(arr)

    for i in binlist:

        k = 0

        while (len(i) != n):
            i.insert(k, 0)
            k = k + 1

for i in binlist:
    subsets.append(checkb(i, l))
subsets.remove([])

print(subsets)


