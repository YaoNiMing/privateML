### Spam / Ham Filter:

Dataset: `https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection`

The first column is the label, the second column is some text recieved by SMS. 

1) Keep a 30% holdout set, seed=42
2) Use CountVectorizer or TFIDF or anything else for pre-processing.
3) Top AUC on Test Data from a non-XGboost model wins!