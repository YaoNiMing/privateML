#Jupyter (IPython) Notebook:  Getting Started
The Jupyter notebook is an interactive computational environment, in which you can combine code, execution, rich text, mathematics, plots and rich media. 

---

###[Install the Notebook](http://jupyter.readthedocs.io/en/latest/install.html)
Installing Jupyter using Anaconda and conda:  
For new users, we highly recommend [installing Anaconda](https://www.continuum.io/downloads). Anaconda conveniently installs Python, the Jupyter Notebook, and other commonly used packages for scientific computing and data science.  (Prereq: Python is installed.)
```console
$ conda install jupyter
```

###[Upgrade Jupyter Notebook](http://jupyter.readthedocs.io/en/latest/projects/upgrade-notebook.html)
```bash
$ conda update jupyter
```

###Run the Notebook at Terminal Prompt  
Note:  The notebook will open at the directory in which you launch the notebook on your terminal.  
```
$ jupyter notebook
```
>my example
```console
reshama$ jupyter notebook
[I 11:41:22.769 NotebookApp] Serving notebooks from local directory: /Users/reshamashaikh/_ds/metis
[I 11:41:22.769 NotebookApp] 0 active kernels 
[I 11:41:22.769 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
[I 11:41:22.769 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

###Shut Down the Juypter Notebook App
At terminal prompt:  
 * control + c
 * type:  `y`
 
>my example 
```console
^C[I 11:43:35.486 NotebookApp] interrupted
Serving notebooks from local directory: /Users/reshamashaikh/_ds/metis
0 active kernels 
The Jupyter Notebook is running at: http://localhost:8888/
Shutdown this notebook server (y/[n])? y
[C 11:43:37.782 NotebookApp] Shutdown confirmed
[I 11:43:37.783 NotebookApp] Shutting down kernels
reshama$ 
```

---

###Getting to Know Jupyter

You can try out Jupyter on a browser without installing it.  
https://try.jupyter.org/

