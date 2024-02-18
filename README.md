## MOVIE RECOMMENDATION SYSTEM

![Website Screenshot](imgg.jpeg)

## Website

[GET ROCOMMENDED](https://movie-recommendation-system-6dsabbtei9kns3qby52xwx.streamlit.app/)


## Cosine Similarity

Cosine similarity is a metric used to measure the similarity between two vectors in a multi-dimensional space. It calculates the cosine of the angle between these vectors, which is a measure of how closely they align with each other. The formula for cosine similarity is:

\[ \text{cosine\_similarity}(\mathbf{A}, \mathbf{B}) = \frac{\mathbf{A} \cdot \mathbf{B}}{||\mathbf{A}|| \cdot ||\mathbf{B}||} \]

where \( \mathbf{A} \) and \( \mathbf{B} \) are the vectors being compared, \( \cdot \) denotes the dot product, and \( ||\mathbf{A}|| \) and \( ||\mathbf{B}|| \) are the magnitudes of the vectors.

### Applications

Cosine similarity finds applications in various fields, including:

- **Natural Language Processing (NLP):** In text analysis, documents can be represented as vectors of word frequencies or embeddings. Cosine similarity is used to measure the similarity between documents, enabling tasks such as document clustering, information retrieval, and document similarity ranking.

- **Information Retrieval:** Cosine similarity is utilized in search engines to match user queries with relevant documents. By computing the similarity between the query vector and document vectors, search engines can rank documents based on their relevance to the query.

- **Recommendation Systems:** In collaborative filtering recommendation systems, user-item interactions are represented as vectors. Cosine similarity is employed to find similar users or items based on their interaction vectors, enabling personalized recommendations.

- **Image Processing:** Cosine similarity can be applied to compare image features extracted using techniques like Convolutional Neural Networks (CNNs). It helps in tasks such as image retrieval and content-based image recommendation.

### Example

Here's a simple example of calculating cosine similarity in Python using NumPy:

```python
import numpy as np

# Define two vectors
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Compute cosine similarity
cos_sim = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))
print("Cosine Similarity:", cos_sim)
