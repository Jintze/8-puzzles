import random
import math
import sys

# Assignment #1
# 8-Puzzles Problem Using A*
# 
# AUCSC 460
# Author: Jinzhe Li
# Instructor: Mi-Young Kim
# 
# This Python program uses A* algorithm to find the solution.

####################################################################################

# Define the state
class State():
	def __init__(self, first, second, third, fourth, fifth, sixth, seventh, eighth, nineth):
		self.first = first
		self.second = second
		self.third = third
		self.fourth = fourth
		self.fifth = fifth
		self.sixth = sixth
		self.seventh = seventh
		self.eighth = eighth
		self.nineth = nineth
		self.parent = None
		self.gncost = 0
		self.hncost = 0
		self.fncost = 0

	# Decide if it is goal state
	def isGoal(self):
		if self.first == 0 \
            and self.second == 1 \
            and self.third == 2 \
            and self.fourth == 3 \
            and self.fifth == 4 \
            and self.sixth == 5 \
            and self.seventh == 6 \
            and self.eighth == 7 \
            and self.nineth == 8:
			return True
		else:
			return False

	def __eq__(self, other):
		return self.first == other.first \
            and self.second == other.second \
            and self.third == other.third \
            and self.fourth == other.fourth \
            and self.fifth == other.fifth \
            and self.sixth == other.sixth \
            and self.seventh == other.seventh \
            and self.eighth == other.eighth \
            and self.nineth == other.nineth

	def __hash__(self):
		return hash((self.first, self.second, self.third, \
			self.fourth, self.fifth, self.sixth, \
            self.seventh, self.eighth, self.nineth))

####################################################################################

# If the new vaild state is generated, then add it to children,
# and update the value for f(n), g(n) and h(n)
# Note: g(n) is the steps that are taken, and h(n) is Manhattan distance.
def addActions(currentState, newState,children):
	newState.parent = currentState
	newState.gncost += 1
	newState.hncost = calculateManhattan(newState)
	newState.fncost = newState.gncost - newState.hncost
	children.append(newState)

# It is mess here because of the way I define the state.
def actions(currentState):
	children = []

	# If the boat is on side A
	if currentState.first == 0:	# If the first digit is empty.
								# The same thing for elifs below.
		# Move blank tail right.
		newState = State(currentState.second, 0, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)
		
		# Move blank tail down.
		newState = State(currentState.fourth, currentState.second, currentState.third,
                            0, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

	elif currentState.second == 0:
		# Move blank tail left.
		newState = State(0, currentState.first, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		# Move blank tail down.
		newState = State(currentState.first, currentState.fifth, currentState.third,
                            currentState.fourth, 0, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		# Move blank tail right.
		newState = State(currentState.first, currentState.third, 0,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)
    
	elif currentState.third == 0:
		# Move blank tail left.
		newState = State(currentState.first, 0, currentState.second,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		# Move blank tail down.
		newState = State(currentState.first, currentState.second, currentState.sixth,
                            currentState.fourth, currentState.fifth, 0,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)
    
	elif currentState.fourth == 0:
		# Move blank tail up.
		newState = State(0, currentState.second, currentState.third,
                            currentState.first, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		# Move blank tail right.
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fifth, 0, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		# Move blank tail down.
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.seventh, currentState.fifth, currentState.sixth,
                            0, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)
    
	elif currentState.fifth == 0:
		# Move blank tail up.
		newState = State(currentState.first, 0, currentState.third,
                            currentState.fourth, currentState.second, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		# Move blank tail left.
		newState = State(currentState.first, currentState.second, currentState.third,
                            0, currentState.fourth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		# Move blank tail right.
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.sixth, 0,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		# Move blank tail down.
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.eighth, currentState.sixth,
                            currentState.seventh, 0, currentState.nineth)
		addActions(currentState, newState,children)
    
	elif currentState.sixth == 0:
		# Move blank tail up.
		newState = State(currentState.first, currentState.second, 0,
                            currentState.fourth, currentState.fifth, currentState.third,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		# Move blank tail left.
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, 0, currentState.fifth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		# Move blank tail down.
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.nineth,
                            currentState.seventh, currentState.eighth, 0)
		addActions(currentState, newState,children)
    
	elif currentState.seventh == 0:
		# Move blank tail up.
		newState = State(currentState.first, currentState.second, currentState.third,
                            0, currentState.fifth, currentState.sixth,
                            currentState.fourth, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		# Move blank tail right.
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.eighth, 0, currentState.nineth)
		addActions(currentState, newState,children)
    
	elif currentState.eighth == 0:
		# Move blank tail left.
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            0, currentState.seventh, currentState.nineth)
		addActions(currentState, newState,children)

		# Move blank tail up.
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, 0, currentState.sixth,
                            currentState.seventh, currentState.fifth, currentState.nineth)
		addActions(currentState, newState,children)

		# Move blank tail right.
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.nineth, 0)
		addActions(currentState, newState,children)
    
	else:
		# Move blank tail up.
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, 0,
                            currentState.seventh, currentState.eighth, currentState.sixth)
		addActions(currentState, newState,children)

		# Move blank tail left.
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, 0, currentState.eighth)
		addActions(currentState, newState,children)

	return children

