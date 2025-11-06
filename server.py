import requests
import json
from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def sent_analyzer():
    text_to_analyse = request.arg.get("textToAnalyze")
    
    result = emotion_detector(text_to_analyse)
    anger = result.get('anger', 0.0)
    disgust = result.get('disgust', 0.0)
    fear = result.get('fear', 0.0)
    joy = result.get('joy', 0.0)
    sadness = result.get('sadness', 0.0)
    dominant = result.get('dominant_emotion', 'joy')

    resp_text = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)