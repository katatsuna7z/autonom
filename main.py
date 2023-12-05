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


import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions
import numpy as np

model = InceptionV3(weights='imagenet')

img_path = 'data/autonom/v1/us.jpg'
img = image.load_img(img_path, target_size=(299, 299))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

predictions = model.predict(img_array)

decoded_predictions = decode_predictions(predictions, top=3)[0]
print("Predictions:")
for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print(f"{i + 1}: {label} ({score:.2f})")
