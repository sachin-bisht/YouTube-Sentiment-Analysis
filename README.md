# YouTube-Sentiment-Analysis

Scrape all the YouTube comments using api.

## Description :
This project works by scraping YouTube comments and identify the sentiment of comments.

The directory FancySentiment shows the WordCloud (most frequent words) of the comments.

The directory CommentSentiment shows the positive/negative sentiment (using NaiveBayesClassifier) of the comments.

## Prerequisite :
_Python 3_

_pip(Python Package Index) :_

> $ sudo apt-get install python3-pip

_requests package :_

> $ sudo pip3 install requests

_lxml package :_

> $ sudo apt-get install libxml2-dev libxslt1-dev python-dev

> $ pip3 install lxml

_matplotlib package :_

> $ sudo pip3 install matplotlib

_nltk package :_

> $ sudo pip3 install nltk

_wordcloud package :_

> $ sudo pip3 install wordcloud


## How to run :
First input the __API key__ in the file.

__CommentSentiment/comment_extract.py__

__FancySentiment/comment_downloader.py__

Then run the __driver.py__ file.
