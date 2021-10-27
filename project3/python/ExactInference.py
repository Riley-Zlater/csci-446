

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
    
    def make_factor(self, V, e):
        return (V,e)
    
    def hidden_variable(self, V):
        return True

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
        for v in self.order(bay_net):
            factors.append(self.make_factor(v,e))
            if self.hidden_variable(v):
                factors = self.sum_out(v, factors)
        return self.normalize(self.pointwise_product(factors))
    
    