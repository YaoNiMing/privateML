# Luther Vandross - D.H. Kim

See leggo.ipynb for reference in terms of code base. My investigation revolved around trying to find drivers of combined gross revenue based on thirty or so variables that I believe were predictive (correlated). There was significant correlation among variables which violated standard OLS procedures and diluted the meaning of coefficients. However, that also meant that the model may possibly lead to lower residual sum of squares on the test set. The model in of itself is however volatile (high variance). Unfortunately, I didn't have the sufficient time to regularize all my paramters which would definitively have increased my model's performance on the test set. I also did not utilize gridsearch or other techniques to procure select features that could be the best parameters for my model. There are many things I would have done, and these regrets will be posted on my blog. This markdown is also to be updated as I continue to develop the model for Luther. 

- CV R2:  0.90477365523
- Test R2 : 0.885177847709
- RSME: 6477840495547744.0


