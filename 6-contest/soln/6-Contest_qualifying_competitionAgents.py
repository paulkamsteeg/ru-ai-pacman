# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance, nearestPoint
from game import Directions, Agent
import random, util
import distanceCalculator

class CompetitionAgent(Agent):
  """
  A base class for competition agents.  The convenience methods herein handle
  some of the complications of the game.

  Recommended Usage:  Subclass CompetitionAgent and override getAction.
  """

  #############################
  # Methods to store key info #
  #############################

  def __init__( self, index=0, timeForComputing = .1 ):
    """
    Lists several variables you can query:
    self.index = index for this agent
    self.distancer = distance calculator (contest code provides this)
    self.timeForComputing = an amount of time to give each turn for computing maze distances
        (part of the provided distance calculator)
    """
    # Agent index for querying state, N.B. pacman is always agent 0
    self.index = index

    # Maze distance calculator
    self.distancer = None

    # Time to spend each turn on computing maze distances
    self.timeForComputing = timeForComputing

    # Access to the graphics
    self.display = None

    # useful function to find functions you've defined elsewhere..
    # self.usefulFunction = util.lookup(usefulFn, globals())


  def registerInitialState(self, gameState):
    """
    This method handles the initial setup of the
    agent to populate useful fields.
    
    A distanceCalculator instance caches the maze distances 
    between each pair of positions, so your agents can use:
    self.distancer.getDistance(p1, p2)
    """
    self.distancer = distanceCalculator.Distancer(gameState.data.layout)
    
    # comment this out to forgo maze distance computation and use manhattan distances
    # self.distancer.getMazeDistances()
    
    import __main__
    if '_display' in dir(__main__):
      self.display = __main__._display


  #################
  # Action Choice #
  #################

  def getAction(self, gameState):
    """
    Override this method to make a good agent. It should return a legal action within
    the time limit (otherwise a random legal action will be chosen for you).
    """
    util.raiseNotDefined()

  #######################
  # Convenience Methods #
  #######################

  def getFood(self, gameState):
    """
    Returns the food you're meant to eat. This is in the form of a matrix
    where m[x][y]=true if there is food you can eat (based on your team) in that square.
    """
    return gameState.getFood()

  def getCapsules(self, gameState):
    return gameState.getCapsules()


  def getScore(self, gameState):
    """
    Returns how much you are beating the other team by in the form of a number
    that is the difference between your score and the opponents score.  This number
    is negative if you're losing.
    """
    return gameState.getScore()

  def getMazeDistance(self, pos1, pos2):
    """
    Returns the distance between two points; These are calculated using the provided
    distancer object.

    If distancer.getMazeDistances() has been called, then maze distances are available.
    Otherwise, this just returns Manhattan distance.
    """
    d = self.distancer.getDistance(pos1, pos2)
    return d


class BaselineAgent(CompetitionAgent):
  """
    This is a baseline reactive agent to see if you can do better.
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.
  """

  def __init__(self, evalFn = 'evaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.depth = int(depth)
    self._expanded = 0

  def getAction(self, gameState):
    """
    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """

    # Collect legal moves and successor states
    numAgents = gameState.getNumAgents()
    self.movedepth = self.depth * numAgents # convert depth in ply into depth in moves
    
    alpha = float('-inf')
    beta = float('inf')
    actions = gameState.getLegalActions(0)
    scores = []
    bestScore=alpha
    for action in actions:
      nextState = gameState.generateSuccessor(0, action)
      self._expanded += 1 # count num successors calls
      #print action
      # N.B. We use alpha-1 as the alpha threshold so we can detect if this action
      #      is exactly as good as the current best action, or just pruned because it
      #      it would have a *worse* value
      # Otherwise all worse actions would have the same evaluation so we would treat 
      # them as ties and our tie-breaker could pick what is actually a *worse* action!
      score = self.alphabeta(nextState, 1, alpha-1, beta)
      scores.append(score)
      alpha = max(score, alpha)
      #print "Root Score = %f  (%f,%f)" % (score,alpha,beta)

    #print actions
    #print scores
    # random tie-breaker between moves with the same evaluation
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best
    return actions[chosenIndex]

  def evaluationFunction(self, state):
    # Useful information you can extract from a GameState (pacman.py)
    return state.getScore()

  def alphabeta(self, state, movedepth, alpha, beta):
    """ This function computes the minimax value of state as estimated by a search to the 
        given movedepth where leaf nodes are scored by calling evaluation function.
        This version uses alpha-beta pruning to reduce the number of nodes which must
        be evaulated. 
       beta represents MIN (non-pacman) player best choice, i.e. lower bound on value of current choice
           MIN won't allow us to use this state if alpha can choose better value.
       alpha represents MAX (i.e. pacman) upper-bound on our best choice 
         MAX won't pick one of these options if it's worse than best value in different branch
         """
    # Terminate the depth-first style search when we reach the indicated depth bound
    # or of the state is a win/loss position
    if movedepth >= self.movedepth or state.isWin() or state.isLose():
      score = self.evaluationFunction(state)
      #print("Score = %d" % score)
      #print "^^^^^^^^^^^^^^"
      return score
    
    # N.B. this code works automatically for any number of ghosts.
    numAgents = state.getNumAgents()
    # N.B. Pacman is always agent #0, ghosts are numbered after that
    agentIndex = movedepth % numAgents

    # initial values for this state are 'worse case' values for this agent,
    # i.e. -inf for pacman (MAX) or inf for ghost (MIN)
    for action in state.getLegalActions(agentIndex):
      # recursively call ourselves to evaluate the child moves
      nextState = state.generateSuccessor(agentIndex, action)
      #print action
      #print nextState
      guess = self.alphabeta(nextState, movedepth+1, alpha, beta)
      #print "Guess = %f  (%f,%f)" % (guess,alpha,beta)
      self._expanded += 1
      # pacman agent = MAX = alpha
      if agentIndex == 0:
        alpha = max(alpha, guess) # update the alpha value
        if beta <= alpha:
          break # stop if alpha is bigger than beta, i.e. MIN can choose other branch with value==beta
      else: # ghost = MIN = beta
        beta = min(beta, guess) # update beta value
        if beta <= alpha:
          break # stop if alpha is bigger than beta, i.e. MAX can choose other branch with value==alpha

    #print "^^^^^^^^^^^^^^"
    if (agentIndex==0):
      return alpha
    else:
      return beta

class TimeoutAgent( Agent ):
  """
  A random agent that takes too much time. Taking
  too much time results in penalties and random moves.
  """
  def __init__( self, index ):
    self.index = index
    
  def getAction( self, state ):
    import random, time
    time.sleep(2.0)
    return random.choice( state.getLegalActions( self.index ) )

MyPacmanAgent=BaselineAgent
