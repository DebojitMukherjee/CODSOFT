import random

def developed_chatbot():
    print("Hello! I'm a developed chatbot. What is your name?")
    user_name = input("You: ").strip()

    print(f"Chatbot: Nice to meet you, {user_name}! Ask me anything or type 'exit' to quit.")
    print("-" * 50)

    while True:
        # Lowercase the input so typing 'HELLO' or 'hello' behaves the same
        user_input = input(f"{user_name}: ").lower().strip()
        
        # 1. Exit Rule
        if user_input in ['exit', 'quit', 'bye']:
            print(f"Chatbot: Goodbye, {user_name}! It was nice talking to you.")
            break  # <-- This MUST be indented inside the 'if' block!
            
        # 2. Greeting Rule
        elif 'hello' in user_input or 'hi' in user_input:
            print(f"Chatbot: Hello, {user_name}! How can I assist you today?")
            
        # 3. Well-being Rule
        elif 'how are you' in user_input or 'how is it going' in user_input:
            statuses = [
                "I am running perfectly. Thanks for asking!",
                "Great! Ready to process your commands.",
                "Doing well, just hanging out in your terminal."
            ]
            print(f"Chatbot: {random.choice(statuses)}")
            
        # 4. Identity Rule
        elif 'your name' in user_input or 'who are you' in user_input:
            print(f"Chatbot: My name is Chatbot, and I was built to help {user_name}.")
            
        # 5. Fallback Rule (if none of the if-elif statements match)
        else:
            fallbacks = [
                "I didn't quite catch that. Could you try phrasing it differently?",
                "My rules don't cover that request yet.",
                "I'm a simple bot, I don't understand that command."
            ]
            print(f"Chatbot: {random.choice(fallbacks)}")

if __name__ == "__main__":
    developed_chatbot()