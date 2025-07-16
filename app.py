from flask import Flask, render_template, request
import requests
import base64
import random
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Simple lists of positive and negative words
POSITIVE_WORDS = ["happy", "good", "great", "awesome", "fantastic", "amazing", "wonderful", "joy"]
NEGATIVE_WORDS = ["sad", "bad", "terrible", "horrible", "awful", "cry", "angry"]

TENOR_API_KEY = os.getenv('TENOR_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meme', methods=['POST'])
def meme():
    user_input = request.form['user_input'].lower()

    try:
        # Fetch a random GIF from Tenor
        search_term = "positive vibes"
        limit = 100  # Fetch more results to get a better random selection
        
        url = f"https://tenor.googleapis.com/v2/search?q={search_term}&key={TENOR_API_KEY}&limit={limit}"
        
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        if data['results']:
            # Select a random GIF from the results
            random_gif = random.choice(data['results'])
            image_url = random_gif['media_formats']['gif']['url']
            
            # Fetch the GIF data
            gif_response = requests.get(image_url, stream=True)
            gif_response.raise_for_status()
            
            # Encode image in base64
            encoded_image = base64.b64encode(gif_response.content).decode('utf-8')
            meme_image = f"data:image/gif;base64,{encoded_image}"
        else:
            meme_image = ''
            meme_text = "Couldn't find any memes, sorry!"

        if user_input in POSITIVE_WORDS:
            meme_text = "Here's a positive meme to make your day even better!"
        elif user_input in NEGATIVE_WORDS:
            meme_text = "Sorry to hear that. Here's a funny meme to cheer you up!"
        else:
            meme_text = "Here is a meme for you!"

    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")
        meme_image = ''  # Set a default or empty image on error
        meme_text = "Sorry, we couldn't load a meme for you at the moment."

    return render_template('meme.html', meme_image=meme_image, meme_text=meme_text)

if __name__ == '__main__':
    app.run(debug=True)
