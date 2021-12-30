"""vast.py

Building and visualising Abstract Syntax Trees for Python code.

Authors: Jesse Phillips <james@jamesphillipsuk.com>

"""
import ast
import sys
import networkx as nx
import EoN
import matplotlib.pyplot as plt


class Vast:

    def __init__(self, path: str = ""):
        if path:
            aST = self.generateAST(path)  # Get python from a URL
            self.visualiseASTGraph(aST)

    def generateAST(self, path: str):
        """This method, given a python file's path, generates an abstract
        syntax tree for it.

        Args:
            path (string): The filepath.

        Returns:
            AST: The abstract syntax tree.

        """
        with open(path) as file:
            fileString = file.read()
        aST = ast.parse(fileString)
        return aST

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
                    labelDictionary[childNodeID] = childLabel

                GRAPH.add_edge(nodeID, childNodeID)
                edges.append([nodeID, childNodeID])

        # Make the graph look like a tree using hierarchy_pos.
        pos = EoN.hierarchy_pos(GRAPH, rootNodeID)
        nx.draw(GRAPH, pos=pos, labels=labelDictionary, with_labels=True)
        plt.show()  # Tada!

    def main(self, argv):
        """Our entrypoint for the script.

        Args:
            argv(list): Command-line arguments.
                Called like so: ">python vast.py ./helloworld.py"

        """
        if len(argv) > 1:
            aST = self.generateAST(argv[1])  # Get python from a URL
            self.visualiseASTGraph(aST)
        else:
            print("No filepath given.")


if __name__ == "__main__":
    vast = Vast()
    vast.main(sys.argv)
