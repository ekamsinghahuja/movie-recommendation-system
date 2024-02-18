# MOVIE RECOMMENDATION SYSTEM

![Website Screenshot](imgg.jpeg)

# Website

[GET ROCOMMENDED](https://movie-recommendation-system-6dsabbtei9kns3qby52xwx.streamlit.app/)

# main notebook
[Link](https://www.kaggle.com/ekamsingh123go/movie-rec)

# DataSet Used

The dataset used in this project contains information on 5000 movies, including various details such as genre, cast, crew, and more. This dataset serves as the foundation for the analysis helps in building recommendation system

# Types of Recommendation Systems

In this project, we utilize Content-Based Filtering recommendation systems to provide personalized recommendations to users. 
The main types of recommendation systems implemented are:

## Content-Based Filtering:
Content-based filtering methods are based on the description of a product and a profile of the user’s preferred choices. In this recommendation system, products are described using keywords, and a user profile is built to express the kind of item this user likes.
**For instance, if a user likes to watch movies such as Iron Man, the recommender system recommends movies of the superhero genre or films describing Tony Stark.**

<p align="center">
<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3YEZG1dEqvNz70h0uhP5Fg.png" alt="Image" width="50%" height="50%">
</p>
<!-- ![Image](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3YEZG1dEqvNz70h0uhP5Fg.png){:height="50%" width="50%"} -->


## Collaborative Filtering:
The collaborative filtering method is based on gathering and analyzing data on user’s behavior. This includes the user’s online activities and predicting what they will like based on the similarity with other users.For example, if user A likes Apple, Banana, and Mango while user B likes Apple, Banana, and Jackfruit, they have similar interests. So, it is highly likely that A would like Jackfruit and B would enjoy Mango. This is how collaborative filtering takes place.

<p align="center">
<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SPE85ePd_aiJDO9RVbfbig.png" alt="Image" width="50%" height="50%">
<!-- ![Image](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SPE85ePd_aiJDO9RVbfbig.png){:height="50%" width="50%"} -->
</p>
   
## Hybrid Recommendation Systems:**
 In hybrid recommendation systems, products are recommended using both content-based and collaborative filtering simultaneously to suggest a broader range of products to customers. This recommendation system is up-and-coming and is said to provide more accurate recommendations than other recommender systems.

<p align="center">
<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jBBeSKBQg4H7VslNT34f4w.png" alt="Image" width="50%" height="50%">
</p>


## Recommendation System Workflow

This project implements a content-based recommendation system for suggesting similar movies based on textual features. The following steps outline the workflow of the recommendation system:

1. **Building the Corpus:**
   - The movie dataset is used to construct a corpus containing various textual features such as title, overview, genres, keywords, cast, and crew. Each movie in the corpus is represented by these features.

2. **Data Cleaning:**
   - Data cleaning techniques are applied to ensure that the dataset is in a suitable format for analysis. This involves handling missing values, removing duplicates, and standardizing text formats.

3. **Applying Count Vectorizer:**
   - Textual features such as movie titles, overviews, genres, keywords, cast, and crew are transformed into numerical representations using Count Vectorization. This process converts each text feature into a vector of term frequencies.

4. **Cosine Similarity Pairwise:**
   - Pairwise similarities between movies are computed using cosine similarity. This metric measures the cosine of the angle between two vectors, providing a measure of similarity between them. The similarity scores capture the relationships between movies based on their textual features.

5. **Sorting for Each Film and Extracting Best 5 Films:**
   - For each movie, the similarity scores obtained from cosine similarity are sorted in descending order. This sorting allows the identification of the top movies that are most similar to each given movie. The top 5 similar movies are then extracted for each movie, forming the basis for recommendations.

By following these steps, the recommendation system analyzes textual features of movies to suggest similar movies, enhancing the overall movie-watching experience for users.


# Count Vectorizer

Count Vectorization is a technique used in natural language processing (NLP) to convert a collection of text documents into a numerical representation that machine learning algorithms can understand. It's one of the simplest and most commonly used methods for text feature extraction.

<p align="center">
  <img src="https://www.educative.io/api/edpresso/shot/5197621598617600/image/6596233398321152" alt="Image" width="50%" height="50%">
</p>


# Cosine Similarity

Cosine similarity is a metric used to measure the similarity between two vectors in a multi-dimensional space. It calculates the cosine of the angle between these vectors, which is a measure of how closely they align with each other. for better understanding , please refer

<p align="center">
  <img src="sim_ex.jpeg" alt="Image" width="50%" height="50%">
</p>

