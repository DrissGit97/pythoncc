#Adding defaults
def make_shirt(size="large", msg= "I love Python"):
    """A function that accepts a size and a message that should be printed on the shirt"""
    print(f"\nThis shirt is size {size.lower()} and its message is {msg}")

make_shirt("A", "I am an A size")

make_shirt(msg="I am a B size", size= "B")

make_shirt()

make_shirt(size="medium")

make_shirt("Any other size", "Any other message")