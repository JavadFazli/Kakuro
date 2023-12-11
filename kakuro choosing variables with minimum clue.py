import time


maxr=8
class CSP: 
    def __init__(self, variables, Domains,constraints): 
        self.variables = variables 
        self.domains = Domains 
        self.constraints = constraints 
        self.solution = None
        self.min_const={}
    def order_domain_values(self, var, assignment): 
        return self.domains[var]
        
    
    def solve(self): 
        self.min_constraints()
        assignment = {} 
        self.solution = self.backtrack(assignment) 
        return self.solution 
    def min_constraints(self):
        for constraint in self.constraints:
            for var in constraint[1:]:
                if var in self.min_const:
                    self.min_const[var]=max(self.min_const[var],constraint[0])
                else:
                    self.min_const[var]=constraint[0]

    def backtrack(self, assignment): 
        if len(assignment) == len(self.variables): 
            return assignment 
        
        var = self.select_unassigned_variable(assignment) 
        for value in self.order_domain_values(var, assignment) : 
            if self.is_consistent(var, value, assignment): 
                assignment[var] = value 
                result = self.backtrack(assignment) 
                if result is not None: 
                    return result 
                del assignment[var] 
        return None

    
     
    def select_unassigned_variable(self, assignment): 
        unassigned_vars = [var for var in self.variables if var not in assignment] 
        return min(unassigned_vars, key=lambda var: self.min_const[var]) 
    


    
    def is_consistent(self, var, value, assignment):
        for constraint in self.constraints:
            if var in constraint:
                    clue_sum = constraint[0]
                    clue_cells = constraint[1:]
                    clue_values = [assignment[v] for v in assignment if v in  clue_cells]
                    if value in clue_values:
                        return False
                    if len(clue_values) == len(clue_cells) - 1:
                        if sum(clue_values) + value != clue_sum:
                            return False
        return True







# clue = [
#     [5, (2, 1), (3, 1)],
#     [12, (1, 2), (1, 3), (1, 4)],
#     [20, (1, 2), (2, 2), (3, 2), (4, 2)],
#     [3, (1,3),(2, 3)],
#     [23, (1, 4), (2, 4), (3, 4)],
#     [24, (2, 5), (3, 5),(4,5)],
#     [16, (1, 6), (1, 7)],
#     [12, (1, 6), (2, 6)],
#     [16, (1, 7), (2, 7)],

#     [41, (2, 1), (2, 2),(2,3),(2,4),(2,5),(2,6),(2,7)],

#     [3, (3, 1), (3, 2)],
#     [13, (3, 4), (3, 5)],
#     [24, (4, 3), (5, 3),(6,3)],
#     [11, (4, 6), (5, 6), (6, 6), (7, 6)],

#     [17, (4, 2), (4, 3)],
#     [23, (5, 4), (6, 4), (7, 4)],
#     [10, (4, 5), (4, 6)],
#     [16, (5, 7), (6, 7)],

#     [14, (6, 1), (7, 1)],
#     [5, (6, 2), (7, 2)],
#     [16, (5, 3), (5, 4)],
#     [17, (6, 5),(7, 5)],
#     [11, (5, 6), (5, 7)],
#     [42, (6, 1), (6, 2), (6, 3), (6, 4), (6, 5),(6, 6),(6, 7)],
    
#     [10, (7, 1), (7, 2)],
#     [22, (7, 4), (7,5),(7,6)]
# ]
# board = [
#          ['b','b','b','b','b','b','b','b'],
#          ['b','b',0,0,0,'b',0,0],
#          ['b',0,0,0,0,0,0,0],
#          ['b',0,0,'b',0,0,'b','b'],
#          ['b','b',0,0,'b',0,0,'b'],
#          ['b','b','b',0,0,'b',0,0],
#          ['b',0,0,0,0,0,0,0],
#          ['b',0,0,'b',0,0,0,'b']
#          ]
clue = [
    [40, (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4),(7,4)],
    [3, (1, 5), (2, 5)],

    [6, (1, 4), (1, 5)],
    [8, (2,3),(3, 3),(4,3)],

    [7, (2, 3), (2, 4), (2, 5)],
    [3, (3, 6), (4, 6)],
    [14, (3, 7), (4, 7)],

    [6, (4, 1), (5, 1)],
    [4, (4, 2), (5, 2)],
    [10, (3, 3), (3, 4)],
    [24, (4, 5), (5, 5),(6, 5)],
    [9, (3, 6), (3, 7)],

    [28, (4, 1), (4, 2),(4,3),(4,4),(4,5),(4,6),(4,7)],

    [3, (5, 1), (5, 2)],
    [17, (5, 4), (5, 5)],
    [17, (6, 3), (7, 3)],

    [23, (6, 3), (6, 4), (6, 5)],

    [16, (7, 3), (7, 4)],

]
board = [
         ['b','b','b','b','b','b','b','b'],
         ['b','b','b','b',0,0,'b','b'],
         ['b','b','b',0,0,0,'b','b'],
         ['b','b','b',0,0,'b',0,0],
         ['b',0,0,0,0,0,0,0],
         ['b',0,0,'b',0,0,'b','b'],
         ['b','b','b',0,0,0,'b','b'],
         ['b','b','b',0,0,'b','b','b']
         ]
variables = [] 
for i in range(0,maxr): 
     for j in range(0,maxr):
          if board[i][j]==0:
               variables.append((i,j))
Domains = {var: list(range(1, 10)) for var in variables} 
csp = CSP(variables, Domains, clue) 
sol = csp.solve()
print(sol)
for c in sol.keys():
    board[c[0]][c[1]]=sol[c]
for i in range(maxr):
    for j in range(maxr):
        print(board[i][j],end=' ')
    print()
print('process_time (s):',time.process_time())