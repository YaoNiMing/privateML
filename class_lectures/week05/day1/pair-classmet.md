## Pair Problem

Let's use the digits dataset again!

1. Load the Handwritten digits dataset using sklearn
2. Convert the dataset into a binary classification problem by augmenting the target values:
  - Class 0: The digit is a zero
  - Class 1: The digit is not a zero
2. Split the dataset into a train/test set
3. Build a classifier against the digits dataset using either:
  - Support Vector Machines
  - Logistic Regression
4. Use your model to make predictions against the test set for zero/nonzero.
5. Compute the **accuracy** of your model against the test set.
6. Let's examine your model performance at different **thresholds**:
  - Use your predictions to retrieve the probabilistic scores for each class for all instances (`predict_proba`)
  - Create 2 empty arrays `tp` and `fp` to store the results from the following loop:
  - For threshold values from 1.0 to 0.0 in intervals of 0.05:
    - Consider a digit to be nonzero if your model predicts a probability greater than the threshold
    - Classify all the test digits according to that rule
    - Calculate the number you correctly predicted nonzero
      - Append this value to `tp`
    - Calculate the number of zeros you incorrectly predicted as nonzero
      - Append this value to `fp`
  - Divide every element in `tp` and `fp` by the number of nonzero digits in the test set
  - Plot `tp` along the y-axis against `fp` on the x-axis
  - What have you done?
  - Which value of the threshold would you select for your final model?  Why?
7. What is the accuracy of your selected model?
8. What is the value of `tp` for the model that you selected?
  - What does this represent?
9. What is the value of `tp`/(`tp` + `fp`) for your chosen model?
  - What does this represent?

Please submit the following:
- Your Classifier of choice
- Your code
- A quick explanation of the threshold you selected and why.
