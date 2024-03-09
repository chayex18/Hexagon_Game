# Hexagonal_Game

In our hexagon game’s implementation, two players take turns adding edges to a hexagonal graph. The game progresses with alternating moves between Player 1 (user) and Player 2 (AI), avoiding forming triangles with their edges. The AI player utilizes the minimax algorithm to make strategic moves based on future game states. The game ends when one of the players completes a triangle, and the other player wins. The following is our code structure:  

 

1. Graph Initialization: we initialize the hexagonal graph and assign initial positions for the nodes. 

 

2. Graph Visualization: our program provides a function to visualize the current state of the graph using Matplotlib and NetworkX. 

 

3. Winning Condition check: we implement two functions, isTriangle() and evaluate_game_state(), to check for winning conditions. isTriangle() examines if a triangle is formed with the newly added edge, while evaluate_game_state() assesses the game state to determine if a player has won. 

  

4. Player Moves: two functions, player1() and player2(), enable players to make their moves. Player 1 interacts with the user to input edge selections, while Player 2 uses the minimax algorithm to choose the best move. 

  

5. Minimax Algorithm: our AI player's decision-making process lies in the minimax algorithm, which explores potential future game states and selects the optimal move for the AI player. The algorithm looks at different moves one by one, going deeper into each possibility, and then chooses the move that seems best. 

 

6. Input Handling: the user can select a player number (1 or 2) and then initiates the game accordingly.

In order to use our implementation, please follow the instructions provided below.

1. Download Visual Studio Code: https://code.visualstudio.com/
2. Install library networkx: https://pypi.org/project/networkx/ 
3. Install library matplotlib: https://pypi.org/project/matplotlib/
4. After installing Visual Studio Code and the mentioned libraries, open the file p3.py in this folder.
5. Run the program. 
6. Select the player and enjoy the game. 
