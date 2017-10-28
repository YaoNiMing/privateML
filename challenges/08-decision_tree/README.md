### Tree / Forest Challenges

Note: for challenge 1, acquire the [Congressional Voting Records Dataset](https://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records)

#### Challenge 1

For the house representatives data set, fit and plot a decision tree classifier to decide whether each member of the 1984 US Congressional assembly is (was?) a Democrat or a Republican. Examine the rules your tree uses.


#### Challenge 2 (Optional but recommended)

Tackle the [Titanic Survivors kaggle competition](https://www.kaggle.com/c/titanic-gettingStarted) with decision trees. Look at your splits; how does your tree decide?


##### `pydot` for decision tree plotting & path inspection:

You can examine the decision paths of an `sklearn` tree by generating `pydot` graphs as in the `sklearn` [documentation](http://scikit-learn.org/stable/modules/tree.html). It's sometimes tricky to get `pydot` working -- if you're having trouble try the following Installation steps.


### Installing pydot (might need to be modified for Linux or Windows):

Note: Uninstall pydot if you already installed it but it's not working

    pip uninstall pydot

Otherwise, you can start here:

    pip uninstall pyparsing

    pip install -Iv
    https://pypi.python.org/packages/source/p/pyparsing/pyparsing-1.5.7.tar.gz#md5=9be0fcdcc595199c646ab317c1d9a709

    pip install pydot

    brew install graphviz