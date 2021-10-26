from food import names
import random
import time
import matplotlib.pyplot as plt

def create_random(size, special_number):
    knapsack_wt = random.randint(self.special_number)
    item_dict = {}

    for i in range(size):
        new_name = random.choice(names)
        new_wt = random.randint(self.special_number)
        new_val = random.randint(self.special_number)
        item_dict.add(new_name, (new_wt, new_val))

    return (item_dict, knapsack_wt)

def item_dict_to_double_array(item_dict):
    weights = []
    values = []
    for item in item_dict:
        (weight, value) = item_dict[item]
    return (weights, values)

def time_knapsack_solver(solver_class, timing_iterations, item_dict = True):
    special_number = 1000
    solver = solver_class()
    size = []
    time = []
    for i in range(1,timing_iterations):
        new_problem = create_random(i, special_number)'
        if not item_dict:
            start_time = time.perf_counter()
            weights, values = item_dict_to_double_array(new_problem[0])
            solver.solve(new_problem[1], weights,values)
            end_time = time.perf_counter()
        else:
            start_time = time.perf_counter()
            solver.solve(new_problem[0], new_problem[1])
            end_time = time.perf_counter()
        size.append(i)
        time.append(end_time-start_time)

    return (size, time)


def time_solvers(solvers_plus_interface):
    iterations = 500
    plt.xlabel("Input problem size")
    plt.ylabel("Running time")
    for (solver, item_dict?) in solvers_plus_interface:
        (size, time) = time_knapsack_solver(solver,iterations, item_dict?))
        plt.plot(size, times)
        
    plt.show()
