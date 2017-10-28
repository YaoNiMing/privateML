# Pair Programming

[Pairing](http://www.wikihow.com/Pair-Program), ideally, is good for both participants and for the work they produce.

We would like to have everyone do some morning pairing with everyone else.


#### Problem

The first problem is to determine a schedule of pairings so that everyone has a pair every day, and everyone eventually pairs with everyone else.

Write a function that takes a list of names and returns a list of lists of tuples representing pairs. (Assume an even number of names, all distinct.) For example:

```
>>> pairs_for(['Andrea', 'Bob', 'Cassandra', 'Doug'])
# [[('Bob', 'Cassandra'), ('Andrea', 'Doug')],
#  [('Andrea', 'Bob'), ('Cassandra', 'Doug')],
#  [('Andrea', 'Cassandra'), ('Bob', 'Doug')]]
```

##### Extra Credit

Modify your function so that it elegantly handles the case where there are an odd number of students by having one trio per day.

List of Student names for you to generate this list:
```
Christopher Buie
Rebecca Hyde
Nils Hansen
Catherine Henderson
Travis James
D.H. Kim
Kyle Mix
Sarick Shah
Bob Tian
Samuel Wong
Rohan Shah
Li Zhang
Veena Kumar
Kevin Du
Joshua Concepcion
Daniel Vigil
Kaushik Vasudevan
Ronald Olshansky-Lucero
Andrea Everett
Nicholas Thomas
James McGlone
Zach Gambill
William Sanders
Jennifer Wang
```
