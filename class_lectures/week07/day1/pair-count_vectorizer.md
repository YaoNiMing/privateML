#### Pair Problem


text= ['It was the best of times, it was the worst of times.',  
      'My name is Inigo Montoya.You killed my father. Prepare to die.',   
       'Too weird to live, too rare to die!']


1) Using sklearn.feature_extraction.text CountVectorizer function, (also fit and transform) convert a collection of text documents to a matrix of token counts.

You will get a sparse matrix of output.
ex:

  (0, 0)	1    
  (0, 5)	2    
  (0, 11)	2    
  (0, 14)	2    
  (0, 15)	2    
  (0, 18)	2    
  (0, 20)	1    
  ...
  ...
  ...


Can you explain what each row of this matrix
represents?  

**Additionally**:
- Examine the Parameters of `CountVectorizer`
   - See how you can change these to change the resulting matrix!  What's happening?
   - Submit your understanding of each parameter
- Can you convert your matrix to the usual "dense matrix" format?  What is the difference?  Why/when do you think Sparse or Dense are used?
