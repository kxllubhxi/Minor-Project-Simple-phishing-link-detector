# Phishing Website Detection

## Overview
This project is a web-based application designed to detect phishing URLs. It uses a Machine Learning model (Gradient Boosting Classifier) trained on various website features to classify a given URL as either "Safe" or "Not Safe".

The application is built using Python, Flask for the web interface, and Scikit-Learn for the machine learning model.

## How it Works
1. **URL Input**: The user enters a URL into the web interface.
2. **Feature Extraction**: The application uses the `FeatureExtraction` class (`feature.py`) to extract 30 different features from the provided URL. These features include:
    - URL structure (e.g., length, use of IP address, presence of '@' symbol, prefix/suffix).
    - Domain characteristics (e.g., domain registration length, age of domain, subdomains).
    - HTML and JavaScript features (e.g., iframe redirection, disabling right-click, links in `<script>` tags, server form handlers).
    - Network features (e.g., DNS records, website traffic ranking, Google index status).
3. **Prediction**: The extracted features are passed as a vector to the pre-trained Machine Learning model (`newmodel.pkl`).
4. **Result**: The model predicts whether the URL is likely to be a phishing website or not. The prediction is combined with some rule-based checks (like URL shortener detection in `convert.py`) to provide a final "Safe" or "Not Safe" verdict back to the user on the web interface.

## Project Structure
- `app.py`: The main Flask application that handles routing, requests, and model prediction.
- `feature.py`: Contains the `FeatureExtraction` class which implements the logic for extracting 30 specific features from a URL using libraries like `BeautifulSoup`, `requests`, and `whois`.
- `convert.py`: Contains utility functions to process the model's prediction and handle edge cases like URL shorteners.
- `newmodel.pkl`: The serialized (pickled) pre-trained machine learning model used for making predictions.
- `requirements.txt`: Lists the Python dependencies required to run the project.
- `static/` & `templates/`: Directories containing the HTML, CSS, and other static assets for the visual web interface.

## Setup and Installation
1. Ensure you have Python installed on your system.
2. Navigate to the project directory.
3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open your web browser and go to `http://127.0.0.1:5001` (or the port specified in your terminal) to access the application.
