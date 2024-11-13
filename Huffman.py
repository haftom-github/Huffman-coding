from collections import defaultdict

def generateWeightDict(filename, enc='utf-8'):
    """
    Builds a weight dictionary for each character in a text file.

    This function reads the content of a file and calculates the relative frequency (weight) 
    of each character. The resulting dictionary holds each character as a key with its 
    weight as the value, where the weight is the character's frequency divided by the 
    total number of characters.

    :param filename: str - The path to the text file to analyze.
    :param enc: str - The encoding of the file (default is 'utf-8').
    :return: dict - A dictionary with characters as keys and their weight (frequency) as values.
    """
    weights = defaultdict(int)
    weights['end'] = 1
    total_characters = 0

    # Read the file and count character frequencies
    with open(filename, 'rt', encoding=enc) as file:
        while chunk := file.read(100):
            total_characters += len(chunk)
            for ch in chunk:
                weights[ch] += 1

    # Use dictionary comprehension to calculate the weight of each character
    return {ch: count / total_characters for ch, count in weights.items()}