#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])


#Conducting stopword removal. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {"I", "and", "She", "her", "They", "their"}

for document in documents:
    index = documents.index(document)
    documents[index] = document.split(" ")

for document in documents:
    for word in document:
        if word in stopWords:
            document.remove(word)



#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {'loves': 'love','cats': 'cat', 'dogs': 'dog'}

for document in documents:
    for word in document:
        index = document.index(word)
        if word in stemming.keys():
            word = stemming[word]
        document[index] = word


#Identifying the index terms.
#--> add your Python code here
terms = []
for document in documents:
    for word in document:
        if word not in terms:
            terms.append(word)



#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []
for document in documents:
    #print(document)
    docRow = []
    for term in terms:
        tf = document.count(term) / len(document)
        df = sum(1 for doc in documents if term in doc)
        idf = math.log10(len(documents) / df)
        tfidf = tf * idf
        docRow.append(tfidf)
    docTermMatrix.append(docRow)

#Printing the document-term matrix.
#--> add your Python code here
headers = ["Love", "Cat", "Dog"]
print("Doc Term Matrix", headers)
counter = 0
for row in docTermMatrix:
    counter += 1
    row.insert(0, f"Document {counter}")
    for item in row:
        if isinstance(item,str):
            print(f"{item}\t", end="")
        else:
            print(f"{item:.4f}\t", end="")
    print()