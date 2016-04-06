## Topic 3: Single agent search in Pacman

### Introduction

Pacman is hungry but tired. He knows there is food around (he can smell
it), but how can he get to the food as efficiently as possible?

In this project, we have a simple Pacman environment in which there are
no ghosts and only a single food pellet. Your Pacman agent will find
paths through this maze world to reach a particular location (where the
food is). You will build general search algorithms and apply them to
Pacman scenarios.

The code for this project consists of several Python files, some of
which you will need to read and understand in order to complete the
assignment, and some of which you can ignore.

#### Files you'll edit and submit

* `search.py` where all of your search algorithms will reside.
* `searchAgents.py` where all of your search-based agents will reside.

#### Files you might want to look at

* `pacman.py`, the main file that runs Pacman games. This file describes a Pacman
GameState type, which you use in this project.

* `game.py`, the logic behind how the Pacman world works. This file describes several
supporting types like AgentState, Agent, Direction, and Grid.

* `util.py`, useful data structures for implementing search algorithms.

### Welcome to Pacman

After downloading the code, you should be able to play a
game of Pacman by typing the following at the command line:

```
python pacman.py
```

**Note:** see the information in the Python tutorial for how to to use
the command-line to execute these files. Alternatively, you can execute
them directly from PyCharm by using the menu option `Run -> Run...`.

Pacman lives in a shiny blue world of twisting corridors and tasty round
treats. Navigating this world efficiently will be Pacman's first step in
mastering his domain.

The simplest agent in `searchAgents.py` is called the
`GoWestAgent`, which always goes West (a trivial reflex
agent). This agent can only be successful in very simple and special
worlds:

```
python pacman.py --layout testMaze --pacman GoWestAgent
```

**Note**: again this is the command-line way to run the program.
When running from PyCharm you will enter the
options in PyCharm's interpreter window as explained in the Python tutorial.
The options are the bits after the `.py`, in this case
`--layout testMaze --pacman GoWestAgent`.

But, things already get ugly for this agent when turning is required:

```
python pacman.py --layout tinyMaze --pacman GoWestAgent
```

If pacman gets stuck, you can exit the game by typing CTRL-c into your
terminal. Note that `pacman.py` supports a number of
parameters (options) that can each be expressed in a long way (e.g.,
`--layout`) or a short way (e.g., `-l`). You can see
the list of all options and their default values via:

```
python pacman.py -h
```

Also, all of the commands that appear in this topic also appear in
[commands.txt](commands.txt), for easy copying and pasting.

### Finding a Fixed Food Dot using Search Algorithms

