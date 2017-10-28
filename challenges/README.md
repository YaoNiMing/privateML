## Instructions for Submitting Challenges

#### 1.  GitHub - notices
Your GitHub settings should be set to receive email notifications by email.  Below are instructions on setting this up:

>a) In GitHub, on upper right corner, click on your profile picture, then "Settings"

>b) On left menu, under "Personal Settings", click on "Notification Center"

>c) On right menu, under "Participating", make sure both boxes, "Email" and "Web" are checked.

#### 2.  GitHub Folder Naming Convention
Use lower-case names and underscores, preferably your first name.  (This is because GitHub folder/file names are case-sensitive.)  In the case there is someone in the class with your same first name, you can use:  firstname_lastname for folder name.

#### 3.  Submitting Files
>a) Submit Jupyter notebook for challenges instead of *.py files.  Makes it easier to follow:  code, output & graphs.

>b) Submit one file.  (Don't submit several versions of files.)

>c) *DO NOT SUBMIT* data files.  There will already be a copy of data file on GitHub in the challenges_data folder.  We want to avoid multiple copies of data files.  It takes up unnecessary space and slows server down needlessly.

#### 4.  Setting up Jupyter Notebook
>a) Add a header section to your notebook
```
Challenge Set 1
Topic:        Explore MTA turnstile data
Date:         xx/xx/xxxx
Name:         student name
Worked with:  other student's name
```

>b) Label challenge numbers in bold.

#### 5.  Graphs
>a) To includes graphs in the Jupyter notebook, include the following code:
```
%matplotlib inline
import matplotlib.pyplot as plt
```

>b) All graphs should have a title.  Also, label both x and y axes.

#### 6.  Comparing results
To compare results consistently, where applicable, use:  test_size=0.30, random_state=4444.  You can always experiment with different test_size and random_state, but for submission purposes, use these given settings.

#### 7.  Don't print copious output in your Jupyter notebook.
For dictionaries, print a few key/value pairs.  Don't print more than 10-20 lines of data (of data frame or array).
