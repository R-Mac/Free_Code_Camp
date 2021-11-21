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
      print(index)
      if index > 0:
        top += "    "
        bottom += "    "
        line += "    "
        if show_answers:
          solution += "    "


      split_problem = problem.split()
      #Error checking for length of integers,if the integers exsist, and if the 
      #appropriate symbol was used
      
      if not(split_problem[0].isdigit() or split_problem[2].isdigit()):
        arranged_problems = "Error: Numbers must only contain digits."
        print("1!")
        break
      elif (len(split_problem[0]) or len(split_problem[2])) > 4:
        arranged_problems = "Error: Numbers cannot be more than four digits."
        print("2!")
        break
      elif split_problem[1] != "-" and split_problem[1] != "+":
        arranged_problems = "Error: Operator must be '+' or '-'."
        print("3!")
        break
      #appending starting section to their appropriate string
      bottom += split_problem[1] + " "
      if show_answers:
        solution += " " + eval(problem)

      if (len(split_problem[0]) > len(split_problem[2])):
        bottom += (" " * abs(len(split_problem[0])-len(split_problem[2])))  
        line += '-' * (len(split_problem[0]) + 2)
      else:
        top += (" " * abs(len(split_problem[0])-len(split_problem[2])))
        line += '-' * (len(split_problem[2]) + 2)

      top += split_problem[0]
      bottom += split_problem[2]
      print(top)  
      print(bottom)
      print(line)

    top = "\n"
    bottom = "\n"
    line = "\n"
    solution = "\n"
    arranged_problems = top + bottom + line
    if show_answers:
      arranged_problems += solution

    print(arranged_problems)

  return arranged_problems