def arithmetic_arranger(problems,show_answers = False):
  top = ""
  bottom = ""
  line = ""
  solution = ""
  if len(problems) > 5:
    arranged_problems = "Error: Too many problems."
  else:
    #appending beginning spaces to the top line
    top += "  "
    for index,problem in enumerate(problems):
      if index > 0:
        top = "    "
        bottom = "    "
        line = "    "
        if show_answers:
          solution = "    "


      split_problem = problem.split()
      #Error checking for length of integers,if the integers exsist, and if the 
      #appropriate symbol was used
      
      if not(split_problem[0].isdigit() or split_problem[2].isdigit()):
        arranged_problems = "Error: Numbers must only contain digits."
        break
      elif (len(split_problem[0]) or len(split_problem[2])) > 4:
        arranged_problems = "Error: Numbers cannot be more than four digits."
        break
      elif not(split_problem[0] == "-" or split_problem[0] == "+"):
        arranged_problems = "Error: Operator must be '+' or '-'."
        break

      #appending starting section to their appropriate string
      bottom += split_problem[1] + " "
      if show_answers:
        solution += " " + eval(problem)

      if (len(split_problem[0]) > len(split_problem[2])):
        bottom += (" " * abs(len(split_problem[0])-len(split_problem[2])))  
        line += '-' * len(split_problem[0])
      else:
        top += (" " * abs(len(split_problem[0])-len(split_problem[2])))
        line += '-' * len(split_problem[2])  
      
    top = "\n"
    bottom = "\n"
    line = "\n"
    solution = "\n"
    arranged_problems = top + bottom + line
    if show_answers:
      arranged_problems += solution

  return arranged_problems