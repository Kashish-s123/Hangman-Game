print("========== Simple ChatBot ==========")
print("Type 'bye' to exit the chat")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hii!")

    elif user == "how are you":
        print("Bot: I am fine. How are you?")

    elif user == "what is your name":
        print("Bot: My name is Kashish Bot.")

    elif user == "who made you":
        print("Bot: Kashish created me using Python.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")
