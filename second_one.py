import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

responses = {
    'hello': 'Hi there! How can I help you today?',
    'hi': 'Hello! How can I assist you?',
    'hey': 'Hey! What’s up?',
    'good morning': 'Good morning! How’s your day going?',
    'good evening': 'Good evening! How can I make your evening better?',
    'how are you': 'I am good, thanks for asking!',
    'how are you doing': 'I’m doing great, thank you for asking!',
    'see you': 'See you later! Take care!',
    'good night': 'Good night! Sleep well!',
    'thank you': 'You’re welcome! Feel free to ask if you need anything else.',
    'thanks': 'No problem! Let me know if you need help with anything.',
    'sorry': 'No worries! How can I assist you?',
    'what is your name': 'I’m your friendly assistant bot! How can I help you?',
    'what can you do': 'I can answer your questions, help with tasks, or just chat with you!',
    'tell me a joke': 'Why don’t skeletons fight each other? They don’t have the guts!',
    'help': 'I’m here to assist you! What do you need help with?',
    'tell me more': 'I’d be happy to! What would you like to know more about?',
    'can you assist me': 'Of course! What can I help you with?',
    'who are you': 'I’m a bot created to help you with whatever you need!',
    'what time is it': 'I’m not sure about the exact time, but you can check the clock on your device.',
    'what’s up': 'Not much, just here to help! How can I assist you?',
    'how’s the weather': 'I don’t have the latest weather info, but you can check your local weather app or website.',
}

def tokenize_input(user_input):
    tokens = word_tokenize(user_input)
    return tokens

def stem_input(tokens):
    stemmer = PorterStemmer()
    stems = [stemmer.stem(token) for token in tokens ]
    return stems

def chatbot():
    print("Chatbot: Hi! say 'bye' if you want to end the chat.")
    while True:
        user_input = input('You: ').split()
        tokens = tokenize_input(user_input)
        stems = stem_input(tokens)

        stemmed_input = ' '.join(stems)

        if "bye" in stemmed_input:
            print('Chatbot: Bye!')
            break
        
        matched_response = None
        for pattern, response in response.items():
            if pattern in stemmed_input:
                matched_response = response
                break
        
        if matched_response:
            print(f'Chatbot: {matched_response}')
        else:
            print("Chatbot: Sorry, I am not able to answer this.")

