##this class uses a dynammic programming approach to solve the knapsack problem

class KnapsackDynamicProg:

	def __init__(self, max_weight, weight_arr, value_arr, number_of_items):
		self.max_weight = max_weight
		self.weight_arr = weight_arr
		self.number_of_items = number_of_items
		self.value_arr = value_arr

	def buildknapSackTable(self):
		## initialize array, fill with zeros
		K = [[0 for x in range(self.max_weight + 1)] for x in range(self.number_of_items + 1)]

		#build array from bottom to up
		for i in range(self.number_of_items + 1):
			for w in range(self.max_weight + 1):
				if i == 0 or w == 0:
					K[i][w] = 0
				elif self.weight_arr[i-1] <= w:
					K[i][w] = max(self.value_arr[i-1]
							+ K[i-1][w-self.weight_arr[i-1]],
								K[i-1][w])
				else:
					K[i][w] = K[i-1][w]
		## bottom right corner of arr gives the max value that can be stored in knapsack of given size
		return K[self.number_of_items][self.max_weight]

	def solve(max_weight, weight_arr, value_arr):
		kp = KnapsackDynamicProg(max_weight, weight_arr, value_arr, len(weight_arr))
		return kp.buildknapSackTable()