In `searchAgents.py`, you'll find a fully implemented
`SearchAgent`, which plans out a path through Pacman's world
and then executes that path step-by-step. The search algorithms for
planning a path are not implemented -- that's your job. As you work
through the following questions, you might need to refer to the
[glossary of objects in the code](#object-glossary). First, test that the
`SearchAgent` is working correctly by running:

```
python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
```

The command above tells the `SearchAgent` to use
`tinyMazeSearch` as its search algorithm, which is implemented
in `search.py`. Pacman should navigate the maze successfully.

Now it's time to write full-fledged generic search functions to help
Pacman plan routes! Pseudocode for the search algorithms you'll write
can be found in the lecture slides and *Poole & Mackworth*. Remember that a
search node must contain not only a state but also the information
necessary to reconstruct the path (plan) which gets to that state.

**Note:** All of your search functions need to return a list of
*actions* that will lead the agent from the start to the goal. These
actions all have to be legal moves (valid directions, no moving through
walls).

*Hint:* Each algorithm is very similar. Algorithms for DFS, BFS, UCS and
A\* differ only in the details of how the fringe is managed. So,
concentrate on getting DFS right and the rest should be relatively
straightforward. Indeed, one possible implementation requires only a
single generic search method which is configured with an
algorithm-specific queuing strategy by a parameter (but your implementation need not
be of this form to receive full credit).

*Hint:* Make sure to check out the `Stack`, `Queue` and
`PriorityQueue` types provided to you in `util.py`!

### Assignment 1 (for submission)

Implement the depth-first search (DFS) algorithm in
the `depthFirstSearch` function in `search.py`. To
make your algorithm *complete*, write the graph search version of DFS,
which avoids expanding any already visited states (*P&M* section 3.7.1).

Your code should quickly find a solution for:

```
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
```

The Pacman board will show an overlay of the states explored, and the
order in which they were explored (brighter red means earlier
exploration). Is the exploration order what you would have expected?
Does Pacman actually go to all the explored squares on his way to the
goal?

*Hint:* If you use a `Stack` as your data structure, the
solution found by your DFS algorithm for `mediumMaze` should
have a length of 130 (provided you push successors onto the fringe in
the order provided by `getSuccessor`s; you might get 244 if you push them
in the reverse order). Is this a least cost solution? If not, think
about what depth-first search is doing wrong.

### Assignment 2 (for submission)

Implement the breadth-first search (BFS) algorithm in
the `breadthFirstSearch` function in `search.py`.
Again, write a graph search algorithm that avoids expanding any already
visited states. Test your code the same way you did for depth-first
search.

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```

Does BFS find a least cost solution? If not, check your implementation.

*Hint:* If Pacman moves too slowly for you, try the command-line option `--frameTime 0`.

**Note:** If you've written your search code generically, your code should
work equally well for the eight-puzzle search problem without any
changes.

```
python eightpuzzle.py
```

### Run configuration arguments

Tired of entering the command line arguments
(like `bigMaze -p SearchAgent -a fn=bfs -z .5`)
over and over again? There is an easier,
faster way to do this. We can tell PyCharm to always run our program
with these arguments.

To do this, go to the menu at the top; `Run -> Edit Configurations...`.
The settings for the current default configuration
(which is run when you click the green arrow) are shown. In the 'Script
parameters' field, enter the arguments you like (without `python
pacman.py`).

Now, each time you hit the green arrow button, or the debug button, the
arguments will automatically be entered. Don't forget to change the
arguments when you get to another part of the assignment!

### Varying the Cost Function

While BFS will find a fewest-actions path to the goal, we might want to
find paths that are "best" in other senses. Consider
`mediumDottedMaze` and `mediumScaryMaze`. By
changing the cost function, we can encourage Pacman to find different
paths. For example, we can charge more for dangerous steps in
ghost-ridden areas or less for steps in food-rich areas, and a rational
Pacman agent should adjust its behavior in response.

### Assignment 3 (for submission)

Implement the uniform-cost graph search algorithm in
the `uniformCostSearch` function in `search.py`. We
encourage you to look through `util.py` for some data
structures that may be useful in your implementation. You should now
observe successful behavior in all three of the following layouts, where
the agents below are all UCS agents that differ only in the cost
function they use (the agents and cost functions are written for you):

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```

**Note:** You should get very low and very high path costs for the
`StayEastSearchAgent` and `StayWestSearchAgent`
respectively, due to their exponential cost functions (see
`searchAgents.py` for details).


### Assignment 4 (for submission)

Implement A\* graph search in the empty function
`aStarSearch` in `search.py`. A\* takes a heuristic
function as an argument. Heuristics take two arguments: a state in the
search problem (the main argument), and the problem itself (for
reference information). The `nullHeuristic` heuristic function
in `search.py` is a trivial example.

You can test your A\* implementation on the original problem of finding
a path through a maze to a fixed position using the Manhattan distance
heuristic (implemented already as `manhattanHeuristic` in
`searchAgents.py`).

```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

You should see that A\* finds the optimal solution slightly faster than
uniform cost search (about 549 vs. 620 search nodes expanded in our
implementation, but ties in priority may make your numbers differ
slightly). What happens on `openMaze` for the various search
strategies?

The real power of A\* will only be apparent with more challenging search
problems, in particular when more than one goal (i.e, food pellet) has
to be reached. That will be the topic for next week's practical
sessions.

### Changing the representation

The Pacman world is full of corridors. Clearly it's stupid for Pacman to
go partway down a corridor and then turn around (when there are no
ghosts). However, the search methods used so far all check if turning
around is a reasonable option after every step down the corridor (even
if the cycle avoidance mechanism ensures that they do not actually do
turn around). Potentially, a lot of effort can be saved by
re-representing the problem in such a way that a single action is moving
the whole way down a corridor rather than just moving one cell onwards.
Replacing a sequence of actions by a single action in this way is a form
of problem abstraction, which is commonly used to speed up search - in
particular in computer games, where the graph of cross-roads and moves
between them is called the *waypoint graph*.

### Bonus assignment (for submission)

Implement the missing code in the
`CrossroadSearchAgent` in `searchAgents.py`, so that
one action is a move between crossroads in the map (i.e. points where
Pacman has more than 2 legal moves available).

### Object Glossary

Here's a glossary of the key objects in the code base related to search
problems, for your reference:

- `SearchProblem` (`search.py`)

   A SearchProblem is an abstract object that represents the state
    space, successor function, costs, and goal state of a problem. You
    will interact with any SearchProblem only through the methods
    defined at the top of `search.py`

- `PositionSearchProblem` (`searchAgents.py`)

	A specific type of SearchProblem that you will be working with ---
    it corresponds to searching for a single pellet in a maze.

- `CrossroadSearchProblem` (`searchAgents.py`)

    A specific type of SearchProblem that you will define for the *extra
    credit* problem --- it corresponds to searching only between
    cross-roads where pacman has to make a choice between directions
    to proceed.

- `CornersProblem` (`searchAgents.py`)

	A specific type of SearchProblem that you will define --- it
    corresponds to searching for a path through all four corners of
    a maze. (next week)

- `FoodSearchProblem` (`searchAgents.py`)

	A specific type of SearchProblem that you will be working with ---
    it corresponds to searching for a way to eat all the pellets in
    a maze. (next week)

- Search Function

	A search function is a function which takes an instance of
    SearchProblem as a parameter, runs some algorithm, and returns a
    sequence of actions that lead to a goal. Example of search functions
    are `depthFirstSearch` and `breadthFirstSearch`,
    which you have to write. You are provided `tinyMazeSearch`
    which is a very bad search function that only works correctly on
    `tinyMaze`

- `SearchAgent`

	`SearchAgent` is a class which implements an Agent (an
    object that interacts with the world) and does its planning through
    a search function. The `SearchAgent` first uses the search
    function provided to make a plan of actions to take to reach the
    goal state, and then executes the actions one at a time.
