import networkx as nx
import matplotlib.pyplot as plt

def visualize_workflow(steps):
    G = nx.DiGraph()

    for i in range(len(steps)-1):
        G.add_edge(steps[i], steps[i+1])

    nx.draw(G, with_labels=True)
    plt.title("SentinelFlow Workflow Graph")
    plt.show()
