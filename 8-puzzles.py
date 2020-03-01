import random
import math
import sys

# Lab Assignment #4
# 8-Puzzles Problem
# 
# AUCSC 460
# Author: Jinzhe Li
# Instructor: Mi-Young Kim
# 
# This Python program uses simulated annealing algorithm to find the solution.

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

def addActions(currentState, newState,children):
	newState.parent = currentState
	newState.gncost += 1
	newState.hncost = calculateManhattan(newState)
	newState.fncost = newState.gncost - newState.hncost
	children.append(newState)

def actions(currentState):
	children = []

	# If the boat is on side A
	if currentState.first == 0:

		newState = State(currentState.second, 0, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		# newState.parent = currentState
		# newState.gncost += 1
		# newState.hncost = calculateManhattan(newState)
		# newState.fncost = newState.gncost - newState.hncost
		# children.append(newState)
		addActions(currentState, newState,children)
		

		newState = State(currentState.fourth, currentState.second, currentState.third,
                            0, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

	elif currentState.second == 0:
		newState = State(0, currentState.first, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.fifth, currentState.third,
                            currentState.fourth, 0, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.third, 0,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)
    
	elif currentState.third == 0:
		newState = State(currentState.first, 0, currentState.second,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.second, currentState.sixth,
                            currentState.fourth, currentState.fifth, 0,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)
    
	elif currentState.fourth == 0:
		newState = State(0, currentState.second, currentState.third,
                            currentState.first, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fifth, 0, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.seventh, currentState.fifth, currentState.sixth,
                            0, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)
    
	elif currentState.fifth == 0:
		newState = State(currentState.first, 0, currentState.third,
                            currentState.fourth, currentState.second, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.second, currentState.third,
                            0, currentState.fourth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.sixth, 0,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.eighth, currentState.sixth,
                            currentState.seventh, 0, currentState.nineth)
		addActions(currentState, newState,children)
    
	elif currentState.sixth == 0:
		newState = State(currentState.first, currentState.second, 0,
                            currentState.fourth, currentState.fifth, currentState.third,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, 0, currentState.fifth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.nineth,
                            currentState.seventh, currentState.eighth, 0)
		addActions(currentState, newState,children)
    
	elif currentState.seventh == 0:
		newState = State(currentState.first, currentState.second, currentState.third,
                            0, currentState.fifth, currentState.sixth,
                            currentState.fourth, currentState.eighth, currentState.nineth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.eighth, 0, currentState.nineth)
		addActions(currentState, newState,children)
    
	elif currentState.eighth == 0:
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            0, currentState.seventh, currentState.nineth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, 0, currentState.sixth,
                            currentState.seventh, currentState.fifth, currentState.nineth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.nineth, 0)
		addActions(currentState, newState,children)
    
	else:
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, 0,
                            currentState.seventh, currentState.eighth, currentState.sixth)
		addActions(currentState, newState,children)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, 0, currentState.eighth)
		addActions(currentState, newState,children)

	return children

####################################################################################


def AStarSearch():
	print("Enter 9 numbers (including 0): ")
	one, two, three = input().split()
	four, five, six = input().split()
	seven, eight, nine = input().split() 
	initialState = State(int(one), int(two), int(three), int(four), \
				int(five), int(six), int(seven), int(eight), int(nine))
	openList = list()
	closeList = list()
	openList.append(initialState)
	moveCount = 0
	if initialState.isGoal():
		print('What you entered is the goal!')
		sys.exit()
	print("Output:")
	print("(Initial)")
	printState(initialState)
	while openList:
		min = openList[0].fncost
		currentMin = openList[0]
		for i in range(0, len(openList)):
			if openList[i].fncost < min:
				min = openList[i].fncost
				currentMin = openList[i]
		openList.remove(currentMin)
		closeList.insert(0,currentMin)
		children = actions(currentMin)
		moveCount +=1
		for child in children:
			if child not in closeList:
				if child.isGoal():
					return child
				elif child not in openList:
					openList.append(child)

####################################################################################

def printMoveNum(count):
	print("===========================")
	print("Total number of moves: " + str(count))
	print("===========================")

def printNextInfo(count, nextState, lastState):
	oldList = list()
	oldList.append(str(lastState.first))
	oldList.append(str(lastState.second))
	oldList.append(str(lastState.third))
	oldList.append(str(lastState.fourth))
	oldList.append(str(lastState.fifth))
	oldList.append(str(lastState.sixth))
	oldList.append(str(lastState.seventh))
	oldList.append(str(lastState.eighth))
	oldList.append(str(lastState.nineth))

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
	status = str

	for i in range(0,9):
		if oldList[i] == '0':
			lastZeroIndex = i
		if newList[i] == '0':
			nextZeroIndex = i
	
	if ((nextZeroIndex//3) - (lastZeroIndex//3)) == 1:
		status = "down"
	elif ((nextZeroIndex//3) - (lastZeroIndex//3)) == -1:
		status = "up"
	elif ((nextZeroIndex%3) - (lastZeroIndex%3)) == 1:
		status = "right"
	else:
		status = "left"
	
	if count == 1:
		print(str(count) + "st move" + " (move blank tail " + status + "):")
	elif count%10 == 2:
		print(str(count) + "nd move" + " (move blank tail " + status + "):")
	elif count%10 == 3:
		print(str(count) + "rd move" + " (move blank tail " + status + "):")
	else:
		print(str(count) + "th move" + " (move blank tail " + status + "):")

def printState(solution):
		printList = list()
		printList.append(str(solution.first))
		printList.append(str(solution.second))
		printList.append(str(solution.third))
		printList.append(str(solution.fourth))
		printList.append(str(solution.fifth))
		printList.append(str(solution.sixth))
		printList.append(str(solution.seventh))
		printList.append(str(solution.eighth))
		printList.append(str(solution.nineth))
		for i in range(0,9):
			if printList[i] == '0':
				printList[i] = ' '
		for i in range(0,9,3):
			print(printList[i] + " " + printList[i+1] + " " + printList[i+2])
		print("")

def printAll(solution):
	path = []
	path.append(solution)
	parent = solution.parent
	while parent:
		path.insert(0, parent)
		parent = parent.parent
	for t in range(0,len(path)):
		if t + 1 < len(path):
			state = path[t]
			nextState = path[t + 1]
			printNextInfo(t + 1, nextState, state)
			printState(nextState)
	printMoveNum(len(path) - 1)

####################################################################################

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
	# Find the solution
    # SASearch()
	
	solution = AStarSearch()
	printAll(solution)

####################################################################################

# Call main() to run it
if __name__ == "__main__":
    main()