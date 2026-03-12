# Fake News Detector using Gemini AI

## Overview

The Fake News Detector is a web application that analyzes news content
and determines whether the information is real or fake using Google
Gemini AI. The application is built with Python and Flask and provides
an easy interface for users to check the credibility of news articles.

## Features

-   Detects whether news content is Real or Fake
-   Uses Gemini AI API for intelligent analysis
-   Provides confidence score and explanation
-   Performs sentiment and bias analysis
-   Simple web interface for user input

## Technologies Used

-   Python
-   Flask
-   HTML
-   CSS
-   Google Gemini AI API

## Project Structure

fake-news-detector │ ├── app.py ├── list_models.py ├── templates │ └──
index.html ├── static │ └── style.css └── README.md

## How to Run the Project

### 1. Install Dependencies

pip install flask pip install google-generativeai

### 2. Add Gemini API Key

Create a .env file and add: GEMINI_API_KEY=your_api_key_here

### 3. Run the Application

python app.py

## Future Improvements

-   Add news URL analysis
-   Store results in database
-   Improve user interface
-   Support multiple languages

## Author

Developed as a project to demonstrate AI integration with web
applications for misinformation detection.
