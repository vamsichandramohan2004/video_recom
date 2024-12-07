# video_recomndation_system

my_new_project Documentation
Overview
Project Name: video_recommendation_system
Description: This project involves creating a recommendation system with an API to suggest posts to users based on their preferences. The system uses username, category_id, and mood as inputs to provide personalized content.
Approach
The system uses a collaborative filtering approach combined with mood-based adjustments to generate recommendations. By leveraging user interaction data (e.g., previous posts viewed, liked, or shared) and mood-based context, the system tailors its recommendations to the user's current emotional state and preferred content category.
Key Decisions Made:
- Model Selection: The recommendation system uses collaborative filtering techniques (e.g., matrix factorization or user-item interactions) to predict which posts will be most relevant to a user based on their historical data.
- Mood Adjustment: A dynamic element was added to the recommendation algorithm, where user mood influences the ranking of suggested posts, increasing the relevance based on current emotional state.
- Evaluation Metric: The performance of the model is evaluated using Root Mean Square Error (RMSE), with a final score of 0.29, indicating good accuracy in the prediction of user preferences.
Model Architecture
The architecture consists of several layers:
1. Data Layer: User data, post data, and mood data are collected and stored.
2. Preprocessing Layer: User interactions and mood are preprocessed into features used for the recommendation engine.
3. Recommendation Engine: The collaborative filtering model predicts scores for user-post pairs.
4. Mood Adjustment: Mood-based adjustments modify the recommendations based on the current emotional state of the user.
5. Post Processing Layer: The system filters and ranks the recommended posts based on relevancy and mood.
API Endpoints
1. Feed with Mood Input:
URL:
http://localhost:port_no/feed?username=your_username&category_id=category_id_user_want_to_see&mood=user_current_mood

This endpoint returns 10 recommended posts tailored for the user based on:
- username: Identifies the user for personalized recommendations.
- category_id: Specifies the type of content the user wants to see (e.g., music, news, sports).
- mood: The user’s current emotional state, which adjusts the recommendations accordingly.

Response Example:
{
  "recommended_posts": [
    {"post_id": 123, "title": "Post Title 1", "category": "music", "mood_recommendation_score": 0.87},
    {"post_id": 124, "title": "Post Title 2", "category": "news", "mood_recommendation_score": 0.92},
    ...
  ]
}
2. Feed without Mood Input:
URL:
http://localhost:port_no/feed?username=your_username&category_id=category_id_user_want_to_see

This endpoint returns 10 recommended posts based only on the username and category_id. It doesn’t take mood into account but will recommend content based on user history and selected category.

Response Example:
{
  "recommended_posts": [
    {"post_id": 125, "title": "Post Title 3", "category": "sports", "mood_recommendation_score": 0.65},
    {"post_id": 126, "title": "Post Title 4", "category": "entertainment", "mood_recommendation_score": 0.78},
    ...
  ]
}
3. Feed with Username Only:
URL:
http://localhost:port_no/feed?username=your_username

This endpoint returns 10 posts recommended solely based on the username, without considering category_id or mood. It will primarily rely on the user's historical interactions and preferences.

Response Example:
{
  "recommended_posts": [
    {"post_id": 127, "title": "Post Title 5", "category": "fashion", "mood_recommendation_score": 0.82},
    {"post_id": 128, "title": "Post Title 6", "category": "technology", "mood_recommendation_score": 0.76},
    ...
  ]
}
Performance Evaluation
Model Performance:
The model is evaluated using Root Mean Square Error (RMSE), which measures the difference between predicted and actual values. A lower RMSE indicates better accuracy in the recommendations.

RMSE Score: 0.24, MAE: 0.2
This score indicates that the model is performing well in predicting the most relevant posts for users.
