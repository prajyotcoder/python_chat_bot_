"""
Chatbot Demonstration Script
Author: Prajyot Talkar
Date: [24/11/2024]

Description:
------------
This Python script demonstrates how a simple chatbot works, including its ability to:
1. Respond with predefined answers for basic queries.
2. Learn new responses from user input dynamically.
3. Save its learned responses for persistence across sessions using a JSON file.

The chatbot starts with a set of default responses for common queries like "hello" or "how are you." 
When it encounters an unknown input, it asks the user to teach it the appropriate response and saves this
new knowledge for future use.

Purpose:
--------
This code is designed for educational purposes, showcasing:
1. The basic structure of a chatbot.
2. How you can train and update the chatbot's knowledge in real-time.
3. Persistent storage of learned responses.

Key Features:
-------------
1. Predefined responses for commonly used inputs.
2. Dynamic learning for unrecognized inputs.
3. Persistent memory using a JSON file to store learned responses.
4. A fallback response mechanism when the chatbot doesn't understand the input.

Usage:
------
- Run the script in a Python environment.
- Type your messages to interact with the chatbot.
- To quit the chatbot, type 'exit'.
- If the chatbot doesn't know how to respond, provide a response when prompted to teach it.

License:
--------
This code is free to use, modify, and distribute. If you use or modify this code, please give credit to the author.

Disclaimer:
-----------
This is a simple demonstration of chatbot functionality. It is not intended for production use or complex 
natural language understanding tasks.
"""

import json

# File to store chatbot memory
DATA_FILE = "chatbot_memory.json"

# Predefined responses
DEFAULT_RESPONSES = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a program, but I'm functioning as expected!",
    "what is your name": "I'm a simple chatbot. What's yours?",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!"
}

# Default fallback response
FALLBACK_RESPONSE = "I'm not sure how to respond to that. Can you teach me?"

def load_memory():
    """Load chatbot memory from file or initialize it."""
    try:
        with open(DATA_FILE, "r") as file:
            memory = json.load(file)
    except FileNotFoundError:
        memory = {}  # Initialize with an empty dictionary if file not found
    return memory

def save_memory(memory):
    """Save chatbot memory to file."""
    with open(DATA_FILE, "w") as file:
        json.dump(memory, file)

def get_response(user_input, memory):
    """Get the chatbot's response."""
    # Check in user-learned memory
    if user_input in memory:
        return memory[user_input]
    # Check in default responses
    elif user_input in DEFAULT_RESPONSES:
        return DEFAULT_RESPONSES[user_input]
    else:
        return FALLBACK_RESPONSE

def main():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'exit' to quit.")
    memory = load_memory()

    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            save_memory(memory)
            break

        response = get_response(user_input, memory)
        print(f"Chatbot: {response}")

        # Teach new response if chatbot doesn't recognize input
        if response == FALLBACK_RESPONSE:
            new_response = input("You can teach me by typing the correct response: ").strip()
            memory[user_input] = new_response
            print("Chatbot: Got it! I'll remember that.")

if __name__ == "__main__":
    main()
