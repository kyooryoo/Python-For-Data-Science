# Natrual Language Processing NLP compiles documents, featurizes them, and
# compares their features. Use Bag of Words and improve it by adjusting word
# counts based on their frequency in corpus (the group of all the documents)
# with TF-IDF (Term Frequency - Inverse Document Frequency).
# Term Frequency TF is the importance of the term within that document
# TD(d,t) = num of occurrences of term t in document d
# Inverse Document Frequency is the importance of the term in the corpus
# IDF(t) = log(D/t) D is total num of docs, t is num of docs with the term
# TF-IDF combines the term importance to the document and to all documents

# a collection of texts is sometimes called "corpus"

# intall nltk library if it is not installed
# we will use the stopwords file from this library
import nltk
# optionally, download the stopwords file to check its content
nltk.download_shell()
# enter d to inter download mode, or enter l to list out all files 
# enter stopwords to download the file, then enter q to quit the shell

# read sample messages and convert it to a list
file = './Documents/Workspace/Python-For-Data-Science/sample_SMSSpamCollection'
messages = [line.rstrip() for line in open(file)]

# check the number of messages and some specific message content
# notice there is a tab seperator (\t) between message class and content
print(len(messages))
messages[50]

# use enumerate method to number and print the first ten messages
# message_no is not part of the file but from the enumerate call
for message_no,message in enumerate(messages[:10]):
    print(message_no,message)
    print('\n')

# parsing this TSV tab seperated values file with pandas
import pandas as pd
messages = pd.read_csv(file,sep='\t',names=['label','message'])
# check the file is imported well with correct column names
messages.head()
messages.describe()
# check describe after groupby label to think about features engineering 
messages.groupby('label').describe()

# generate a new length features based on the understanding of the data
messages['length'] = messages['message'].apply(len)
# check the new lenght feature
messages.head()

# explore the length of messages and find some outliers
messages['length'].plot.hist(bins=50)
messages['length'].describe()
# find the longest test message in sample data
messages[messages['length'] ==  910]['message'].iloc[0]
# notice that spam messages tend to be little big longer
messages.hist(column='length',by='label',bins=40,figsize=(10,4))

# pre-process the text to normalize it and eliminate noise

import string
# prepare a message sample
mess = 'Sample message! Notice: it has punctuation.'
# check the punctuation provided by string lib
string.punctuation
# replace all punctuations in sample message with space and ouput as a list
nopunc = [char for char in mess if char not in string.punctuation]
# check the list with original punctuation replaced with space
nopunc
# join the list back to a string of message
nopunc = ''.join(nopunc)
# check that the message is recovered without all punctuations 
nopunc
# stop words are some common words that should not be analyzed
from nltk.corpus import stopwords
# check the sample stop words from nltk library
stopwords.words('english')[:10]
# message could be split to a list of words for removing stop words
nopunc.split()
# clearn the words in stop words list from nopunc message
clean_mess = [word for word in nopunc.split() if word.lower() not in 
              stopwords.words('english')]
# check the stop words of "it" and "has" has been removed 
clean_mess

# create a function to eliminate punctuation and stopwords in text 
def text_process(mess):
    # 1. remove punc
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    # 2. remove stop words
    clean_mess = [word for word in nopunc.split() if word.lower() not in
                  stopwords.words('english')]
    # 3. return list of clean words back
    return clean_mess

# test the function on first five messages
messages['message'].head(5).apply(text_process)

# convert message in seqence of words into vector in sequence of numbers
# 1. find term frequency: how many times a word occur in each message
# 2. inverse doc frequency: to have frequent words with lower weight
# 3. L2 norm: normalize the vectors to unit length

# 1. create an all words against all messages 2D matrix
from sklearn.feature_extraction.text import CountVectorizer
# create the bag of words transformer
bow_transform = CountVectorizer(analyzer=text_process).fit(messages['message'])
# check the total number of unique words found from all messages
print(len(bow_transform.vocabulary_))

