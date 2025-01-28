import graphviz

def nested_dict_to_dot(nested_dict, parent=None, graph=None):
    """
    Convert a nested dictionary into DOT code.

    :param nested_dict: The nested dictionary to convert.
    :param parent: The parent node for the current recursion.
    :param graph: The graphviz.Digraph object.
    :return: The graphviz.Digraph object.
    """
    if graph is None:
        graph = graphviz.Digraph(format='png')
        graph.attr('node', shape='box')  # Set nodes to rectangular boxes
        graph.attr('graph', rankdir='TB', splines='ortho')  # Ensure tree layout with orthogonal lines

    for key, value in nested_dict.items():
        node_name = f"{key}"
        graph.node(node_name)

        if parent is not None:
            graph.edge(parent, node_name)  # Add arrowheads to edges

        if isinstance(value, dict):
            # Recurse into sub-dictionary
            nested_dict_to_dot(value, parent=node_name, graph=graph)
        else:
            # Add leaf nodes
            leaf_name = f"{key}_{value}"
            graph.node(leaf_name, label=str(value))
            graph.edge(node_name, leaf_name)

    return graph

# Example nested dictionary
data = {
    'A': {
        'B': {
            'D': {},
            'E': {
                'H': {}
            }
        },
        'C': {
            'F': {},
            'G': {}
        }
    }
}

# Convert nested dictionary to DOT and generate the tree diagram
graph = nested_dict_to_dot(data)
graph.render('tree_diagram', cleanup=True)  # Outputs tree_diagram.png

print("Tree diagram saved as 'tree_diagram.png'")
