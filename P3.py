# Yeixon Chacon U:24830068
# Elias Hurtando U:00042456
# This program written in python is an Hexagonal Game played against an AI that follows the minimax algorithm with a depth of 3.
# The player will be prompted if he/she wants to play first or second by inputting the number 1 or 2:
# - If select to play as player 1 the program makes the first move.
# - If select to play as player 2 the user makes the first move.

import networkx as nx               # Use of networkx to create graph used in game
import matplotlib.pyplot as plt     # Use of matplotlib.pyplot to visually show the game and the current state

def buildGraph():       # Function to build the graph
    global graph        # Declare graph as global to be used in the whole program
    graph = nx.Graph()  # Build graph using networkx
    graph.add_nodes_from([1, 2, 3, 4, 5, 6])    # Add six nodes for the game
    global pos      # Create pos to represent position of nodes as global
    pos = {1: (0, 1), 2: (1, 2), 3: (2, 1), 4: (2, -1), 5: (1, -2), 6: (0, -1)} # Set position of nodes

def printGraph():   # Function to print the Graph
    plt.close()     # Close any visualization if opened 
    nx.draw(graph,pos, with_labels=True, node_color='green', node_size=500, font_size=12)   # Draw the nodes with specific characteristics
    for u, v, d in graph.edges(data=True):  # For edge drawing
        if playerNum == 2:  # If player number input is 2
            if d['weight'] == 1:    # The user will control the solid line
                nx.draw_networkx_edges(graph, pos, edgelist=[(u, v)], width=4.0, alpha=0.5)
            else:                   # And the AI will be presented as the dashed line
                nx.draw_networkx_edges(graph, pos, edgelist=[(u, v)], width=4.0, alpha=0.9, style='dashed')
        else:   # Else if the player input is 1
            if d['weight'] == 1:    # The user will control de dashed line 
                nx.draw_networkx_edges(graph, pos, edgelist=[(u, v)], width=4.0, alpha=0.9, style='dashed')
            else:                   # And the AI will be presented as the solid line
                nx.draw_networkx_edges(graph, pos, edgelist=[(u, v)], width=4.0, alpha=0.5)
    plt.show(block = False) # Show visual representation of graph drawned. Used block = false to make program keep running after graph is displayed

def isTriangle(graph, weight):  # Function to check if a triangle was made in the graph
    for u, v in graph.edges():  # Check for all edges in graph
        if graph[u][v]['weight'] == weight: # If the edges have the weight desired
            for w in graph.neighbors(v):    # Check for its neighbors and repeat process:
                if graph.has_edge(u, w) and graph[u][w]['weight'] == weight:
                    if graph.has_edge(w, u) and graph[w][u]['weight'] == weight:
                        if graph[u][v]['weight'] == graph[v][w]['weight'] == graph[w][u]['weight']:
                            return True # If all three neighbors are the same return True, which means a triangle was formed
    return False    # Else return false

def isCondition(edge1, edge2):  # Validate edge selection conditions
    if (edge1 == None):
        return False
    elif ((edge1 < 1) or (edge1 > 6) or (edge2 < 1) or (edge2 > 6)):    
        print("Please choose a node between 1 and 6")   # Print message for users
        return False
    elif (edge1 == edge2):
        print("You can't create a line to the same node")   # Print message for users
        return False
    elif (graph.has_edge(edge1, edge2)):
        print("Please select a different line that is not taken")   # Print message for users
        return False
    else:
        return True # If conditions passed return True
    
def isCondition2(edge1, edge2): # Validate edge selection conditions for minimax algorithm. This will not print any message
    if ((edge1 < 1) or (edge1 > 6) or (edge2 < 1) or (edge2 > 6)):
        return False
    elif (edge1 == edge2):
        return False
    elif (graph.has_edge(edge1, edge2)):
        return False
    else:
        return True

# Player's 1 Turn (User)
def player1():
    printGraph()    # Print Graph
    # Set edges to None
    edge1 = None 
    edge2 = None 
    while isCondition(edge1, edge2) is False:   # Until conditions are not met
        edge1 = int(input("Enter First Edge: "))    # Print to enter First Edge
        edge2 = int(input("Enter Second Edge: "))   # Print to enter Second Edge
    graph.add_edge(edge1,edge2, weight = 1) # Add them to the graph
    printGraph()    # Print the graph
    if isTriangle(graph, 1):    # Check if change made a triangle
        print(f"Player {playerNum2} Created a Triangle. Player {playerNum2} Lost!")    # In case it did show message that player lost the game
        plt.show()  # Show final state of game
        return 0    # Finish Program
    else:   # If game has not finished
        input("Press enter to continue ")   # Enter to continue will allow user to control when to go to the next state
        plt.close() # Close window
        player2()   # Go to player two

