def auto_response(user_input):
    if "hello" in user_input.lower():
        return "Hi there! How can I help you?"
    elif "how are you" in user_input.lower():
        return "I'm just a computer program, but thanks for asking!"
    elif "python" in user_input.lower():
        return "Python is a powerful programming language!"
    else:
        return "I'm not sure how to respond to that."

# Get user input
user_input = input("Type something: ")

# Get auto response
response = auto_response(user_input)

# Print the response
print(response)


# USEDJK
# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions
import numpy as np

# Load the pre-trained InceptionV3 model
model = InceptionV3(weights='imagenet')

# Load and preprocess an example image
img_path = 'path/to/your/image.jpg'
img = image.load_img(img_path, target_size=(299, 299))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# Make predictions
predictions = model.predict(img_array)

# Decode and print the top-3 predicted classes
decoded_predictions = decode_predictions(predictions, top=3)[0]
print("Predictions:")
for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print(f"{i + 1}: {label} ({score:.2f})")
