


oaqjp-final-project-emb-ai
## Project Description
This application analyzes user-provided text snippets to evaluate and extract emotional sentiments using an integrated Watson NLP library connection. It ranks primary indicators across multiple emotion keys and returns a designated dominant emotion. The backend logic is packaged as an independent module and served to clients via a responsive web portal deployed through the Flask framework.

## Project Architecture & Layout
* **`EmotionDetection/`**: Core application module handling the Watson NLP endpoint integrations.
* **`templates/`**: Frontend user interface elements and document layouts.
* **`server.py`**: Web gateway script orchestrating route handlers and application requests.
* **`test_emotion_detection.py`**: Automated unit testing assertion suite.
* **`setup.py`**: Local project packaging configuration script.

## Core Features Implemented
* Dynamic Watson NLP Emotion Predict API processing.
* Formatted key-value metric data parsing.
* Local Python package distribution framework.
* Automated unit testing assertions.
* Flask server deployment on port 5000.
* Graceful input verification error handling.
* Clean structural formatting verified via Pylint.
