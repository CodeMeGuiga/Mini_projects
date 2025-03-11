# NLP Model Documentation

## Overview
This project focuses on Natural Language Processing (NLP) to analyze and process drug-related text data. The dataset used contains information about drugs and their uses.

## Dataset
- **File:** `drugs_data.csv`
- **Columns Used:** `drug_name`, `uses`
- **Preprocessing:**
  - Data cleaning and filtering.
  - Text length analysis.
  - Exporting cleaned data.

## Model Training
- Uses **TF-IDF Vectorization** for feature extraction.
- Implements a **Machine Learning model** (possibly Logistic Regression or Naive Bayes) for classification.
- Trains and evaluates the model using standard NLP techniques.

## Dependencies
Install required libraries using:
```bash
pip install pandas scikit-learn nltk
```

## How to Run
1. Load the dataset and preprocess text data.
2. Train the NLP model using the provided Jupyter Notebook (`NLP.ipynb`).
3. Evaluate the model's performance.

## Results
- Displays average, max, and min length of drug descriptions.
- Outputs classification results based on text features.

## Repository Structure
```
├── NLP.ipynb          # Jupyter Notebook with code & analysis
├── cleaned.csv        # Processed dataset
├── README.md          # Documentation
```