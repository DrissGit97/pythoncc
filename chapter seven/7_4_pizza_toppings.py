prompt = "What pizza topping do you want? "
prompt += "\nEnter 'quit' to end the program "

message = " "
while message !="quit":
    message= input(prompt)
    if message !="quit":
        print(f"We'll add {message} to your pizza!")