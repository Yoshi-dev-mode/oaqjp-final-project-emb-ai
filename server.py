"""
Flask server for the Emotion Detection application.
"""

from flask import Flask
from flask import render_template
from flask import request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """Analyze the given text and return the emotion analysis."""
    res = request.args.get('textToAnalyze')
    emotion = emotion_detector(res)

    if emotion['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    statement = (
        f"For the given statement, the system response is "
        f"'anger': {emotion['anger']}, "
        f"'disgust': {emotion['disgust']}, "
        f"'fear': {emotion['fear']}, "
        f"'joy': {emotion['joy']} and "
        f"'sadness': {emotion['sadness']}. "
        f"The dominant emotion is {emotion['dominant_emotion']}."
    )
    return statement

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
