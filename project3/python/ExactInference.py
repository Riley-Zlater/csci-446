import itertools as it

class ExactInference():
    def __init__(self) -> None:
        pass

    def order(self, vars):
        """
            Kahns algorithm for topological sorting
            https://en.wikipedia.org/wiki/Topological_sorting
        """
        l = []
        s = set()

        for var in vars:
            if len(var.getParents()) is 0:
                s.add(var)
        
        while len(s) is not 0:
            n = s.pop()
            l.append(n)
            for m in n.getChildren():
                parents = m.getParents()
                if all(p_i in parents for p_i in l):
                    s.add(m)
        
        return l
    
    def make_factor(self, v, e):
        
        new_factor = []
        prob_table = v.getProbTable()
        parents = v.getParents()
        
        

        parent_types = []
        for parent in parents:
            if parent not in e:
                parent_types.append(list(parent.getVarTypes()))
        
        possible_combinations = list(it.product(*parent_types))

        

        return new_factor
    
    def hidden_variable(self, X, V, e):
        if X != V and X not in e:
            return True
        return False

    def sum_out(self, V, factors):
        return factors
    
    def pointwise_product(self, factors):
        return factors
    
    def normalize(self, factors):
        normalized_factors = []
        for x in factors:
            normalized_factors.append(x * 1/sum(factors))
        return normalized_factors

    def elimination_ask(self, X, e, bay_net):

        factors = []
        bay_net = self.order(bay_net)
        for v in bay_net:
            factors.append(self.make_factor(v, e, bay_net))
            if self.hidden_variable(v, X, e):
                factors = self.sum_out(X, v, factors)
        return self.normalize(self.pointwise_product(factors))
    
    