"""
ChatGPT
https://chatgpt.com/share/6aeff665-14b4-83e8-917d-46d7bf0151d0

Prompt: how to count degree in graph by networkx?

Prompt: how to use for loop for graph?

"""
import networkx as nx

def degree_check(g: nx.Graph, threshold: int = 5) -> int:
    """Count the number of nodes in a graph with a degree greater than a specified threshold.
    Args:
        g (nx.Graph): A NetworkX graph object.
        threshold (int): The degree threshold to compare against. Default is 5.
    Returns:
        int: The number of nodes with a degree greater than the threshold."""
    counter: int = 0
    for _, degree in g.degree():
        if degree > threshold:
            counter += 1
    return counter

if __name__ == "__main__":
    # Example usage
    g = nx.Graph()
    g.add_edges_from([(1,2), (1,3), (2,4), (3,4), (4,5), (5,6), (6,7), (1,4),(1,5), (1,6),(1,7),(2,3), (2,5), (3,6), (4,7)])
    threshold_value = 5
    print(f"Number of nodes with degree greater than {threshold_value}:", degree_check(g, threshold_value))
        