# take one message to test the model function
mess_test = messages['message'][3]
# check content of the message for test
print(mess_test)
# transform the test message to a vector
bow_test = bow_transform.transform([mess_test])
# check the vector presentation of the test message
print(bow_test)
# check the shape of vectorized message
print(bow_test.shape)
# check the ones which appear twice
bow_transform.get_feature_names()[4068]
bow_transform.get_feature_names()[9554]

# transform the entire dataframe of messages
messages_bow = bow_transform.transform(messages['message'])
print('Shape of the Sparse Matrix:',messages_bow.shape)
# check the non zero accurencies
print('Amount of the Non-Zero occurences:', messages_bow.nnz)
# check the sparsity, how much percentage of zeros in matrix
sparsity = (100.0*messages_bow.nnz/(messages_bow.shape[0]*messages_bow.shape[1]))
print('Sparsity:',sparsity)


# 2. use Term Frequency - Inverse Document Frequency to evaluate how important
# a word is to a document in a collection of documents (corpus). The importance
# increases proportionally to the number of times a word appears in the doc but
# is offset by the frequency of the word in corpus. One simple ranking function
# is sum tf-idf for each query term. TF is calculated by dividing the times a
# word appears in a document with the total number of words in that document.
# IDF is calculated by deviding the logarithm of the number of documents in
# that corpus with number of documents the specific term appears. The fianal
# tf-idf value is calculated by multiplying the TF value and IDF value.

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer().fit(messages_bow)
# test the tfidf transformer with the test vector
tfidf_test = tfidf_transformer.transform(bow_test)
print('Before the tfidf transform:\n{}'.format(bow_test))
print('After the tfidf transform:\n{}'.format(tfidf_test))
# check the inverse document frequency of a word
tfidf_transformer.idf_[bow_transform.vocabulary_['u']]
tfidf_transformer.idf_[bow_transform.vocabulary_['university']]

# transform the entire bag of words corpus into tf-idf corpus
messages_tfidf = tfidf_transformer.transform(messages_bow)
print(messages_tfidf.shape)

# use Naive Bayes classifier algorithm to train the model
from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(messages_tfidf,messages['label'])
# test the prediction of the model on the test vector
spam_detect_model.predict(tfidf_test)[0]
messages['label'][3]
# apply model to the entire tfidf transformed dataset
all_pred = spam_detect_model.predict(messages_tfidf)

# evaluate the model performance
from sklearn.cross_validation import train_test_split
msg_train,msg_test,label_train,label_test = train_test_split(
        messages['message'],messages['label'],test_size=0.2)
print('The splitted data has {} to train, {} to test and {} in total.'.
      format(len(msg_train),len(msg_test),len(msg_train)+len(msg_test)))


# use pipeline feature to chain multiple estimators into one
from sklearn.pipeline import Pipeline
pipeline = Pipeline([('bow',CountVectorizer(analyzer=text_process)), # string to token int counts
                     ('tfidf',TfidfTransformer()), # int counts to weighted TF-IDF scores
                     ('classifier',MultinomialNB())]) # train on TF-IDF scores with NB classifier
pipeline.fit(msg_train,label_train)
predictions = pipeline.predict(msg_test)

from sklearn.metrics import classification_report
print(classification_report(label_test,predictions))

# reference
# dataset: https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
# bag of words: https://en.wikipedia.org/wiki/Bag-of-words_model
# normalize text: https://en.wikipedia.org/wiki/Stemming
# normalize text: http://www.nltk.org/book/ch05.html
# textbook: http://www.nltk.org/book/
# textbook: https://www.kaggle.com/c/word2vec-nlp-tutorial
# textbook: http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
# https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html
# https://en.wikipedia.org/wiki/Sparse_matrix
# https://en.wikipedia.org/wiki/Tf–idf
# http://www.inf.ed.ac.uk/teaching/courses/inf2b/learnnotes/inf2b-learn-note07-2up.pdf
# https://en.wikipedia.org/wiki/Naive_Bayes_classifier
# https://en.wikipedia.org/wiki/Precision_and_recall
# http://scikit-learn.org/stable/modules/pipeline.html
# https://en.wikipedia.org/wiki/F1_score