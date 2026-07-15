"""
Emotion Detection module using the Watson NLP API service.
Provides analysis of input text to extract emotional scores.
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes input text using Watson NLP API and returns formatted emotional metrics.
    Handles blank input errors gracefully.
    """
    # Task 7: Error handling for blank or whitespace-only inputs
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://skills.network'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers, timeout=10)
    
    # Task 7: Handling unexpected API status code errors (like 400 Bad Request)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    formatted_response = json.loads(response.text)
    
    emotions = formatted_response['emotionPredictions']['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    emotion_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    emotion_dict['dominant_emotion'] = dominant_emotion
    
    return emotion_dict
