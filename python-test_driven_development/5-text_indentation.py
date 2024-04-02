#!/usr/bin/python3
"""This function prints two new lines after one of the characters . ? :"""
def text_identation(text):
    """Actual function for putting the lines after . ? :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for jmp in ".?:":
        txt = (jmp + "\n\n").join([line.strip(" ") for line in text.split(jmp)])
        print(txt, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_identation.txt")