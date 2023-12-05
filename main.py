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
