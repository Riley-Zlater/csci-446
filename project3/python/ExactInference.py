# import itertools as it
import numpy as np

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
        
        var_types = v.getVarTypes()
        len_num_types = len(v.getVarTypes())

        array_shape = (len_num_types,)

        for parent in parents:
            array_shape += (len(parent.getVarTypes()), )

        new_factor_2 = np.zeros(array_shape)

        # print(new_factor_2)

        new_factor_3 = {}

        for i in range(len_num_types):
            for prob_list in prob_table:
                new_factor.append(prob_table[prob_list][i])
        
        new_factor_2 = np.reshape(new_factor, array_shape)
        
        for i in range(len_num_types):
            for prob_list in prob_table:
                prob_index = (var_types[i],) + prob_list
                new_factor_3[prob_index] = prob_table[prob_list][i]

        print(new_factor)
        print(new_factor_2)
        for factor in new_factor_3:
            print(str(factor) + " " + str(new_factor_3[factor]))
        # print(new_factor_3)

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
    
    