# app.py

from flask import Flask, render_template, request
import recommendation_engine as rec

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        genres_input = request.form.getlist('genres')
        recommendations = rec.recommend_for_new_user(genres_input)

    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
