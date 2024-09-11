# prompt: now generate other file using fastapi python to carry out above functionality

from fastapi import FastAPI
from sim_extraction import calculate_overall_sentiment

app = FastAPI()


@app.post("/analyze_sentiment/")
async def analyze_sentiment(data: dict):
    """
    Analyzes the sentiment of reviews for a given product.

    Args:
      data: A dictionary containing the product name and a list of reviews.
        Example:
        {
          "product_name": "samsung galaxy z fold6",
          "reviews": [
            "This phone is amazing!",
            "The camera is not very good.",
            "I love the design."
          ]
        }

    Returns:
      A dictionary containing the overall positive and negative sentiment percentages.
    """
    product_name = data["product_name"]
    reviews = data["reviews"]
    # Calculate overall sentiment
    result = calculate_overall_sentiment(reviews, product_name)
    return result