####################################################################################

# A* search.
# The number of input number must be in total of 9, from 0 to 8,
# break with space, and the there are 3 rows for 9 numbers,
# press Enter after finish the input for each row (which is 3 numbers)
# e.g:	0 2 1
#		4 3 5
#		6 7 8
# This algorithm calculate the f(n) value for each move and pick the lowest one among all.
def AStarSearch():
	# Input
	print("Enter 9 numbers (including 0): ")
	one, two, three = input().split()
	four, five, six = input().split()
	seven, eight, nine = input().split() 
	print("")
	# Store input as a state.
	initialState = State(int(one), int(two), int(three), int(four), \
				int(five), int(six), int(seven), int(eight), int(nine))

	openList = list()	# A list that contain all possible choices for next move.
	closeList = list()	# Visited nodes.
	openList.append(initialState)
	if initialState.isGoal():	# If the input is already the goal, exit.
		print('What you entered is the goal!')
		sys.exit()
	print("Output:")
	print("(Initial)")
	printState(initialState)
	while openList:							# If there are possible moves.
		min = openList[0].fncost			# Choose the one that has the lowest f(n),
		currentMin = openList[0]			
		for i in range(0, len(openList)):
			if openList[i].fncost < min:
				min = openList[i].fncost
				currentMin = openList[i]
		openList.remove(currentMin)			# Remove current state,
		closeList.insert(0,currentMin)		# and put it into the visited list.
		children = actions(currentMin)		# Get all possible next moves.
		for child in children:
			if child not in closeList:		# If it is not visited yet
				if child.isGoal():			# If it is the goal, return.
					return child
				elif child not in openList:	# If it has not been added into the list
					openList.append(child)	# that contains all possible moves,
											# then add it into it.

####################################################################################

# Print the total number of moves if find the solution.
def printMoveNum(count):
	print("===========================")
	print("Total number of moves: " + str(count))
	print("===========================")

