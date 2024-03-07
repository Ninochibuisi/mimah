import random

class MimahChatbot:
    def __init__(self):
        self.responses = {
            "How are you?": {
                "Fine": 0.5,
                "Good": 0.3,
                "Not bad": 0.2
            },
            "What's your name?": {
                "My name is Mimah": 0.6,
                "You can call me Mimah": 0.4
            },
            "What's the weather like today?": {
                "Sunny": 0.4,
                "Cloudy": 0.3,
                "Rainy": 0.2,
                "Snowy": 0.1
            },
            "What's your favorite color?": {
                "Blue": 0.5,
                "Red": 0.3,
                "Green": 0.2
            },
            "Who created you?": {
                "A programmer": 0.5,
                "I was created by Chibuisi Michael at Nino Tech Enterprises": 0.5
            }
        }
        self.intro_message = "Mimah is always here to help."

    def get_response(self, user_input):
        if "how are you" in user_input.lower():
            response_options = list(self.responses["How are you?"].keys())
            probabilities = list(self.responses["How are you?"].values())
            response = random.choices(response_options, weights=probabilities, k=1)[0]
        elif "exit" in user_input.lower():
            response = "Goodbye!"
        else:
            response = self.intro_message
        return response

if __name__ == "__main__":
    chatbot = MimahChatbot()
    print("Welcome to Mimah Chatbot!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print("Mimah:", response)
        if "exit" in user_input.lower():
            break

# Copyright and trademark notice
print("\n© 2022 Nino Tech Enterprises. All rights reserved. Mimah™ is a trademark of Nino Tech Enterprises.")
