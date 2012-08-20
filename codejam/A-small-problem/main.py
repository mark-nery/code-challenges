from small_problem import *

f = open('A-large-practice.in')
string = f.read()
f.close()

large_problem = SmallProblem(string)

ans_file = open('A-large-practice.out','w+')
ans_file.write(large_problem.print_results())
ans_file.close()

f = open('A-small-practice.in')
string = f.read()
f.close()

small_problem = SmallProblem(string)

ans_file = open('A-small-practive.out','w+')
ans_file.write(small_problem.print_results())
ans_file.close()
