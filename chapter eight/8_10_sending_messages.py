message_list = ["Hello", "Goodbye", "See you later"]
finished_list = []
def send_messages(words, finished_words):
    """Print messages from a list and update them into a finished messages list"""
    while words:
        current_word = words.pop()
        print(f"Current message: {current_word}")
        finished_words.append(current_word)
    print(f"Finished words: {finished_words}")

        

send_messages(message_list, finished_list)