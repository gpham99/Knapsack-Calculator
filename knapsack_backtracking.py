class KnapsackRecurser:

    def __init__(self):
        self.best_so_far = (0,0)

    def solve_internal(self, max_wt, weights, values, weight = 0, value = 0):
        if weight > max_wt:# the case where this subtree isn't worth checking
            return (weight, -1)#set value to neg number to discount this branch
        if value + sum(values) <self.best_so_far[1]:#could never be better then the best
            return (weight, value)
        if len(weights) == 0:
            return (weight, value)
        else:#check all children
            children_values = []
            for i in range(1,len(weights)+1):
                children_values.append(self.solve_internal(max_wt, weights[i:], values[i:],weight+weights[i-1], value+values[i-1] ))
            best_child = max(children_values,key=lambda item:item[1])
            if best_child[1] > self.best_so_far[1]:
                self.best_so_far = best_child
            if best_child[1] == -1:#none of the children worked out
                return (weight, value)
            return best_child

    def solve(max_weight, weight_arr, value_arr):
        self_solver = KnapsackRecurser()
        return (self_solver.solve_internal(max_weight, weight_arr, value_arr))[1]
