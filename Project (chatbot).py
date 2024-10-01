def chatbot():
    print("Hello! I am a simple chatbot. You can ask me a few questions.")
    print("Type 'exit' to end the chat.")

    while True:
        question = input("Ask your question: ").lower()

        if "exit" in question:
            print("Goodbye! Have a great day.")
            break
        elif "your name" in question:
            print("I am Chatbot 2.0, created to answer basic questions.")
        elif "your age" in question:
            print("I am a program, so I don't have an age, but I was written just now!")
        elif "pi value" in question:
            pi_value = 3.14159
            print(f"The value of Pi is {pi_value}.")
        elif "sum" in question:
            try:
                num1 = int(input("Enter the first integer: "))
                num2 = int(input("Enter the second integer: "))
                total = num1 + num2 
                print(f"The sum of {num1} and {num2} is {total}.")
            except ValueError:
                print("Please enter valid integers.")
        elif "temperature" in question:
            try:
                temp_celsius = float(input("Enter the temperature in Celsius: "))
                temp_fahrenheit = (temp_celsius * 9/5) + 32
                print(f"The temperature in Fahrenheit is {temp_fahrenheit}.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("I don't understand that question. Try asking something else.")

chatbot()
