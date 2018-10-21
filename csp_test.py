from constraint import Problem, AllEqualConstraint

problem = Problem()
problem.addVariables(["a", "b"], [[1,3], [2,4], [5,6]])
problem.addConstraint(AllEqualConstraint(), ["a", "b"])
solutions = problem.getSolutions()

print (solutions)