"""
ChatGPT
https://chatgpt.com/share/6aeff665-14b4-83e8-917d-46d7bf0151d0

Prompt: how to use networkx in python?

"""

import networkx as nx

def count_nodes(g: nx.Graph) -> int:
    """Count the number of nodes in a graph.
    Args:
        g (nx.Graph): A NetworkX graph object.
    Returns:
        int: The number of nodes in the graph."""
    return g.number_of_nodes()

if __name__ == "__main__":
    # Example usage
    g = nx.Graph()
    g.add_edges_from([(1,2), (1,3), (2,4), (3,4)])
    print("Number of nodes in the graph:", count_nodes(g))