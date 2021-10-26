import heapq

class KnapsackApproximator():

    def solve(item_dict, max_wt):
        names_and_ratios = []
        for item_key, item_value in item_dict.items():
            heapq.heappush(names_and_ratios,(item_value[0]/item_value[1],item_key, item_value))
            #item[0] is wt, item[1] is value. so i[0]/i[1] is the weight per value.

        approximation_wt = 0
        approximation_value = 0
        approximation_items = []
        not_found = True
        while(len(names_and_ratios)>0):
            #get the itme with the lowest weight/value (this is greedy!)
            (ratio, name, (weight, value)) = heapq.heappop(names_and_ratios)

            if (approximation_wt + weight < max_wt): #make sure we dont go over!
                approximation_wt += weight
                approximation_value += value
                approximation_items.append( name)

        return approximation_value
