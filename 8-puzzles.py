import random
import math

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
		if self.first == 1 \
            and self.second == 2 \
            and self.third == 3 \
            and self.fourth == 4 \
            and self.fifth == 5 \
            and self.sixth == 6 \
            and self.seventh == 7 \
            and self.eighth == 8 \
            and self.nineth == 0:
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

# def addActions(currentState):
# 	newState.parent = currentState
# 	newState.gncost += 1
# 	newState.hncost = calculateManhattan(newState)
# 	children.append(newState)

def actions(currentState):
	children = []

	# If the boat is on side A
	if currentState.first == 0:

		newState = State(currentState.second, 0, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)
		

		newState = State(currentState.fourth, currentState.second, currentState.third,
                            0, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

	elif currentState.second == 0:
		newState = State(0, currentState.first, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.fifth, currentState.third,
                            currentState.fourth, 0, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.third, 0,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)
    
	elif currentState.third == 0:
		newState = State(currentState.first, 0, currentState.second,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.second, currentState.sixth,
                            currentState.fourth, currentState.fifth, 0,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)
    
	elif currentState.fourth == 0:
		newState = State(0, currentState.second, currentState.third,
                            currentState.first, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fifth, 0, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.seventh, currentState.fifth, currentState.sixth,
                            0, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)
    
	elif currentState.fifth == 0:
		newState = State(currentState.first, 0, currentState.third,
                            currentState.fourth, currentState.second, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.second, currentState.third,
                            0, currentState.fourth, currentState.sixth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.sixth, 0,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.eighth, currentState.sixth,
                            currentState.seventh, 0, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)
    
	elif currentState.sixth == 0:
		newState = State(currentState.first, currentState.second, 0,
                            currentState.fourth, currentState.fifth, currentState.third,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, 0, currentState.fifth,
                            currentState.seventh, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.nineth,
                            currentState.seventh, currentState.eighth, 0)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)
    
	elif currentState.seventh == 0:
		newState = State(currentState.first, currentState.second, currentState.third,
                            0, currentState.fifth, currentState.sixth,
                            currentState.fourth, currentState.eighth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.eighth, 0, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)
    
	elif currentState.eighth == 0:
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            0, currentState.seventh, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, 0, currentState.sixth,
                            currentState.seventh, currentState.fifth, currentState.nineth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, currentState.nineth, 0)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)
    
	else:
		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, 0,
                            currentState.seventh, currentState.eighth, currentState.sixth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

		newState = State(currentState.first, currentState.second, currentState.third,
                            currentState.fourth, currentState.fifth, currentState.sixth,
                            currentState.seventh, 0, currentState.eighth)
		newState.parent = currentState
		newState.gncost += 1
		newState.hncost = calculateManhattan(newState)
		newState.fncost = newState.gncost - newState.hncost
		children.append(newState)

	return children

####################################################################################

def schedule(t):    # This is a linear schedule(t) function, which makes T reduced 
                    # as time goes by
    T = 999999 - t  # The number (e.g: 999999) here should equal to (the top range 
                    # of t - 1), user can edit it on line 229.
    return T

def AStarSearch():
	# userInput = list()
	# for i in range(1, 4):
	# 	for j in range(1, 4):
	# 		print("input column " + str(i) + ", row " + str(j) + "'s number:")
	# 		currInput = int(input())
	# 		userInput.append(currInput)
	# userInput = tuple(userInput)
	# initialState = State(userInput[0],userInput[1],userInput[2],
	# 					userInput[3],userInput[4],userInput[5],
	# 					userInput[6],userInput[7],userInput[8])
	initialState = State(0,1,2,3,4,5,6,7,8)
	openList = list()
	closeList = list()
	# costList = list()
	# path = []
	# gn = int()
	# hn = int()
	openList.append(initialState)
	# print(openList)
	# print(type(openList))
	# print(openList[0])
	while openList:
		# if len(openList) == 0:
		# min = 0
		min = openList[0].fncost
		currentMin = openList[0]
		for i in range(0, len(openList)):
			# currentIndex = 0
			if openList[i].fncost < min:
				min = openList[i].fncost
				currentMin = openList[i]
				currentIndex = i
		# if currentMin:
		openList.remove(currentMin)
		closeList.append(currentMin)
		if currentMin.isGoal():
			print('Success!')
			return currentMin
		else:
			children = actions(currentMin)
			for child in children:
				if child not in closeList:
					if child.isGoal():
						print('Success!')
						printTest(child)
						return child
					elif child not in openList:
						openList.append(child)


def printTest(solution):
	print("[ " + str(solution.first) + " " + str(solution.second) + " " + str(solution.third) + " ] \n")
	print("[ " + str(solution.fourth) + " " + str(solution.fifth) + " " + str(solution.sixth) + " ] \n")
	print("[ " + str(solution.seventh) + " " + str(solution.eighth) + " " + str(solution.nineth) + " ]")





