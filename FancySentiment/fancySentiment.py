import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def fancySentiment(comments):
	stopword = set(stopwords.words('english') + list(string.punctuation) + ['n\'t'])
	filtered_comments = []
	for i in comments:
		words = word_tokenize(i)
		temp_filter = ""
		for w in words:
			if w not in stopword:
				temp_filter += str(w)
				temp_filter += ' '
		filtered_comments.append(temp_filter)
	filtered_comments_str = ' '.join(filtered_comments) 
	sentiment = WordCloud(background_color = 'orange', max_words=100)
	sentiment.generate(filtered_comments_str)
	plt.figure()
	plt.imshow(sentiment)
	plt.axis("off")
	plt.show()
