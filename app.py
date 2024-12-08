from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for demonstration purposes
posts = [
    {"id": 1, "category_id": 1, "mood": "happy", "view_count": 100, "average_rating": 4.5},
    {"id": 2, "category_id": 2, "mood": "sad", "view_count": 200, "average_rating": 4.8},
    {"id": 3, "category_id": 1, "mood": "excited", "view_count": 150, "average_rating": 4.2},
]

# Helper function to recommend posts
def recommend_posts(username, category_id=None, mood=None):
    filtered_posts = posts

    # Filter by category_id
    if category_id:
        filtered_posts = [post for post in filtered_posts if post["category_id"] == int(category_id)]

    # Filter by mood
    if mood:
        filtered_posts = [post for post in filtered_posts if post["mood"].lower() == mood.lower()]

    # Sort by view_count and average_rating
    recommended_posts = sorted(
        filtered_posts,
        key=lambda x: (x["view_count"], x["average_rating"]),
        reverse=True
    )

    # Return top 10 posts
    return recommended_posts[:10]

@app.route('/feed', methods=['GET'])
def feed():
    username = request.args.get('username')
    category_id = request.args.get('category_id')
    mood = request.args.get('mood')
    recommended_posts = recommend_posts(username, category_id, mood)
    return jsonify(recommended_posts)

if __name__ == '__main__':
    app.run(debug=True, port=5001,use_reloader=False)
