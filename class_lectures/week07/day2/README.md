### Plan for Tuesday, Nov 1

#### Overview

Today we'll cover our first real **Topic Modeling**, with **Latent Dirichlet Allocation (LDA)**.  LDA is a simple concept with a not-so-simple Bayesian derivation to get there.  Essentially though, we're focused on breaking documents into their relative proportions of component topics and topics into their related words.

**Remember:**
* SQL Challenges are due **11/4**
* Decision Tree Challenges are due **11/14**
* All other challenges are posted and **optional**

#### Schedule

**9:00 am**: What up!?

**9:15 am**: Pair Programming:  
  * Pair: [Documents as Topic Distributions](pair-lda.md)   

Pairings:  

| Partner 1 | Partner 2 |
|------|-----|
| Sam | Catherine |
| Nils | Bob |
| Will | Josh |
| Li | Kevin |
| Rohan | D.H. |
| Andrea | Ron |
| James | Kaushik |
| Jenn | Chris |
| Daniel | Veena |
| Sarick | Rebecca |
| Nick | Zach |
| Kyle | Travis |

**10:15 am**: Topic Modeling: LDA
* [Intro to Topic Modeling with LDA](Topic_Modeling.pdf)
* [LDA with `gensim`](LDA.ipynb)

**12:00 pm**: Feels like a Chipotle day

**1:30 pm**: Investigation Presentation: Rebecca on Improving Customer Service

**1:45 pm**: Work Time
* Get/process Fletcher data
* Challenges 7-8

**6:00 pm:** Tomorrow will be even better :wink:

### Further Resources

 * Christine Doig's [Introduction to Topic Modeling in Python](http://chdoig.github.io/pygotham-topic-modeling/) from PyGotham 2015
 * [Topic Models (Wikipedia)](http://en.wikipedia.org/wiki/Topic_model): This also has links to other main topic modeling algorithms:
     * Explicit semantic analysis (Using documents of another corpus as topics)
     * Latent semantic analysis  (PCA with Multinomial distribution, predecessor of LDA)
     * Latent Dirichlet allocation (LDA, the most popular one, what we went over today)
     * Hierarchical Dirichlet process (Hierarchical LDA)
     * Non-negative matrix factorization (A linear algebra based method)
 * [How does LDA work?](http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/): This is a pretty good explanation, I really recommend reading it.
 * [LDA Math](http://obphio.us/pdfs/lda_tutorial.pdf)
 * [Introduction to Probabilistic Topic Models](https://www.cs.princeton.edu/~blei/papers/Blei2011.pdf) from LDA originator David Blei
 * [gensim tutorial for working with corpora](http://radimrehurek.com/gensim/tut1.html)
 * [gensim tutorial for tfidf and topic modeling](http://radimrehurek.com/gensim/tut2.html)
 * [gensim LDAModel](http://radimrehurek.com/gensim/models/ldamodel.html)
 * Brandon Rose has a nice [notebook](http://brandonrose.org/clustering) demonstrating a whole process including using Gensim.
 * There's another Python package called [lda](https://pypi.python.org/pypi/lda).
 * [LDAvis: A method for visualizing and interpreting topics](http://nlp.stanford.edu/events/illvi2014/papers/sievert-illvi2014.pdf), a paper about the corresponding tool, which now has a Python version
