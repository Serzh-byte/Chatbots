from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import json
import random
import nltk
from sklearn.preprocessing import LabelEncoder

ignore_words = ["?", "!", ".", ",", "'s", "a", "the", "in", "on", "at", "to", "and", "is", "for", "of"]

# Download necessary NLTK resources
nltk.download("punkt")
nltk.download("wordnet")

# Load intents file
with open("third_one/intents.json") as file:
    intents = json.load(file)

# Initialize variables for training
training_sentences = []
training_labels = []
classes = []
words = []

# Tokenize and preprocess data
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        training_sentences.append(pattern)
        training_labels.append(intent["intent"])
    
    if intent["intent"] not in classes:
        classes.append(intent["intent"])

# Stem and lemmatize words
words = [nltk.WordNetLemmatizer().lemmatize(w.lower()) for w in words if w not in ignore_words]

# Sort and remove duplicates
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Prepare the data for training
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(training_sentences)

# Create and fit the LabelEncoder for training labels
label_encoder = LabelEncoder()
y_train = label_encoder.fit_transform(training_labels)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Function to predict the intent of a given input text
def predict_intent(text):
    """
    Predicts the intent of the given text.
    """
    text_vector = vectorizer.transform([text])  # Convert the input text to a numerical vector using TF-IDF
    prediction = model.predict(text_vector)  # Predict the label for the input text
    intent = label_encoder.inverse_transform(prediction)  # Convert the numeric label back to the string label
    return intent[0]  # Return the predicted intent as a string

# Chatbot loop
def chatbot():
    """
    Simple chatbot that interacts with the user.
    """
    print("ChatBot: Hello! How can I help you?")
    while True:
        user_input = input("You: ").strip()  # Read user input and remove any extra spaces
        if user_input.lower() == "bye":  # Check if the user wants to exit
            print("ChatBot: Goodbye!")
            break

        intent = predict_intent(user_input)  # Predict the intent of the user's input

        # Find and display the corresponding response
        for i in intents['intents']:
            if i['intent'] == intent:
                print(f"ChatBot: {random.choice(i['responses'])}")  # Pick a random response from the intent's responses
                break

chatbot()