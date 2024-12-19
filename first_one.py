import re

responses = {
    r"hi|hello|hey": "Hello! How can I help you?",
    r"how are you": "I'm just a bot, but I'm doing fine. How can I assist you?",
    r"what is your name": "I'm ChatBot, your virtual assistant.",
    r"bye|goodbye": "Goodbye! Have a great day!"
}

def math_response(user_input):
    for pattern, response in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    
    return "I am sorry, I am unable to answer your question"

def chatbot():
    print("Chatbot: Hello, type 'bye' to exit!")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        
        response = math_response(user_input)
        print(f'Chatbot: {response}')

chatbot()