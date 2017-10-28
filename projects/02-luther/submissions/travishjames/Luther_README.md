#Project Luther Submission

**The Problem**

Movie review sentiment is an important gauge of how well a particular film is perceived by the public. This can have large implications financially, and for advancing an individual director or actor's career. Thus, if a film studio could anticipate the type of review sentiment a film will receive before filming, then they could predict the success of the project while figuring out which aspects of the film contribute to that success. For this project, I used IMDB user score as a proxy for public movie review sentiment, and predicted user score using a number of features. These include runtime, gross domestic revenue, budget, Metacritic score, year and month of release, genre, among others. After performing feature selection and running various machine learning models on the data, I was was able to obtain a test-sample R-squared of 0.6879 using a ridge regression specification. This was a major improvement from a basic linear OLS model, and I am confident my model would perform well given additional data.

**Data Sources**

All relevant data was scraped from the IMDB website.

**Python Script**

All code used to scrape the IMDB website is contained within the Scraping-IMDB-Data.ipynb IPython notebook. All code used to analyze the data and run predictive models is contained within the Analyzing-IMDB-Data.ipynb notebook.