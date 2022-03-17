import unittest
import ast
from visast import generate

class TestVisAST(unittest.TestCase):
    def testGenerateFromURLOne(self):
        aSTScript = '''
""" helloworld.py
A simple Hello World python script.
Authors: Jesse Phillips <james@jamesphillipsuk.com>
"""


def main():
    """ main.  Our entrypoint for the script.
    """
    print("\\nHello, World!\\n")


if __name__ == "__main__":
    main()
'''
        aST = ast.parse(aSTScript)
        remoteAST = generate.fromURL("https://gist.githubusercontent.com/JamesPhillipsUK/f3498b07d94a5a4e4ea4d3060c0af907/raw/a8eca1ef2d096bb652b3a1009d3bcb0f09f31af5/helloworld.py")
        # self.assertEqual(remoteAST._fields, aST._fields, "Should generate an AST.")
        self.assertIsInstance(remoteAST, ast.AST, "generate.fromURL should generate an AST")
        # remoteIDs = []
        # localIDs = []
        # for node in ast.walk(aST):
        #     localIDs.append(str(node.__class__))
        # for node in ast.walk(remoteAST):
        #     remoteIDs.append(str(node.__class__))
        # i = 0
        # while i < len(localIDs):
        #     self.assertEqual(localIDs[i], remoteIDs[i], "Items in ASTs must match.")

if __name__ == "__main__":
    unittest.main()
