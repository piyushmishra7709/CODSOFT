import random

def chatbot_response(user_input):
    greetings = ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Hey! How can I help you?"]
    farewells = ["Goodbye! Have a great day!", "See you later! Take care!", "Bye! Have a wonderful day!"]
    inquiries = ["I'm just a bot, but I'm here to help you!", "Doing great! How about you?", "I'm functioning optimally! How can I assist you?"]

    user_input = user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return random.choice(greetings)
    elif 'bye' in user_input or 'goodbye' in user_input:
        return random.choice(farewells)
    elif 'how are you' in user_input:
        return random.choice(inquiries)
    elif 'name' in user_input:
        return "I'm your friendly neighborhood chatbot, at your service!"
    elif 'help' in user_input:
        return "I'm here to help! You can ask me about our services, opening hours, or any other questions you might have."
    elif 'hours' in user_input:
        return "We are open from 9 AM to 6 PM, Monday to Friday."
    elif 'services' in user_input:
        return "We offer a variety of services including customer support, product information, and more. How can I assist you today?"
    elif 'joke' in user_input:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you get when you cross a snowman and a vampire? Frostbite!"
        ]
        return random.choice(jokes)
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

# Testing the chatbot with specific inputs to match the desired output
print(chatbot_response("Hi there!"))
print(chatbot_response("How are you?"))
print(chatbot_response("Bye"))
print(chatbot_response("What's your name?"))
print(chatbot_response("Tell me a joke"))
print(chatbot_response("What are your services?"))
