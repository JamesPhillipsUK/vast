"""visualise.py Visualises an Abstract Syntax Tree

VisAST - Building and visualising Abstract Syntax Trees for Python code.

Authors: Jesse Phillips <james@jamesphillipsuk.com>

"""

import ast
import sys
import networkx as nx
import EoN
import matplotlib.pyplot as plt


def graph(aST: ast):
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
                if (childLabel == "Load"
                   or childLabel == "Store"
                   or childLabel == "Del"):
                    if hasattr(node, "id"):
                        nodeLabel = str(node.id)
                        labelDictionary[nodeID] = nodeLabel

            GRAPH.add_edge(nodeID, childNodeID)
            edges.append([nodeID, childNodeID])

    # Make the graph look like a tree using hierarchy_pos.
    pos = EoN.hierarchy_pos(GRAPH, rootNodeID)
    nx.draw_networkx_nodes(GRAPH, pos=pos, alpha=0.6)
    nx.draw_networkx_edges(GRAPH, pos=pos, alpha=0.5)
    nx.draw_networkx_labels(GRAPH, pos=pos, labels=labelDictionary)

    plt.title("Abstract Syntax Tree:")
    plt.tight_layout(pad=0)
    plt.axis("off")
    plt.show()  # Tada!
