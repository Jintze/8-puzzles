import random
import math

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

def actions(currentState):
	children = []

	# If the boat is on side A
	if currentState.first == 0:

		newState = State(currentState.second, 
                            0,
                            currentState.third,
                            currentState.fourth,
                            currentState.fifth,
                            currentState.sixth,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.fourth,
                            currentState.second,
                            currentState.third,
                            0,
                            currentState.fifth,
                            currentState.sixth,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

	elif currentState.second == 0:
		newState = State(0, 
                            currentState.first,
                            currentState.third,
                            currentState.fourth,
                            currentState.fifth,
                            currentState.sixth,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.fifth,
                            currentState.third,
                            currentState.fourth,
                            0,
                            currentState.sixth,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.third,
                            0,
                            currentState.fourth,
                            currentState.fifth,
                            currentState.sixth,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)
    
	elif currentState.third == 0:
		newState = State(currentState.first, 
                            0,
                            currentState.second,
                            currentState.fourth,
                            currentState.fifth,
                            currentState.sixth,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.second,
                            currentState.sixth,
                            currentState.fourth,
                            currentState.fifth,
                            0,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)
    
	elif currentState.fourth == 0:
		newState = State(0, 
                            currentState.second,
                            currentState.third,
                            currentState.first,
                            currentState.fifth,
                            currentState.sixth,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            currentState.fifth,
                            0,
                            currentState.sixth,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            currentState.seventh,
                            currentState.fifth,
                            currentState.sixth,
                            0,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)
    
	elif currentState.fifth == 0:
		newState = State(currentState.first, 
                            0,
                            currentState.third,
                            currentState.fourth,
                            currentState.second,
                            currentState.sixth,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            0,
                            currentState.fourth,
                            currentState.sixth,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            currentState.fourth,
                            currentState.sixth,
                            0,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            currentState.fourth,
                            currentState.eighth,
                            currentState.sixth,
                            currentState.seventh,
                            0,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)
    
	elif currentState.sixth == 0:
		newState = State(currentState.first, 
                            currentState.second,
                            0,
                            currentState.fourth,
                            currentState.fifth,
                            currentState.third,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            currentState.fourth,
                            0,
                            currentState.fifth,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            currentState.fourth,
                            currentState.fifth,
                            currentState.nineth,
                            currentState.seventh,
                            currentState.eighth,
                            0)
		newState.parent = currentState
		children.append(newState)
    
	elif currentState.seventh == 0:
		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            0,
                            currentState.fifth,
                            currentState.sixth,
                            currentState.fourth,
                            currentState.eighth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            currentState.fourth,
                            currentState.fifth,
                            currentState.sixth,
                            currentState.eighth,
                            0,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)
    
	elif currentState.eighth == 0:
		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            currentState.fourth,
                            currentState.fifth,
                            currentState.sixth,
                            0,
                            currentState.seventh,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            currentState.fourth,
                            0,
                            currentState.sixth,
                            currentState.seventh,
                            currentState.fifth,
                            currentState.nineth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            currentState.fourth,
                            currentState.fifth,
                            currentState.sixth,
                            currentState.seventh,
                            currentState.nineth,
                            0)
		newState.parent = currentState
		children.append(newState)
    
	else:
		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            currentState.fourth,
                            currentState.fifth,
                            0,
                            currentState.seventh,
                            currentState.eighth,
                            currentState.sixth)
		newState.parent = currentState
		children.append(newState)

		newState = State(currentState.first, 
                            currentState.second,
                            currentState.third,
                            currentState.fourth,
                            currentState.fifth,
                            currentState.sixth,
                            currentState.seventh,
                            0,
                            currentState.eighth)
		newState.parent = currentState
		children.append(newState)

	return children

####################################################################################

def schedule(t):
    t = 999999 - t
    return t

def SASearch():
	initialState = State(1,2,3,4,5,8,6,7,0)
	chooseOne = list()
	nextNode = list()
	parentNode = list()
	nextNode.append(initialState)
	for t in range(1000000): #for t = 1 to ∞ do
		T = schedule(t) #T ← schedule(t)
		currentState = nextNode.pop(0)
		if T == 0: #if T = 0 then return current
			return currentState
		if currentState.isGoal():
			return currentState
		children = actions(currentState) 
		for child in children:
			if child not in parentNode:
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
			parentNode.append(currentState)
		else: #else: current ← next only with probability e^(ΔE/T)
			probability = random.uniform(0, 1)
			if func > probability:
				nextNode.append(nextChild)
				parentNode.append(currentState)
			else:
			    nextNode.append(currentState)
		chooseOne.clear()

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

def main():
	# Find the solution
    solution = SASearch()
	# Print the solution
    printSolution(solution)



def printSolution(solution):
		# path = []
		# path.append(solution)
		# parent = solution.parent
		print(str(solution.first) + " " + str(solution.second) + " " + str(solution.third))
		print(str(solution.fourth) + " " + str(solution.fifth) + " " + str(solution.sixth))
		print(str(solution.seventh) + " " + str(solution.eighth) + " " + str(solution.nineth))
		print("-----")


# Call main() to run it
if __name__ == "__main__":
    main()