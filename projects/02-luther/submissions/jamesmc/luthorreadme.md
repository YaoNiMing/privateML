# Project Luthor README

## Proposal

Predict Domestic Revenue of foreign language films. Understanding how to maximize box office impact of a film can provide strong incentive for foreign films. The vast majority of films under the foreign language genre category are either wholly or partially produced abroad. Understanding how similar films performed in the domestic market can give insight as to how to approach a theatre release and through which (type of) distributor.

## Final Features:

1. Distributor type (Major, Mini-major, minor)
2. Runtime
3. Widest Release
4. Foreign Revenue
5. Genre (Action)

## Results

Linear Regression score: ~.22

## Comments

* Due to heavy loss of variables during data cleaning, only 5 features remained that were used for modeling. Adding more features (e.g. directors, rating, actors, budget, etc.) would provide greater insight and opportunity to more accurately predict which movies are successful at the box office.

* Limited to using only a linear regression model, utilizing other models (e.g. Random Forest) may produce better results. 

* A number of top high-grossing movies slightl skewed outcomes but more importantly stood out when plotted. These top-ranking movies could be specifically examined for possible commonalities to their success. At the same time, examining the body of movies without them may also provide insight on general trends for movies with revenue values at order of magnitude less or more.