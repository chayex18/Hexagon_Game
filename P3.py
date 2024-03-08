import networkx as nx
import matplotlib.pyplot as plt

def buildGraph():
    global graph 
    graph = nx.Graph()
    graph.add_nodes_from([1, 2, 3, 4, 5, 6])
    global pos 
    pos = {1: (0, 1), 2: (1, 2), 3: (2, 1), 4: (2, -1), 5: (1, -2), 6: (0, -1)}


def printGraph():
    nx.draw(graph,pos, with_labels=True, node_color='green', node_size=500, font_size=12)
    for u, v, d in graph.edges(data=True):
        if d['weight'] == 1:
            nx.draw_networkx_edges(graph, pos, edgelist=[(u, v)], width=4.0, alpha=0.5)
        else:
            nx.draw_networkx_edges(graph, pos, edgelist=[(u, v)], width=4.0, alpha=0.9, style='dashed')
    plt.show(block = False)
    input("Press enter to continue ")

def isTriangle(graph, weight):
    for u, v in graph.edges():
        if graph[u][v]['weight'] == weight:
            for w in graph.neighbors(v):
                if graph.has_edge(u, w) and graph[u][w]['weight'] == weight:
                    if graph.has_edge(w, u) and graph[w][u]['weight'] == weight:
                        if graph[u][v]['weight'] == graph[v][w]['weight'] == graph[w][u]['weight']:
                            #print("Triangle found: ", u, v, w)
                            return True
    return False

def player1():
    plt.close()
    edge1 = int(input("Enter First Edge: ")) 
    edge2 = int(input("Enter Second Edge: "))
    while isCondition(edge1, edge2) is False:
        edge1 = int(input("Enter First Edge: ")) 
        edge2 = int(input("Enter Second Edge: "))
    graph.add_edge(edge1,edge2, weight = 1)
    printGraph()
    if isTriangle(graph, 1):
        print("Player 1 Won")
        return 0
    else:
        plt.close()
        player2()

def isCondition(edge1, edge2):
    if ((edge1 < 1) or (edge1 > 6) or (edge2 < 1) or (edge2 > 6)):
        print("Please choose a node between 1 and 6")
        return False
    elif (edge1 == edge2):
        print("You can't create a line to the same node")
        return False
    elif (graph.has_edge(edge1, edge2)):
        print("Please select a different line that is not taken")
        return False
    else:
        return True

def player2():
    edge1 = int(input("Enter First Edge: ")) 
    edge2 = int(input("Enter Second Edge: "))
    while isCondition(edge1, edge2) is False:
        edge1 = int(input("Enter First Edge: ")) 
        edge2 = int(input("Enter Second Edge: "))
    graph.add_edge(edge1,edge2, weight = 0)
    printGraph()
    if isTriangle(graph, 0):
        print("Player 2 Won")
        return 0
    else:
        plt.close()
        player1()

buildGraph()
printGraph()
player1()
