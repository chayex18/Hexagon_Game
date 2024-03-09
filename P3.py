"""
Hexagon Game with Minimax Algorithm
This Hexagon game's implementation, two players take turns adding edges to a hexagonal graph.
The main goal is to avoid creating triangles with the added edges. 
The AI player (Player 2) uses the minimax algorithm to make optimal moves.

"""
import networkx as nx  # Importing NetworkX library for graph manipulation
import matplotlib.pyplot as plt # Importing Matplotlib library for graph visualization

# Initialize the hexagonal graph
def buildGraph():
    global graph 
    graph = nx.Graph()  # Creating an empty graph
    graph.add_nodes_from([1, 2, 3, 4, 5, 6])   # Adding nodes to the graph
    global pos 
    pos = {1: (0, 1), 2: (1, 2), 3: (2, 1), 4: (2, -1), 5: (1, -2), 6: (0, -1)}
    
# Printing the graph with current state
def printGraph():
    # Drawing the graph with labels and node properties
    nx.draw(graph,pos, with_labels=True, node_color='green', node_size=500, font_size=12)
    # Drawing edges with different styles based on weight
    for u, v, d in graph.edges(data=True):
        if d['weight'] == 1:
            nx.draw_networkx_edges(graph, pos, edgelist=[(u, v)], width=4.0, alpha=0.5) # Solid edges
        else:
            nx.draw_networkx_edges(graph, pos, edgelist=[(u, v)], width=4.0, alpha=0.9, style='dashed') # Dashed edges
    plt.show(block = False)  # Displaying the graph without blocking the program execution
    input("Press enter to continue ") # Waiting for user input to continue

# Checking if a triangle is formed in the graph
def isTriangle(graph, weight):
    for u, v in graph.edges():
        if graph[u][v]['weight'] == weight:
            for w in graph.neighbors(v):
                if graph.has_edge(u, w) and graph[u][w]['weight'] == weight:
                    if graph.has_edge(w, u) and graph[w][u]['weight'] == weight:
                        if graph[u][v]['weight'] == graph[v][w]['weight'] == graph[w][u]['weight']:
                            return True
    return False
    
# Validate edge selection conditions
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
        
# Validate edge selection conditions for minimax algorithm    
def isCondition2(edge1, edge2):
    if ((edge1 < 1) or (edge1 > 6) or (edge2 < 1) or (edge2 > 6)):
        return False
    elif (edge1 == edge2):
        return False
    elif (graph.has_edge(edge1, edge2)):
        return False
    else:
        return True
        
# Player 1's turn
def player1():
    printGraph()
    edge1 = int(input("Enter First Edge: ")) 
    edge2 = int(input("Enter Second Edge: "))
    while isCondition(edge1, edge2) is False:
        edge1 = int(input("Enter First Edge: ")) 
        edge2 = int(input("Enter Second Edge: "))
    plt.close()
    graph.add_edge(edge1,edge2, weight = 1)
    printGraph()
    if isTriangle(graph, 1):
        print("Player 1 Created a Triangle. Player 1 Lost!")
        plt.show()
        return 0
    else:
        plt.close()
        player2()

# Player 2's turn using minimax algorithm
def player2():
    # Use minimax algorithm to choose the best move for player 2
    _, edge1, edge2 = minimax(graph, 0, 2, True)
    graph.add_edge(edge1, edge2, weight=0)
    printGraph()
    if isTriangle(graph, 0):
        print("Player 2 Created a Triangle. Player 2 Lost!")
        plt.show()
        return 0
    else:
        plt.close()
        player1()
# Evaluating the game state 
def evaluate_game_state(graph):
    if isTriangle(graph, 1):  # If player 1 forms a triangle, return a winning score
        return 1
    elif isTriangle(graph, 0):  # If player 2 forms a triangle, return a loosing score
        return -1
    else:
        return 0  # Game is ongoing 

# Implementing minimax algorithm for AI player

def minimax(graph, depth, player, is_maximizing_player):
    if depth == 3 or isTriangle(graph, 0) or isTriangle(graph, 1):  # Depth limit reached, evaluate the game state
        return evaluate_game_state(graph), None, None
    
    if is_maximizing_player:
        best_value = -10000 # Set toa large value (represents negative infinity)
        best_edge1 = None
        best_edge2 = None
        for edge1 in range(1, 7):
            for edge2 in range(edge1 + 1, 7):
                if isCondition2(edge1, edge2):
                    graph.add_edge(edge1, edge2, weight = 0 )
                    value, _, _ = minimax(graph, depth + 1, player, False)
                    if value > best_value:
                        best_value = value
                        best_edge1 = edge1
                        best_edge2 = edge2
                    graph.remove_edge(edge1, edge2)                    
        return best_value, best_edge1, best_edge2
    else:
        best_value = 10000
        best_edge1 = None
        best_edge2 = None
        for edge1 in range(1, 7):
            for edge2 in range(edge1 + 1, 7):
                if isCondition2(edge1, edge2):
                    graph.add_edge(edge1, edge2, weight = 0)
                    value, _, _ = minimax(graph, depth + 1, player, True)
                    if value < best_value:
                        best_value = value
                        best_edge1 = edge1
                        best_edge2 = edge2
                    graph.remove_edge(edge1, edge2)
        return best_value, best_edge1, best_edge2

# Prompt the user to select a player number and start the game
def getPrompt():
    while True:
        try:
            prompt = int(input("Please enter a player number (1 or 2): "))
            if prompt < 1 or prompt > 2:
                print("Please select either 1 or 2")
                continue
        except ValueError:
            print("Invalid input. Enter an integer (either 1 or 2)")
        else:
            return prompt

# Start the game based on the user's input
playerNum = getPrompt()
buildGraph()
if playerNum == 2:
    player1()
else:
    player2()
