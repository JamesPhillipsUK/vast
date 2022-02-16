"""vast.py

Building and visualising Abstract Syntax Trees for Python code.

Authors: Jesse Phillips <james@jamesphillipsuk.com>

"""
import ast
import sys
import networkx as nx
import EoN
import matplotlib.pyplot as plt
import urllib.request


class Vast:

    def __init__(self, path: str = ""):
        """Constructor.  If a filepath is provided, automatically generates and
        visualises the AST for that filepath.

        Args:
            path (string): The filepath.

        """
        if path:
            aST = self.generateASTFromPath(path)  # Get python
            self.visualiseASTGraph(aST)

    def generateASTFromURL(self, uRL: str):
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

    def generateASTFromPath(self, path: str):
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

    def generateAST(self, path: str):
        """DEPRECATED.This method, given a python file's path, generates an
        abstract syntax tree for it.

        Args:
            path (string): The filepath.

        Returns:
            AST: The abstract syntax tree.

        """
        print("The generateAST method is deprecated and will be removed.")
        print("Defaulting to generateASTFromPath(path: str).")
        return self.generateASTFromPath(path)

    def generateASTFromString(self, codeString: str):
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

    def visualiseASTGraph(self, aST: ast):
        """Builds a visualisation of the provided AST.

        Args:
            aST (AST): The abstract syntax tree.

        """
        GRAPH = nx.DiGraph()
        rootNodeID = "noRoot"
        edges = []
        labelDictionary = {}

        # Walk the tree, breadth-first, noting all edges.
        for node in ast.walk(aST):
            nodeID = str(node.__class__) + str(id(node))  # Unique name
            nodeLabel = str(node.__class__).split("ast.")[1].split("'>")[0]
            if nodeLabel == "Constant":
                nodeLabel += " " + str(node.value)
            elif nodeLabel == "FunctionDef":
                nodeLabel += " " + str(node.name)
            labelDictionary[nodeID] = nodeLabel

            if rootNodeID == "noRoot":
                rootNodeID = nodeID

            for child in ast.iter_child_nodes(node):
                childNodeID = str(child.__class__) + str(id(child))
                for edge in edges:
                    if edge[1] == childNodeID:
                        childNodeID += str(1)  # IDs aren't unique.  Fix.

                # If child is at the bottom of the tree, it won't get walked.
                # Label it manually.
                if labelDictionary.get(childNodeID) is None:
                    childLabel = str(child.__class__
                                     ).split("t.")[1].split("'>")[0]
                    if childLabel == "Constant":
                        childLabel += " " + str(child.value)

                    if (childLabel == "Load"
                       or childLabel == "Store"
                       or childLabel == "Del"):
                        nodeLabel = str(node.id)
                        labelDictionary[nodeID] = nodeLabel
                    else:
                        labelDictionary[childNodeID] = childLabel
                        GRAPH.add_edge(nodeID, childNodeID)
                        edges.append([nodeID, childNodeID])
                else:
                    GRAPH.add_edge(nodeID, childNodeID)
                    edges.append([nodeID, childNodeID])

        # Make the graph look like a tree using hierarchy_pos.
        pos = EoN.hierarchy_pos(GRAPH, rootNodeID)
        nx.draw_networkx_nodes(GRAPH, pos=pos, alpha=0.6)
        nx.draw_networkx_edges(GRAPH, pos=pos, alpha=0.5)
        nx.draw_networkx_labels(GRAPH, pos=pos, labels=labelDictionary)

        plt.tight_layout(pad=0)
        plt.axis("off")
        plt.show()  # Tada!

    def main(self, argv):
        """Our entrypoint for the script.

        Args:
            argv(list): Command-line arguments.
                Called like so: ">python vast.py ./helloworld.py"

        """
        if len(argv) > 1:
            aST = self.generateASTFromPath(argv[1])  # Get python from a URL
            self.visualiseASTGraph(aST)
        else:
            print("No filepath given.")


if __name__ == "__main__":
    vast = Vast()
    vast.main(sys.argv)
