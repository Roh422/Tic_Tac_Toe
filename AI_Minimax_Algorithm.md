# Minimax Algorithm
## Introduction
The Minimax algorithm is a decision-making algorithm commonly used in two-player games, such as Tic Tac Toe, Chess, and Checkers. Its goal is to find the best possible move for the current player, assuming that the opponent also plays optimally.

## Explanation
The algorithm works by exploring all possible moves and their consequences, forming a tree-like structure called the game tree. It recursively evaluates each node in the tree, assigning a score to each possible move based on the outcome of the game. The scores are then propagated back up the tree to determine the best move for the current player.

## Working
1. Game Tree Generation:
At the root node of the game tree, the current state of the game is represented.
The algorithm generates all possible moves that the current player can make from the current state. Each move results in a new game state.
The algorithm continues this process recursively, generating the entire game tree until the game reaches a terminal state (win, lose, or draw).

2. Assigning Scores to Terminal States:
When a terminal state is reached (a state where the game is over), the algorithm assigns a score to that state.
For example, in Tic Tac Toe, a win for the current player is assigned a score of +1, a loss a score of -1, and a draw a score of 0.

3. Propagating Scores Up the Tree:

* As the algorithm evaluates the terminal states, it propagates the scores back up the tree to the root.
* If the current player is the maximizing player, it selects the highest score from its children nodes (representing its possible moves).
* If the current player is the minimizing player (opponent), it selects the lowest score from its children nodes (representing the opponent's best moves).

4. Selecting the Best Move:
Once the algorithm has propagated scores up to the root node, it selects the move that leads to the highest score if it is the maximizing player or the move that leads to the lowest score if it is the minimizing player

## Breadth-First Search (BFS) and Depth-First Search (DFS) Algorithms
Breadth-First Search (BFS) and Depth-First Search (DFS) are two fundamental search algorithms used to traverse and explore graph or tree structures.   
* BFS explores the graph in a level-by-level manner, visiting all the neighbors of a node before moving to the next level.
* DFS explores the graph by traversing as far as possible along each branch before backtracking.
