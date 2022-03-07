from django.shortcuts import render
from psutil import users
from .sudokusolver import SudokuSolver
#from django.http import HttpResponse
# Create your views here.

def sudoku_solver(response):
    if response.method == "POST":
        show_solution = True
    else:
        show_solution = False
    
    blockrows = range(3)
    blocknumbers = range(3) 
    linenumbers = range(3)
    fieldnumbers = linenumbers
    
    solved = SudokuSolver(response.POST)
    number_of_solutions = len(solved.formatted)
    
    if number_of_solutions <= 10:
        solutions = solved.formatted
    else:
        solutions = solved.formatted[:10]
    
    entry_dict = {"solutions": solutions,
                  "failsafe": solved.failsafe,
                  "show_solution": show_solution,
                  "number_of_solutions": number_of_solutions,
                  "blockrows": blockrows,
                  "blocknumbers": blocknumbers,
                  "linenumbers": linenumbers,
                  "fieldnumbers": fieldnumbers}


    return render(response, "main/sudoku_solver.html", entry_dict)