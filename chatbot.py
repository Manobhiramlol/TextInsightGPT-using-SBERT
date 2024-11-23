import spacy
import unicodedata
import re
import streamlit as st
from sentence_transformers import SentenceTransformer, util

# Preprocess the text
def clean_text(text):
    # Normalize Unicode characters
    text = unicodedata.normalize('NFKC', text)

    # Replace non-breaking or zero-width spaces with regular spaces
    text = text.replace('\u200a', ' ').replace('\u00a0', ' ')

    return text

# Load the SBERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load and clean the text file
with open('long-story.txt', encoding='utf-8') as f:
    text = f.read()

cleaned_text = clean_text(text)

# Define the regular expression to match titles and the content between them
pattern = r"\n\n([A-Z\s]+)\n([^\n]+(?:\n[^\n]+)*)"

# Use findall to capture all title-content pairs
sections = re.findall(pattern, cleaned_text)

# Store the sections in a dictionary with embeddings for content
sections_dict = {}
embeddings_dict = {}

for title, content in sections:
    # Clean the title and content by stripping unnecessary newlines
    cleaned_title = title.strip().lower()  # Convert the title to lowercase for case-insensitive matching
    cleaned_content = content.strip()
    
    # Create embeddings for each section content
    content_embedding = model.encode(cleaned_content, convert_to_tensor=True)
    
    sections_dict[cleaned_title] = cleaned_content
    embeddings_dict[cleaned_title] = content_embedding

# Function to retrieve content based on user input (semantic matching with SBERT)
def get_section(user_input):
    # Normalize user input to lowercase for matching
    user_input = user_input.lower()
    
    # Generate the embedding for the user input
    user_input_embedding = model.encode(user_input, convert_to_tensor=True)
    
    best_match = None
    best_score = -1

    # Iterate through the sections to find the best match based on cosine similarity
    for title, section_embedding in embeddings_dict.items():
        cosine_score = util.pytorch_cos_sim(user_input_embedding, section_embedding)[0][0].item()
        
        if cosine_score > best_score:
            best_score = cosine_score
            best_match = title

    # Return the best matching section
    if best_score > 0.5:  # You can adjust the threshold based on your needs
        return sections_dict[best_match]
    else:
        return "No matching section found."

# Streamlit UI
def chatbot_ui():
    st.title("Text-Based Chatbot")

    # Display instructions
    st.write("Ask the chatbot for specific sections from the document by typing keywords like 'productivity', 'life hacks', 'communication skills', 'skill development', 'personal development', 'goal setting' ")

    # Input field for the user
    user_input = st.text_input("Enter a keyword", "")

    # If the user enters a keyword, get the matching section and display it
    if user_input:
        section_content = get_section(user_input)
        st.write(section_content)

# Run the Streamlit app
if __name__ == "__main__":
    chatbot_ui()
