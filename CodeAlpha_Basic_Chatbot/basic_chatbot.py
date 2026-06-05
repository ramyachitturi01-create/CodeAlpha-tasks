def greet():
    print("\nChatBot : Hello! Nice to meet you.")
    print("ChatBot : Type 'help' to see available commands.")
    print("ChatBot : Type 'bye' to exit.\n")


def show_help():
    print("\nAvailable Commands:")
    print("hello")
    print("hi")
    print("how are you")
    print("what is your name")
    print("who created you")
    print("python")
    print("course")
    print("internship")
    print("time")
    print("date")
    print("help")
    print("bye\n")


greet()

while True:

    user_input = input("You : ").lower()

    if user_input == "hello":
        print("ChatBot : Hello! How can I help you today?")

    elif user_input == "hi":
        print("ChatBot : Hi! Welcome.")

    elif user_input == "how are you":
        print("ChatBot : I am fine. Thanks for asking.")

    elif user_input == "what is your name":
        print("ChatBot : My name is Python ChatBot.")

    elif user_input == "who created you":
        print("ChatBot : I was created using Python programming.")

    elif user_input == "python":
        print("ChatBot : Python is a popular programming language.")

    elif user_input == "course":
        print("ChatBot : This internship helps improve programming skills.")

    elif user_input == "internship":
        print("ChatBot : Complete all assigned tasks and submit them.")

    elif user_input == "time":
        print("ChatBot : I cannot show live time, but you can check your system clock.")

    elif user_input == "date":
        print("ChatBot : I cannot show live date, but you can check your system calendar.")

    elif user_input == "help":
        show_help()

    elif user_input == "bye":
        print("ChatBot : Goodbye! Have a nice day.")
        break

    else:
        print("ChatBot : Sorry, I don't understand that command.")