import training_classifier as tcl
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize	
import os.path
import pickle
from statistics import mode
from nltk.classify import ClassifierI
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import BigramCollocationFinder as BCF
import itertools
from nltk.classify import NaiveBayesClassifier


def features(words):
	temp = word_tokenize(words)

	words = [temp[0]]
	for i in range(1, len(temp)):
		if(temp[i] != temp[i-1]):
			words.append(temp[i])

	scoreF = BigramAssocMeasures.chi_sq

	#bigram count
	n = 150

	bigrams = BCF.from_words(words).nbest(scoreF, n)

	return dict([word,True] for word in itertools.chain(words, bigrams))

class VoteClassifier(ClassifierI):
	def __init__(self, *classifiers):
		self.__classifiers = classifiers

	def classify(self, comments):
		votes = []
		for c in self.__classifiers:
			v = c.classify(comments)
			votes.append(v)
		con = mode(votes)

		choice_votes = votes.count(mode(votes))
		conf = (1.0 * choice_votes) / len(votes)

		return con, conf

def sentiment(comments):

	if not os.path.isfile('classifier.pickle'):
		tcl.training()

	fl = open('classifier.pickle','rb')
	classifier = pickle.load(fl)
	fl.close()

	pos = 0
	neg = 0
	for words in comments:
		comment = features(words)
		sentiment_value, confidence = VoteClassifier(classifier).classify(comment)
		if sentiment_value == 'positive':# and confidence * 100 >= 60:
			pos += 1
		else:
			neg += 1

	print ("Positive sentiment : ", (pos * 100.0 /len(comments)) )
	print ("Negative sentiment : ", (neg * 100.0 /len(comments)) )
