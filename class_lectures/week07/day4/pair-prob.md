You are given documents as probability distributions over topics, and topics as probability distributions over words.

Implement a function `make_doc` that takes a document (as `topic_probs`) and a number of words. The function should randomly generate a document by choosing a topic for each word using the document's topic probabilities and then choosing a particular word using that topic's word probabilities. The function should return a string containing all the generated document's words.

For example:

```python
docs = [[0.98, 0.01, 0.01],
        [0.01, 0.98, 0.01],
        [0.01, 0.01, 0.98]]
topics = [[ 0.4,      0.4,   0.01,        0.01,    0.01,       0.01,
            0.1,     0.04,   0.01,        0.01],
          [0.01,     0.01,    0.4,         0.4,    0.01,       0.01,
            0.1,     0.04,   0.01,        0.01],
          [0.02,     0.02,   0.01,        0.01,     0.4,        0.4,
           0.02,      0.1,   0.01,        0.01]]
words =  ['cat', 'kitten',  'dog',     'puppy',  'deep', 'learning',
          'fur',  'image',  'GPU', 'asparagus']


def make_doc(topic_probs, n_words):
    raise NotImplementedError

for doc in docs:
    print make_doc(topic_probs=doc, n_words=10)
```

**Stop and Think**:  
- Analytically, what are the probability distributions that you have been given?
  - Can you write them down in symbols?
    - Use `d` for 1 document, `D` for all documents
    - Use `w` for 1 word, `W` for all words
    - Use `t` for 1 topic, `T` for all topics  
    - You may not need to use all of these variables in your expressions
    - You can get creative with notation if you think you need other symbols (e.g. $W_d$ for all words in a given document)   
- What if you flipped the problem and were given the words only (aka just a bunch of documents) and had to make your best guess at the real probability distributions?  How would you do it?  
  - You can assume you know the number of topics ahead of time.
  - **Hint**: You should recall a very special rule we've encountered a few times that flips the equation when talking about conditional probabilities :wink:
- Submit your answers to these questions as well via slack.
