# Alternate_Medicines_Generator

## Introduction
The Alternative Medicine Generator is a Flask-based web application that helps users find alternative medicines based on composition similarity. The system takes a medicine name as input, analyzes its composition, and recommends alternatives with similar active ingredients. This tool is particularly useful for users looking for cost-effective, locally available, or generic medicine substitutes.

## Features
- Medicine Search: Users can enter a medicine name to find alternatives.
- Composition Analysis: Uses Natural Language Processing (NLP) techniques to analyze and compare compositions.
- Cosine Similarity Matching: Finds alternative medicines based on textual similarity in compositions.
- Interactive UI: Simple and user-friendly interface for easy access to information.
- Flask API: Backend powered by Flask to handle requests and provide recommendations dynamically.

## Technologies Used
* Flask - Web framework for handling API requests.
* Python - Core programming language.
* scikit-learn - Used for CountVectorizer and Nearest Neighbors similarity computations.
* HTML, CSS - For front-end development.
* Pandas & NumPy - For dataset handling and preprocessing.

## Approach
1. Data Preparation
- The dataset contains medicine names and their compositions.
- Data is preprocessed using Pandas to clean and normalize text.

2. Feature Extraction
- CountVectorizer is used to tokenize and vectorize medicine compositions.
- Term Frequency-Inverse Document Frequency (TF-IDF) weighting can be optionally applied.

3. Similarity Computation
- The system calculates cosine similarity between medicine composition vectors.
- Nearest Neighbors model is used to find the most similar medicines.

4. Flask API Development
- The backend is developed using Flask, where:
  - Users input a medicine name.
  - The system processes the request and finds alternatives.
  - The results are displayed on the front-end.

5. Frontend Integration
- HTML, CSS are used to create a responsive UI.
- AJAX is used to fetch results dynamically from the Flask backend.

## Installation and Setup
### Prerequisites
Ensure you have Python installed. You can install dependencies using:  >> pip install -r requirements.txt

### Running the Application
Run the app.py file using the command: >> python app.py
Then open the http address provided in your browser.

## Usage
1. Open the application in a web browser.
2. Enter a medicine name in the search box.
3. Click the "Find Alternatives" button.
4. View the list of alternative medicines and their compositions.

## Future Enhancements
- Expand dataset with more medicines and more detailed compositions.
- Improve NLP processing for more accurate similarity matching.
- Implement user feedback and rating system for better recommendations.
- Add the feature to check reactions between any medicines provided.
- Deploy the application online for public access.

## Conclusion
The Alternative Medicine Generator provides a practical and efficient way to find medicine substitutes based on composition similarity. By leveraging NLP and machine learning techniques, the system ensures accurate and reliable recommendations. This project has the potential to make medicine more accessible and affordable to users. Future improvements will focus on refining similarity algorithms, expanding the dataset, and enhancing the user experience. Overall, this tool serves as a valuable resource for healthcare accessibility and informed decision-making.

