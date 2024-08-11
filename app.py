import streamlit as st

st.title('Hello, Streamlit!')
st.write('This is a simple Streamlit app running in a Docker container.')

# Import the classifiers from the dl_classifier.pkl file
import pickle
with open('dl_classifier.pkl', 'rb') as f:
    dl_classifiers = pickle.load(f)

# Import the ul classifiers from the ul_classifier.pkl file
with open('ul_classifier.pkl', 'rb') as f:
    ul_classifiers = pickle.load(f)

# Create a function that takes in a model and a list of features and returns a prediction
def predict(model, features):
    return model.predict(features)