def player2():  # Player 2's turn using minimax algorithm
    _, edge1, edge2 = minimax(graph, 0, True)   # Return the most accurate edge1 and edge2
    graph.add_edge(edge1, edge2, weight=0)  # Add it to the graph
    printGraph()    
    if isTriangle(graph, 0):    # If triangle was made
        print(f"Player {playerNum} Created a Triangle. Player {playerNum} Lost!")   # show message that player lost the game
        plt.show()  # Show final state of game
        return 0    # Finish Program
    else:   # If game has not finished
        plt.close() # Close window
        player1()   # Go to player one

def evaluate_game_state(graph): # Evaluating the game state 
    if isTriangle(graph, 1):  # If player 1 forms a triangle, return a winning score
        return 1
    elif isTriangle(graph, 0):  # If player 2 (AI) forms a triangle, return a loosing score
        return -1
    else:
        return 0  # Game is ongoing 

def minimax(graph, depth, is_maximizing_player): # Function with minimax algorithm
    if depth == 3 or isTriangle(graph, 0) or isTriangle(graph, 1):  # If Depth limit reached or a triangle is found evaluate the game state
        return evaluate_game_state(graph), None, None   # Return the game state - The other nones represent edges that are not used here.
    
    if is_maximizing_player:    # If looking for mac
        best_value = float('-inf') # Set to a large value (represents negative infinity)
        best_edge1 = None
        best_edge2 = None
        for edge1 in range(1, 7):   # Look for all possible combinations
            for edge2 in range(edge1 + 1, 7):
                if isCondition2(edge1, edge2):  # If conditions are met
                    graph.add_edge(edge1, edge2, weight = 0 )   # Add values to edge
                    value, _, _ = minimax(graph, depth + 1, False)  # Call minimax to return value of nodes
                    if value > best_value:  # If value is greater than best value (for first iteration negative infinite)
                        best_value = value  # Best value equals value
                        best_edge1 = edge1  # Best_edge1 equals edge1
                        best_edge2 = edge2  # Best_edge2 equals edge2
                    graph.remove_edge(edge1, edge2) # Remove the edge from graph                    
        return best_value, best_edge1, best_edge2   # Return values
    else:   # Else looking for min
        best_value = float('inf') # Set to a large value (represents infinity)
        best_edge1 = None
        best_edge2 = None
        for edge1 in range(1, 7):   # Look for all possible combinations
            for edge2 in range(edge1 + 1, 7):
                if isCondition2(edge1, edge2):  # If conditions are met
                    graph.add_edge(edge1, edge2, weight = 0)    # Add the edge 
                    value, _, _ = minimax(graph, depth + 1, True) # # Call minimax to return value of nodes
                    if value < best_value:  # If value is smeller than best value (for first iteration positive infinite)
                        best_value = value  # Best value equals value
                        best_edge1 = edge1  # Best_edge1 equals edge1
                        best_edge2 = edge2  # Best_edge2 equals edge2
                    graph.remove_edge(edge1, edge2) # Remove the edge from graph  
        return best_value, best_edge1, best_edge2   # Return values

# Prompt the user to select a player number and start the game
def getPrompt():
    while True: # While it is true
        try:    # Use try to catch if string is inputed
            prompt = int(input("Please enter a player number (1 or 2): ")) # Get input
            if prompt < 1 or prompt > 2:    # Check if prompts are in correct range
                print("Please select either 1 or 2")
                continue
        except ValueError:  # If string found print failure message
            print("Invalid input. Enter an integer (either 1 or 2)")
        else:
            return prompt   # Else return prompt

def main(): # Main function
    global playerNum    # Set playerNum and playerNum2 as global
    global playerNum2
    playerNum = getPrompt() # Set playerNum to getPrompt
    buildGraph()    # Build graph
    if playerNum == 2:  # If playerNum is two
        playerNum2 = 1
        player1()   # player 1 plays first
    else:   # Else
        playerNum2 = 2
        player2()   # player 2 plays first

if __name__ == "__main__":  # Call main function
    main()
