def arithmetic_arranger(problems,show_answers = False):
  top = ""
  bottom = ""
  line = ""
  solution = ""
  error_status = False
  if len(problems) > 5:
    arranged_problems = "Error: Too many problems."
    error_status = True
  else:
    #appending beginning spaces to the top line
    top += "  "
    for index,problem in enumerate(problems):
      #print(index)
      if index > 0:
        top += "      "
        bottom += "    "
        line += "    "
        if show_answers:
          solution += "    "


      split_problem = problem.split()
      #Error checking for length of integers,if the integers exsist, and if the 
      #appropriate symbol was used
      
      if not(split_problem[0].isdigit()) or not(split_problem[2].isdigit()):
        arranged_problems = "Error: Numbers must only contain digits."
        error_status = True
        print("3!")
        break
      elif (len(split_problem[0]) > 4) or (len(split_problem[2]) > 4):
        arranged_problems = "Error: Numbers cannot be more than four digits."
        error_status = True
        print("2!")
        break
      elif split_problem[1] != "-" and split_problem[1] != "+":
        arranged_problems = "Error: Operator must be '+' or '-'."
        error_status = True
        print("4!")
        break
      #appending starting section to their appropriate string
      bottom += split_problem[1] + " "


      if (len(split_problem[0]) > len(split_problem[2])):
        bottom += (" " * abs(len(split_problem[0])-len(split_problem[2])))  
        line += '-' * (len(split_problem[0]) + 2)
        if show_answers:
          solution +=  str(eval(problem)).rjust(len(split_problem[0]) + 2)
      else:
        top += (" " * abs(len(split_problem[0])-len(split_problem[2])))
        line += '-' * (len(split_problem[2]) + 2)
        if show_answers:
          solution +=  str(eval(problem)).rjust(len(split_problem[2]) + 2)

      top += split_problem[0]
      bottom += split_problem[2]

    if not error_status:
      top += "\n"
      bottom += "\n"
      arranged_problems = top + bottom + line
      if show_answers:
        arranged_problems += "\n"
        arranged_problems += solution

  print(arranged_problems)
  return arranged_problems