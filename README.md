# TextInsightGPT-using-SBERT
TextInsightGPT leverages SBERT (Sentence-BERT) to provide advanced text processing and analysis capabilities. This combination makes it ideal for:

1. Semantic Text Similarity: Compare sentences or texts for similarity.
2. Semantic Search: Retrieve relevant documents or information based on user queries.
3. Text Clustering and Categorization: Group or categorize similar texts into themes.
4. Sentiment Analysis: Understand positive or negative sentiments in text data.
5. Text Summarization: Generate concise summaries of lengthy content.
6. Question Answering: Build systems that answer questions using textual data.
7. Anomaly Detection: Identify unusual or spam-like text.
8. Cross-Lingual Applications: Work with multiple languages for search and analysis.
9. Knowledge Extraction: Extract meaningful insights from unstructured text.
10. E-Learning Tools: Enhance learning with smarter tools like automatic grading or question generation.



# Why SBERT?

1. Fast & Scalable: Ideal for tasks like semantic search and clustering.
2. Accurate: Captures the meaning of sentences effectively.


# Why We Used text-preprocessing.ipynb 

The text-preprocessing.ipynb notebook plays a crucial role in preparing raw text data for use in the TextInsightGPT using SBERT project.



Purpose of text-preprocessing.ipynb:

1. Clean Raw Text Data:
   Removes noise such as special characters, numbers, and extra whitespaces.
   Ensures the input data is consistent and ready for analysis.

2. Tokenization:

   Splits text into words or sentences, making it easier for SBERT to process.

3. Stopword Removal:

   Removes common but uninformative words (e.g., "and," "is," "the") to focus on meaningful content.

4. Stemming and Lemmatization:

   Reduces words to their base or root forms (e.g., "running" → "run") for better semantic understanding.

5. Text Normalization:

   Converts all text to lowercase to ensure uniformity.
   Handles contractions (e.g., "don't" → "do not").

6. Data Preparation for Embedding:

   Prepares the processed text data for generating embeddings using SBERT.

7. Improves Model Performance:

   Reduces noise and irrelevant information, leading to better results in tasks like similarity matching, clustering, and search.

 This file is not used by the chatbot, it is written just to show the basic functionalities.
 long-story.txt: The document containing the text to be processed. The chatbot extracts and processes sections from this file. 
 chatbot.py: The main Python script that runs the chatbot. It includes: Text cleaning and preprocessing. Regular expressions to extract titles and their corresponding content. 
 Streamlit-based UI for user interaction.
 ![Image Alt](https://github.com/Manobhiramlol/TextInsightGPT-using-SBERT/blob/a3ba3b0670d340a11ba8c0f8707aa65052800c9c/Screenshot%202024-11-23%20175624.png)
 ![Image Alt](https://github.com/Manobhiramlol/TextInsightGPT-using-SBERT/blob/a3ba3b0670d340a11ba8c0f8707aa65052800c9c/Screenshot%202024-11-23%20175641.png)
 ![Image Alt](https://github.com/Manobhiramlol/TextInsightGPT-using-SBERT/blob/a3ba3b0670d340a11ba8c0f8707aa65052800c9c/Screenshot%202024-11-23%20175718.png)
 
 