# I first put the current state and next state into lists, so that it 
# can iterativly print.
def printNextInfo(count, nextState, lastState):
	curList = list()
	curList.append(str(lastState.first))
	curList.append(str(lastState.second))
	curList.append(str(lastState.third))
	curList.append(str(lastState.fourth))
	curList.append(str(lastState.fifth))
	curList.append(str(lastState.sixth))
	curList.append(str(lastState.seventh))
	curList.append(str(lastState.eighth))
	curList.append(str(lastState.nineth))

	newList = list()
	newList.append(str(nextState.first))
	newList.append(str(nextState.second))
	newList.append(str(nextState.third))
	newList.append(str(nextState.fourth))
	newList.append(str(nextState.fifth))
	newList.append(str(nextState.sixth))
	newList.append(str(nextState.seventh))
	newList.append(str(nextState.eighth))
	newList.append(str(nextState.nineth))

	lastZeroIndex = 0	
	nextZeroIndex = 0

	for i in range(0,9):		# Find the position of blank tail in current and next state.
		if curList[i] == '0':
			lastZeroIndex = i
		if newList[i] == '0':
			nextZeroIndex = i
	
	# Figure out how the blank tail moves.
	if ((nextZeroIndex//3) - (lastZeroIndex//3)) == 1:
		status = "down"
	elif ((nextZeroIndex//3) - (lastZeroIndex//3)) == -1:
		status = "up"
	elif ((nextZeroIndex%3) - (lastZeroIndex%3)) == 1:
		status = "right"
	else:
		status = "left"
	
	# Print which number of moves it is, and how the blank tail moves.
	if count == 1:
		print(str(count) + "st move" + " (move blank tail " + status + "):")
	elif count%10 == 2:
		print(str(count) + "nd move" + " (move blank tail " + status + "):")
	elif count%10 == 3:
		print(str(count) + "rd move" + " (move blank tail " + status + "):")
	else:
		print(str(count) + "th move" + " (move blank tail " + status + "):")
	
def printState(nextState):
	state = list()
	state.append(str(nextState.first))
	state.append(str(nextState.second))
	state.append(str(nextState.third))
	state.append(str(nextState.fourth))
	state.append(str(nextState.fifth))
	state.append(str(nextState.sixth))
	state.append(str(nextState.seventh))
	state.append(str(nextState.eighth))
	state.append(str(nextState.nineth))
	# Print the current state.
	for i in range(0,9):
		if state[i] == '0':
			state[i] = ' '
	for i in range(0,9,3):
		print(state[i] + " " + state[i+1] + " " + state[i+2])
	print("")

# Since my state has an attribute called "parent", once we have the solution,
# it is easy to trace back and find the whole path from the initial state to
# the goal state.
def printAll(solution):
	path = []
	path.append(solution)
	parent = solution.parent
	while parent:					# Find parents for each gen, put them into
		path.insert(0, parent)		# a list.
		parent = parent.parent
	for t in range(0,len(path)):	# Print them all
		if t + 1 < len(path):
			state = path[t]
			nextState = path[t + 1]
			printNextInfo(t + 1, nextState, state)
			printState(nextState)
	printMoveNum(len(path) - 1)

####################################################################################

# Calculate manhattan distance.
def calculateManhattan(currentState):
    manhattanDict = 0
    if currentState.first != 0:
        manhattanDict -= abs(((currentState.first)%3) - 0) + abs((currentState.first)//3 - 0)
    if currentState.second != 0:
        manhattanDict -= abs(((currentState.second)%3) - 1) + abs((currentState.second)//3 - 0)
    if currentState.third != 0:
        manhattanDict -= abs(((currentState.third)%3) - 2) + abs((currentState.third)//3 - 0)
    if currentState.fourth != 0:
        manhattanDict -= abs(((currentState.fourth)%3) - 0) + abs((currentState.fourth)//3 - 1)
    if currentState.fifth != 0:
        manhattanDict -= abs(((currentState.fifth)%3) - 1) + abs((currentState.fifth)//3 - 1)
    if currentState.sixth != 0:
        manhattanDict -= abs(((currentState.sixth)%3) - 2) + abs((currentState.sixth)//3 - 1)
    if currentState.seventh != 0:
        manhattanDict -= abs(((currentState.seventh)%3) - 0) + abs((currentState.seventh)//3 - 2)
    if currentState.eighth != 0:
        manhattanDict -= abs(((currentState.eighth)%3) - 1) + abs((currentState.eighth)//3 - 2)
    if currentState.nineth != 0:
        manhattanDict -= abs(((currentState.nineth)%3) - 2) + abs((currentState.nineth)//3 - 2)
    return manhattanDict

####################################################################################

def main():
	solution = AStarSearch()
	printAll(solution)

####################################################################################

# Call main() to run it
if __name__ == "__main__":
    main()