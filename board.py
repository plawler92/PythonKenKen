import itertools

class Board():
    def __init__(self, size):
        self.board_size = int(size)
    
    def subtract(self, target):
        #maybe put in a message for target = 0.
        ret = []
        for i in range(1, self.board_size + 1):
            for j in range(i + 1, self.board_size + 1):
                if j - i == target:
                    ret.append([j, i])
        return ret
        
    def divide(self, target):
        #maybe put in a message for target = 0
        ret = []
        for i in range(1, self.board_size + 1):
            for j in range(i + 1, self.board_size + 1):
                if j % i == 0 and j // i == target:
                    ret.append([j, i])
        return ret
        
    def add(self, target, num_values, allowed_repeats = 1):
        ret = []
        ranges = []
        for i in range(0, num_values):
            ranges.append(list(range(1, self.board_size + 1)))
        
        combinations = list(itertools.product(*ranges))
        for combo in combinations:
            if sum(combo) == target:
                lst = list(combo)
                lst.sort()
                if lst not in ret:
                    ret.append(lst)
                
        return self.remove_repeats(ret, allowed_repeats)
        
    def multiply(self, target, num_values, allowed_repeats = 1):
        ret = []
        ranges = []
        for i in range(0, num_values):
            ranges.append(list(range(1, self.board_size + 1)))
            
        combinations = list(itertools.product(*ranges))
        for combo in combinations:
            if self.product_of_list_values(combo) == target:
                lst = list(combo)
                lst.sort()
                if lst not in ret:
                    ret.append(lst)
        
        return self.remove_repeats(ret, allowed_repeats)
        
    def remove_repeats(self, lst, allowed_num_repeats):
        ret = []
        for i in lst:
            occurences = self.get_occurrences_in_list(i)
            if all(v <= allowed_num_repeats for v in occurences.values()):
                ret.append(i)
        return ret
                
    def get_occurrences_in_list(self, lst):
        ret = {}
        for i in lst:
            if i in ret.keys():
                ret[i] = ret[i] + 1
            else:
                ret[i] = 1
        return ret
        
    def product_of_list_values(self, lst):
        ret = 1
        for i in lst:
            ret = ret * i
        return ret