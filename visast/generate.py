"""generator.py Generates an Abstract Syntax Tree

VAST - Building and visualising Abstract Syntax Trees for Python code.

Authors: Jesse Phillips <james@jamesphillipsuk.com>

"""
import ast
import urllib.request


def fromURL(uRL: str):
    """This method, given a python file's URL, generates an abstract
    syntax tree for it.

    Args:
        uRL (string): The URL.

    Returns:
        AST: The abstract syntax tree.

    """
    if uRL:
        try:
            fileString = urllib.request.urlopen(uRL).read().decode()
        except Exception as E:
            raise E
        try:
            aST = ast.parse(fileString)
        except SyntaxError as S:
            raise S
        return aST
    raise ValueError("Cannot generate AST from URL if none is provided.")


def fromPath(path: str):
    """This method, given a python file's path, generates an abstract
    syntax tree for it.

    Args:
        path (string): The filepath.

    Returns:
        AST: The abstract syntax tree.

    """
    with open(path) as file:
        fileString = file.read()
    if fileString:
        aST = ast.parse(fileString)
        return aST
    else:
        raise ValueError("Cannot make an AST from an empty file.")


def fromString(codeString: str):
    """This method, given a string of Python, generates an abstract
    syntax tree for it.

    Args:
        codeString (string): The code to analyse.

    Returns:
        AST: The abstract syntax tree.

    """
    if codeString:
        aST = ast.parse(codeString)
        return aST
    else:
        raise ValueError("Cannot make an AST from an empty string.")
