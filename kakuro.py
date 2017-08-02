from board import Board

class Kakuro(Board):
    def __init__(self):
        super().__init__(9)
        
    def get_combinations(self, target, numbers, disallowed=[]):
        ret = []
        combos = super().add(target, numbers)
        for combo in combos:
            if not any(v in disallowed for v in combo):
                ret.append(combo)
        return ret