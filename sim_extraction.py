# prompt: now use all above code to design a function which takes chunked reviews list as input as well as product name as input and gives the overall sentiment scores like above in output

import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")
model = SentenceTransformer('all-MiniLM-L6-v2')
def calculate_overall_sentiment(chunked_reviews, product_name):
  """
  Calculates the overall sentiment score for a list of chunked reviews related to a product.

  Args:
    chunked_reviews: A list of chunked reviews.
    product_name: The name of the product.

  Returns:
    A dictionary containing the overall positive and negative sentiment percentages.
  """

  # Load the sentiment analysis pipeline
  

  # Function to calculate sentiment score
  def calculate_sentiment_score(text):
    """
    Calculates the sentiment score for a given text.

    Args:
      text: The text to analyze.

    Returns:
      A dictionary containing the overall sentiment score (out of 100) and the sentiment label.
    """
    result = sentiment_pipeline(text)[0]
    label = result['label']
    score = result['score']
    # Convert score to a percentage out of 100
    if label == 'POSITIVE':
      sentiment_score = score * 100
    else:
      sentiment_score = (1 - score) * 100

    return {"sentiment_score": sentiment_score, "label": label}

  # Calculate embeddings for the product and reviews
  product_embedding = model.encode(product_name)
  review_embeddings = model.encode(chunked_reviews)

  # Calculate cosine similarity between product and reviews
  similarities = cosine_similarity([product_embedding], review_embeddings)

  # Set a threshold for relevant reviews
  threshold = 0.5
  relevant_reviews = [chunked_reviews[i] for i in range(len(chunked_reviews)) if similarities[0][i] >= threshold]

  # Calculate overall sentiment scores
  positive_count = 0
  negative_count = 0

  for review in chunked_reviews:
    sentiment_result = calculate_sentiment_score(review)
    if sentiment_result['label'] == 'POSITIVE':
      positive_count += sentiment_result['sentiment_score']
    else:
      negative_count += sentiment_result['sentiment_score']

  total_count = positive_count + negative_count
  positive_percentage = (positive_count / total_count) * 100
  negative_percentage = (negative_count / total_count) * 100

  return {"positive_sentiment": positive_percentage, "negative_sentiment": negative_percentage}
