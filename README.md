# Hexagon Game
## Table of Contents
- Usage
- API Reference
- Compile
- Contributors

## Usage
In our hexagon game’s implementation, two players take turns adding edges to a hexagonal graph. The game progresses with alternating moves between Player 1 (user) and Player 2 (AI), avoiding forming triangles with their edges. The AI player utilizes the minimax algorithm to make strategic moves based on future game states. The game ends when one of the players completes a triangle, and the other player wins.

## API Reference
- ### buildGraph()
Function builds six nodes graph using networkx.
- ### printGraph()
Function prints the graph using matplotlib.
- ### isTriangle(graph, weight)
Function checks if a triangle was made in the graph and which player did it according the weight.
- ### isCondition(edge1, edge2)
Function validate edge selection conditions but it prints message for users if input is wrong.
- ### isCondition2(edge1, edge2)
Function validate edge selection conditions for minimax algorithm. This will not print any message.
- ### player1()
Function prompts user to input edges to be connected and check if game is done.
- ### player2()
Function works with AI using minimax algorithm to play a turn and check if game is done.
- ### evaluate_game_state(graph)
Function evaluate the game of the state and it will return '1' if user makes a triangle and '-1' if AI makes a triangle.
- ### minimax(graph, depth, is_maximizing_player)
Function shows minimax algorithm that looks at different moves one by one, going deeper into each possibility, and then chooses the move that seems best. 
- ### getPrompt()
Function to Select which player is going to be played against.
- ### main()
Main function where game is played
  
## Compile
In order to use our implementation, please follow the instructions provided below:
1. Download Python in terminal: https://www.python.org/downloads/
2. Install library networkx: https://pypi.org/project/networkx/
   ![Screenshot 2024-03-06 at 11 14 59 PM](https://github.com/chayex18/Hexagonal_Game/assets/133992144/ea7699c6-f404-41de-af1c-307dd6bda496)
3. Install library matplotlib: https://pypi.org/project/matplotlib/
   ![Screenshot 2024-03-09 at 12 19 35 PM](https://github.com/chayex18/Hexagonal_Game/assets/133992144/5417075e-a5ff-476c-9b3e-dc10803cd3a0)
4. After installing python and the mentioned libraries, open the folder where Assignment3.py is located by using Terminal.
5. Run the program by typing the following line in terminal:
<img width="169" alt="Screenshot 2024-03-09 at 12 21 53 PM" src="https://github.com/chayex18/Hexagonal_Game/assets/133992144/f7940614-9eec-4e8c-9f59-c8e28fb6ae59">
 
6. Select the player and enjoy the game. 
## Contributors
- Yeixon Chacon - U24830068
- Elias Hurtado - U00042456
  
