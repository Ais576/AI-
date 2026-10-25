import re

def chatbot(msg):
    msg = msg.lower()

    if re.search(r"\b(hi|hello|hey)\b", msg):
        return "Hello! How are you?"
    elif "name" in msg:
        return "I am a simple chatbot."
    elif "how are you" in msg:
        return "I am fine. Thank you!"
    elif "bye" in msg:
        return "Goodbye!"

    return "Sorry, I don't understand."

while True:
    msg = input("You: ")
    if msg.lower() == "bye":
        print("Bot: Goodbye!")
        break
    print("Bot:", chatbot(msg))
