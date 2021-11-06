import itertools as it
import numpy as np
import copy

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

        # array_shape = (len_num_types,)

        # for parent in parents:
        #     array_shape += (len(parent.getVarTypes()), )

        # new_factor_2 = np.zeros(array_shape)

        new_factor_3 = {}

        for i in range(len_num_types):
            for prob_list in prob_table:
                new_factor.append(prob_table[prob_list][i])
        
        # new_factor_2 = np.reshape(new_factor, array_shape)
        
        for i in range(len_num_types):
            for prob_list in prob_table:
                prob_index = (var_types[i],) + prob_list
                new_factor_3[prob_index] = prob_table[prob_list][i]

        # print(new_factor)
        # print(new_factor_2)
        # for factor in new_factor_3:
        #     print(str(factor) + " " + str(new_factor_3[factor]))
        # print(new_factor_3)

        title_list = [p.getVarName() for p in parents]
        title_list.insert(0, v.getVarName())


        return tuple(title_list), new_factor_3

    
    def hidden_variable(self, X, V, e):
        if X.getVarName() != V.getVarName() and X not in e:
            return True
        return False
    
    def get_var_types(self, name, bay_net):
        for node in bay_net:
            if node.name == name:
                return list(node.getVarTypes())
        
        return []

    def sum_out(self, V, factors, bay_net):
        factors_to_return = copy.deepcopy(factors)
        reduced_factors = dict()
        temp_new_factor_vars = []
        temp_new_factor_var_types = []
        new_factor_vars = []
        new_factor_var_types = []

        for factor in factors:
            if V in list(factor):
                reduced_factors[factor] = factors[factor]
                del factors_to_return[factor]          

        for var_names in reduced_factors:
            for var in var_names:
                if var not in temp_new_factor_vars:
                    temp_new_factor_vars.append(var)
                    temp_new_factor_var_types.append(self.get_var_types(var, bay_net))
                if var != V and var not in new_factor_vars:
                    new_factor_vars.append(var)
                    new_factor_var_types.append(self.get_var_types(var, bay_net))

        
        enumerated_combinations = list(it.product(*temp_new_factor_var_types))
        enumerated_combinations_2 = list(it.product(*new_factor_var_types))

        temp_new_factor_dict = dict()
        for comb in enumerated_combinations:
            temp_new_factor_dict[comb] = []
        
        new_factor_dict = dict()
        for comb in enumerated_combinations_2:
            new_factor_dict[comb] = []


        for temp_factor_vars in temp_new_factor_dict:
            for red_factors in reduced_factors:
                r_fac = reduced_factors[red_factors]
                for factor in r_fac:
                    count = 0
                    for i in range(len(factor)):
                        idex = temp_new_factor_vars.index(red_factors[i])
                        if temp_factor_vars[idex] == factor[i]:
                            count += 1
                    if count == len(factor):
                        temp_new_factor_dict[temp_factor_vars].append(r_fac[factor])

        
        for t in temp_new_factor_dict:
            temp_new_factor_dict[t] = np.prod(temp_new_factor_dict[t])
        
        
        for temp_factor_vars in temp_new_factor_dict:
            for factor_vars in new_factor_dict:
                count = 0
                for i in range(len(factor_vars)):
                    index = temp_new_factor_vars.index(new_factor_vars[i])
                    if temp_factor_vars[index] == factor_vars[i]:
                        count += 1
                if count == len(factor_vars):
                    new_factor_dict[factor_vars].append(temp_new_factor_dict[temp_factor_vars])

        for t in new_factor_dict:
            new_factor_dict[t] = np.sum(new_factor_dict[t])
            print(str(t) + ":  " + str(new_factor_dict[t]))

        factors_to_return[tuple(new_factor_vars)] = new_factor_dict

        return factors_to_return
    
    def pointwise_product(self, factors, bay_net):
        # factors_to_return = copy.deepcopy(factors)
        # reduced_factors = dict()
        temp_new_factor_vars = []
        temp_new_factor_var_types = []
        # new_factor_vars = []
        # new_factor_var_types = []

        # for factor in factors:
        #     if V in list(factor):
        #         reduced_factors[factor] = factors[factor]
        #         del factors_to_return[factor]          

        for var_names in factors:
            for var in var_names:
                if var not in temp_new_factor_vars:
                    temp_new_factor_vars.append(var)

                    # FAKE INPUT FOR TESTING
                    # temp_new_factor_var_types.append()

                    # THIS IS THE REAL INPUT
                    temp_new_factor_var_types.append(self.get_var_types(var, bay_net))
                # if var != V and var not in new_factor_vars:
                #     new_factor_vars.append(var)
                #     new_factor_var_types.append(self.get_var_types(var, bay_net))

        # print(temp_new_factor_vars)
        enumerated_combinations = list(it.product(*temp_new_factor_var_types))
        # print(enumerated_combinations)
        # enumerated_combinations_2 = list(it.product(*new_factor_var_types))

        temp_new_factor_dict = dict()
        for comb in enumerated_combinations:
            temp_new_factor_dict[comb] = []
        
        # new_factor_dict = dict()
        # for comb in enumerated_combinations_2:
        #     new_factor_dict[comb] = []


        for temp_factor_vars in temp_new_factor_dict:
            for red_factor in factors:
                r_fac = factors[red_factor]
                for f in r_fac:
                    count = 0
                    for i in range(len(f)):
                        idex = temp_new_factor_vars.index(red_factor[i])
                        if temp_factor_vars[idex] == f[i]:
                            count += 1
                    if count == len(f):
                        temp_new_factor_dict[temp_factor_vars].append(r_fac[f])

        
        # for t in temp_new_factor_dict:
        #     print(str(t) + " " + str(temp_new_factor_dict[t]))
            # temp_new_factor_dict[t] = np.prod(temp_new_factor_dict[t])

        # print()

        for t in temp_new_factor_dict:
            temp_new_factor_dict[t] = np.prod(temp_new_factor_dict[t])

        return temp_new_factor_dict
    
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
                factors = self.sum_out(v.getVarName(), factors, bay_net)
        return self.normalize(self.pointwise_product(factors, bay_net))
    
    