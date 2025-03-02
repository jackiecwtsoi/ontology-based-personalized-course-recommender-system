# Literature Review

In this section, we review more than 20 papers on the concept of recommender systems. Specifically, we break our research down into various parts and review papers for each of these parts.

## Ontology Construction

- [Ontology Development 101: A Guide to Creating Your First Ontology](https://protege.stanford.edu/publications/ontology_development/ontology101.pdf)
- [Semantic searching IT careers concepts based on ontology](http://www.joams.com/uploadfile/2013/0426/20130426033427832.pdf)

RDF - Resource Description Framework

## Web Crawling
- [Uni-Search - A Web Crawler for Career Matching and University of Choice Detection](https://su-plus.strathmore.edu/handle/11071/4037)
- [Focused Crawling for Educational Materials from the Web](https://www.interscience.in/cgi/viewcontent.cgi?article=1020&context=ijcsi)
- **[Focused crawling of tagged web resources using ontology](https://www-sciencedirect-com.eproxy.lib.hku.hk/science/article/pii/S0045790612001759?via%3Dihub)**
- [SOF: a semi-supervised ontology-learning-based focused crawler](https://onlinelibrary.wiley.com/doi/abs/10.1002/cpe.2980)

## Ontology-Based Recommender System

- [Ontology-Based Personalized Course Recommendation Framework](https://ieeexplore.ieee.org/document/8587168)
- [An Ontology-Based Recommender System with an Application to the Star Trek Television Franchise](https://arxiv.org/abs/1808.00103)
- [An ontology-based hybrid e-learning content recommender system for alleviating the cold-start problem](https://link-springer-com.eproxy.lib.hku.hk/article/10.1007/s10639-021-10508-0)
- [Knowledge-based recommendation: A review of ontology-based recommender systems for e-learning](https://link.springer.com/article/10.1007/s10462-017-9539-5)
- [Course-recommendation system based on ontology](https://ieeexplore.ieee.org/document/6890767)

## Recommender Engine

### Collaborative-Based Filtering (CF) Method

<!-- - [Item-based collaborative filtering recommendation algorithms](https://dl.acm.org/doi/10.1145/371920.372071)
- [Amazon.com recommendations: Item-to-item collaborative filtering](https://ieeexplore.ieee.org/document/1167344) -->
- [Using semantic similarity to enhance item-based collaborative filtering](http://facweb.cs.depaul.edu/mobasher/research/papers/JM03.pdf)
- [An improved collaborative filtering method for recommendations' generation](https://ieeexplore.ieee.org/document/1401179)

### Content-Based Filtering (CBF) Method

- [Content-based recommendation systems](https://link.springer.com/chapter/10.1007/978-3-540-72079-9_10)

### Hybrid Filtering Method

- [A hybrid course recommendation system by integrating collaborative filtering and artificial immune systems](https://www.mdpi.com/1999-4893/9/3/47)
- [DBNCF: Personalized courses recommendation system based on DBN in MOOC environment](https://ieeexplore.ieee.org/document/8005400)

## Deep Learning Based Recommender Engines

- [A review on deep learning for recommender systems: challenges and remedies](https://daiwk.github.io/assets/Batmaz2018_Article_AReviewOnDeepLearningForRecomm.pdf)
- [Neural Collaborative Filtering (NCF)](https://arxiv.org/abs/1708.05031)
- [A content-based recommendation algorithm for learning resources](https://link.springer.com/article/10.1007/s00530-017-0539-8)

# Fundamental Concepts of Recommender Systems

## Basic Methods

### 1. Content based filtering (CBF)

  **Goal**: To predict user's rating for an item
  
  **Definition**:

  - Use item's content vector  ${\bf x}^{(i)} $ to predict user's preference vector  ${\bf \beta}^{(j)} $
  - Preference vector dot content vector gives rating of item $i$ by user $j$

### 2. Collaborative filtering (CF)

  1. User-based CF
  2. Item-based CF

  **Goal**: To predict user's rating for an item

  **Definition**:

  - Used when we do not already have content vectors for the items or/nor preference vectors for the users
  - To predict content vectors: Use user's preference vector  ${\bf \beta}^{(j)} $ to predict item's content vector  ${\bf x}^{(i)} $

  **Algorithm**:

  1. Initialize content vectors and preference vectors 
  2. Minimize joint cost function using gradient descent
  3. Calculate rating by using dot product

  **Problems**:
  - Data sparsity
  - Cold start
  - Scalability

## Typical Recommender Problems

**1. How to find items $j$ related to item $i$?**

- Minimize the distance between content vectors of item $i$ and item $j$

**2. What about users who have not rated any movies?**

- Problem: Original CF would predict new user to have rating of $0$ for every item (because of the way the cost function is set up)
- Solution: Mean normalization
  - Calculate mean for every item across all users
  - Take the big ratings matrix and subtract by the mean
  - Use this new matrix to learn the vectors, and add the mean vector
  - Result: New user who has not rated anything would now give rating for a particular item by its mean

# Literature Deep Dive

### Deep Dive #1 - OPCR

[Original paper](https://ieeexplore.ieee.org/document/8587168)

![OPCR main architecture](/screenshots/OPRC_main_architecture.png)

**Ontology model**

1. Course ontology
2. Student ontology
   - Personal & educational attributes
   - User's rating of the previously recommended course(s)
3. Job ontology

**Recommender engine**

The paper uses a hybrid recommender engine to generate recommendations.

- For CBF (content-based filtering):
  The course ontology (item profile) is mapped onto the student ontology (user profile), and similarity scores are generated.
- For CF (collaborative-based filtering):
  - Measuring the similarity between the active user and other users in the database
  - Enhance the KNN algorithm using a new algorithm OKNN (ontology similarity)
- Final scoring algorithm
