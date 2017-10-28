
## **Proposal for Project Luther**  
  
Build a model that advices studios what to spend their money on when producing a movie by setting up a regression with target Return on investment (=(Worldwide Total adj gross - adj Budget)/adj. Budget) and the following features:

1. Budget
2. Genre (Documentary, Foreign Language, Animiation, SciFi/ Fantasy, Comedy,
Romance/Drama, Action/ Adventure)
3. 3D technology
4. Reputation of Actors (via imbd list)
5. Reputation of Director (via imbd list)
6. MPAA Rating
7. Season (winter, summer, spring, autumn)
8. Runtime
9. Movie based on real story
10. Movie based on book  

Then evaluate the effect of each feature towards return on investment. As a second step, examine subsets of movies (e.g. by genre) to check whether model accurracy can be improved for the respective subset.

## **Main Results**  

1. Random Forest model has the best accuracy compared to Lasso and standard Linear Regression - R-sqrd of 0.26
2. Accuracy can be largely approved when only looking at Animation or Sci-Fi/ Fantasy movies