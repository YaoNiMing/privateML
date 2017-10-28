#Using Jupyter Notebook

###Launching the notebook
Navigate to the directory where you are working.  
```
$ jupyter notebook
```

Once you launch Jupyter, it will open the notebook in your default browser.

---

###First Steps
* On upper right, select "New" and then "Python 2" (or your default version of Python)
* Click on "Untitled" at upper left and rename your notebook.

###Running bash commands in a Jupyter notebook  
You can run bash (or terminal) commands right from the notebook!  
* Click on gray cell and type the following:  
`!pwd`  
* Run the cell by typing:  `shift + return`  
* Click on next gray cell and type the below.  
`!python --version`
* Run the cell by typing: `shift + return`

###Running python in a Jupyter notebook  
* Click on next gray cell and type the below.    
`print("Hello, World!)`
* Run the cell by typing: `shift + return`

###Other Helpful Commands

* **Help Menu** `esc + h`

* **Save Notebook** `command + s`

###Cell Types
There are 3 cell types:  
- Code  
- Markdown
- Raw

You can use Markdown in Jupyter Notebook as well!  Can add headers, blocks of text, etc. 

###Enabling `matplotlib` Graphics in the Notebook
Include the following two lines in your notebooks so the graphs are viewable.  
```
%matplotlib inline
import matplotlib.pyplot as plt
```