def SASearch():
	initialState = State(1,2,3,4,5,6,7,0,8)
	chooseOne = list()  # For later use of storing all possible child node and pick one 
                        # of them randomly
	nextNode = list()   # Store the next node we gonna visit.
	parentNode = list() # Store current node's parent node so that it will not be visit 
                        # again

	nextNode.append(initialState)
	printInitial(initialState, calculateManhattan(initialState))

	for t in range(1, 1000000):      # for t = 1 to ∞ do
                                    # This topper bound of range is for user to edit.
                                    # While I tested it, t = 1 000 000 and
                                    # T = 999 999 can ensure that we get an answer.
                                    # (in schedule(t))
                                    # (Although it will not iterate that many times,
                                    # it will stop somewhere between )
		T = schedule(t) # T ← schedule(t)
		currentState = nextNode.pop(0)

		if T == 0:      # if T = 0 then return current
			print('T reached 0, did not get the solution.')
			return currentState

		if currentState.isGoal():   # If reach the goal, return and print solution
			print('Success!')
			return currentState

		children = actions(currentState)    # Get all possible states

		for child in children:
			if child not in parentNode:     # Make sure not to visit parent state
				chooseOne.insert(0, child)
		num = random.randrange(0, len(chooseOne))
		nextChild = chooseOne[num] # next ← a randomly selected successor of current
		parentNode.clear()

		currentValue = calculateManhattan(currentState)
		nextValue = calculateManhattan(nextChild)
		
		deltaE = nextValue - currentValue #ΔE ← next.VALUE – current.VALUE
		func = math.exp(deltaE/T)

		if deltaE > 0: #if ΔE > 0 then current ← next
			nextNode.append(nextChild)
			printState(nextChild, currentValue, nextValue)
			parentNode.append(currentState)
		else: # else: current ← next only with probability e^(ΔE/T)

            # Since the way I set up schedule(t), my T's lowest value before it reach 0 is 1,
            # thus the range of e^(ΔE/T)'s value is [math.exp(-1), 1].
            # I believe if I choose random number from math.exp(-1) to 1, it works the best
            # when we consider "next with probability e^(ΔE/T)" .
            # This is, when time goes by, it is less possible to accept next ΔE < 0 node.
			probability = random.uniform(math.exp(-1), 1)

			if func > probability: # if next node accepted
				nextNode.append(nextChild)
				printState(nextChild, currentValue, nextValue)
				parentNode.append(currentState)
			else:
				nextNode.append(currentState) # if next node not accepted, do nothing, loop again

		chooseOne.clear() #For choosing next child node next loop

####################################################################################

def calculateManhattan(currentState):
    manhattanDict = 0
    if currentState.first != 0:
        manhattanDict -= abs(((currentState.first-1)%3) - 0) + abs((currentState.first-1)//3 - 0)
    if currentState.second != 0:
        manhattanDict -= abs(((currentState.second-1)%3) - 1) + abs((currentState.second-1)//3 - 0)
    if currentState.third != 0:
        manhattanDict -= abs(((currentState.third-1)%3) - 2) + abs((currentState.third-1)//3 - 0)
    if currentState.fourth != 0:
        manhattanDict -= abs(((currentState.fourth-1)%3) - 0) + abs((currentState.fourth-1)//3 - 1)
    if currentState.fifth != 0:
        manhattanDict -= abs(((currentState.fifth-1)%3) - 1) + abs((currentState.fifth-1)//3 - 1)
    if currentState.sixth != 0:
        manhattanDict -= abs(((currentState.sixth-1)%3) - 2) + abs((currentState.sixth-1)//3 - 1)
    if currentState.seventh != 0:
        manhattanDict -= abs(((currentState.seventh-1)%3) - 0) + abs((currentState.seventh-1)//3 - 2)
    if currentState.eighth != 0:
        manhattanDict -= abs(((currentState.eighth-1)%3) - 1) + abs((currentState.eighth-1)//3 - 2)
    if currentState.nineth != 0:
        manhattanDict -= abs(((currentState.nineth-1)%3) - 2) + abs((currentState.nineth-1)//3 - 2)
    return manhattanDict

####################################################################################

def main():
	# Find the solution
    # SASearch()
	AStarSearch()
	print('Done')

def printState(solution,value,childValue):
    file = open("output.txt", "a")
    if childValue == 0:
        file.writelines("Goal state: \n")
    else:
        file.writelines("Next: \n")
    file.writelines("[ " + str(solution.first) + " " + str(solution.second) + " " + str(solution.third) + " ] \n")
    file.writelines("[ " + str(solution.fourth) + " " + str(solution.fifth) + " " + str(solution.sixth) + " ] \n")
    if childValue >= value:
        file.writelines("[ " + str(solution.seventh) + " " + str(solution.eighth) + " " + str(solution.nineth) + " ]"\
            + "(h=" + str(-childValue) + ") \n")
    else:   # if child value < current value, then it is a bad move
        file.writelines("[ " + str(solution.seventh) + " " + str(solution.eighth) + " " + str(solution.nineth) + " ]"\
            + "(h=" + str(-childValue) + ", BAD MOVE) \n")
    file.close()

def printInitial(solution, value):
    file = open("output.txt", "a")
    file.writelines("Initial state: \n")
    file.writelines("[ " + str(solution.first) + " " + str(solution.second) + " " + str(solution.third) + " ] \n")
    file.writelines("[ " + str(solution.fourth) + " " + str(solution.fifth) + " " + str(solution.sixth) + " ] \n")
    file.writelines("[ " + str(solution.seventh) + " " + str(solution.eighth) + " " + str(solution.nineth) + " ]" \
        + "(h=" + str(-value) + ") \n")
    file.close() 

####################################################################################

# Call main() to run it
if __name__ == "__main__":
    main()