## Build your own Decision Stump

Let's build our own Classifier from Scratch.

* **Data**:  [UCI Congress Voting Records](https://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records)

* **Target**: Given a voting record, can you predict the member to be a Democrat or Republican

### Task

1. Impute y/n into 1/0

2. Split the data into Train and Test using `sklearn.cross_validation.train_test_split` with `random_state=42` and `test_size=0.2`

3. Build a Decision Stump Classifier from scratch.  Not with Shit learn :-)

You classifier should do the following:

1. For each feature (0/1) split the data, evaluate the split the feature that makes least mistakes i.e., `accuracy` metric.

2. Build 100 such decision stumps by randomly selecting a Subset of Features / Data on each decision stump.  Each tree is only decision stump (split).  In other words the depth of tree is 1.

3. Use Random Forest style ensemble Voting and choose the majority voted class as your prediction.


Challenge:

Can you build Decision Stumps that are more than 1 level deep?
