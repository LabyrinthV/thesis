import streamlit as st
import gzip
st.title('Hello, Streamlit!')
st.write('This is a simple Streamlit app running in a Docker container.')

import pickle

with open('./afreeca_model.pkl', 'rb') as f:
    netflix_model = pickle.load(f)

# Create a function that takes in a model and a list of features and returns a prediction
def predict(model, features):
    return model.predict(features)

# Bitrate
bitrate = st.slider('Downlink Bitrate', 0, 500000, 50000)

make_prediction = st.checkbox('Make Prediction')

if make_prediction:
    # Create a list of features
    features = [[bitrate]]

    # Call the predict function with the model and the features
    prediction = predict(netflix_model, features)
    # If the prediction is 1 it is an inlier, if it is -1 it is an outlier
    if prediction == 1:
        print(prediction)
        st.write(f'The predicted downlink throughput is predicted to be an inlier')
    else:
        print(prediction)
        st.write(f'The predicted downlink throughput is predicted to be an outlier')
