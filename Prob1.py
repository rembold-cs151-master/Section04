
import random

def generate_password(length, characters):
    """
    Generates a password of the desired length with the provided characters

    Args:
        length (int): the length of the password in number of characters
        characters (str): the string of possible characters to use in the password
    Returns:
        (str): the desired password
    """
    # Your code here!




if __name__ == '__main__':

    import string

    chars = string.ascii_letters
    print(f"Simple password:  {generate_password(5, chars)}")
    chars += string.digits
    print(f"Medium password:  {generate_password(10, chars)}")
    chars += string.punctuation
    print(f"Complex password: {generate_password(15, chars)}")
