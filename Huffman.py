from collections import defaultdict
from treee import Tree

def generateTree(dct):
    """
    Generates a Huffman tree based on the provided weight dictionary.

    This function takes a weight dictionary where each character's weight represents its frequency 
    or probability, and builds the corresponding Huffman tree. The function repeatedly combines the 
    two smallest weight trees from the forest until only one tree remains, which becomes the final 
    Huffman tree.

    :param dct: dict - A dictionary where keys are characters, and values are their corresponding weights 
                 (e.g., {'A': 0.5, 'B': 0.2, 'C': 0.3}).
    :return: Tree - The root of the generated Huffman tree, which represents the entire tree structure.
    """
    forest = []
    for key in dct:
        forest.append(Tree(key, dct[key]))

    while len(forest) > 1:
        # find the two smallest weight trees from the forest
        smallWI = 0
        for i in range(len(forest)):                                            #choose the Tree with the smallest weight
            if forest[i].getweight() < forest[smallWI].getweight():
                smallWI = i
        right=forest.pop(smallWI)
        smallWI=0
        for i in range(len(forest)):                                            #choose the second smmallest weight tree to be combined with the above Tree to one tree
            if forest[i].getweight() < forest[smallWI].getweight():
                smallWI = i
        left = forest.pop(smallWI)
        weightsum = left.getweight() + right.getweight()
        t = Tree(None, weightsum).concat(left, to='left').concat(right, to='right')         #concatinating the two smallest weight trees into one
        forest.append(t)
    return forest[0]

def gen(root, st,dct):
    if root.item != None:
        dct[root.item] = st
        return
    gen(root.left, st + '0',dct)
    gen(root.right, st + '1',dct)

def generateDict(hT):
    """
    Generates a dictionary of Huffman codes for each character in the Huffman tree.

    :param hT: HuffmanTree - The Huffman tree object containing the `head` node which is the root of the tree.
    :return: dict - A dictionary where each character from the Huffman tree is a key, 
                     and its Huffman code (binary representation) is the corresponding value (e.g., {'A': '0100101'}).
    """

    dct=dict()
    gen(hT.head, '', dct)
    return dct

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