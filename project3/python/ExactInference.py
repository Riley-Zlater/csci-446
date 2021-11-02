import itertools as it

class ExactInference():
    def __init__(self) -> None:
        pass

    def check_list(self, item, l):
        for l_i in l:
            if item.getVarName() == l_i.getVarName():
                return True
        return False
        

    def order(self, vars):
        """
            Kahns algorithm for topological sorting
            https://en.wikipedia.org/wiki/Topological_sorting
        """
        l = []
        s = set()
        

        for var in vars:
            if len(var.getParents()) == 0:
                s.add(var)
        
        while len(s) != 0:
            n = s.pop()
            l.append(n)
            for m in n.getChildren():
                test = True
                parents = m.getParents()
                for p_i in parents:
                    if self.check_list(p_i, l) == False:
                        test = False
                if test:
                    s.add(m)
        
        return l
    
    def make_factor(self, v, e):
        
        new_factor = []
        
        prob_table = v.getProbTable()
        parents = v.getParents()
        
        len_num_types = len(v.getVarTypes())

        for i in range(len_num_types):
            for prob_list in prob_table:
                new_factor.append(prob_table[prob_list][i])

        print(new_factor)

        title_list = [p.getVarName() for p in parents]
        title_list.insert(0, v.getVarName())


        return tuple(title_list), new_factor

    
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

        factors = dict()
        bay_net = self.order(bay_net)
        for v in bay_net:
            fac_name, new_fac = self.make_factor(v,e)
            factors[fac_name] = new_fac
            # factors.append(self.make_factor(v, e, bay_net))
            if self.hidden_variable(v, X, e):
                factors = self.sum_out(X, v, factors)
        return self.normalize(self.pointwise_product(factors))
    
    