def arithmetic_arranger(problems,solve123=None):

  top = []
  bottom = []
  lines = []
  solving = []
  if len(problems)>5:
    return "Error: Too many problems."

  for problem in problems:

    biggest =  0
    #only + -
    for sign in problem:
      if sign =="/" :
        return "Error: Operator must be '+' or '-'."




    firstnumpos = problem.find("+")

    if firstnumpos == -1:
      firstnumpos = problem.find("-")

    firstnum = problem[:firstnumpos]
    firstnum = firstnum.rstrip()
    secondnumstart = firstnumpos+2
    secondnum = problem[secondnumstart:]
    secondnum.strip()
    mark = problem[firstnumpos:secondnumstart]
    mark = mark.rstrip()
    if mark.find("/") != -1:
      return "Error: Operator must be '+' or '-'." 
    else:
      pass
      #only digits
    try:
      firstnum = int(firstnum)
      secondnum = int(secondnum)
    except:
      return "Error: Numbers must only contain digits."

      #formating
    if firstnum>secondnum:
      firstnum = str(firstnum)
      secondnum = str(secondnum)
      biggest=len(firstnum)
      smallest=len(secondnum)
      dif = biggest-smallest
      firstnum = int(firstnum)

      secondnum = int(secondnum)
    if secondnum>firstnum:
      firstnum = str(firstnum)
      secondnum = str(secondnum)
      biggest=len(secondnum)
      smallest=len(firstnum)
      dif = biggest-smallest
      firstnum = int(firstnum)
      secondnum = int(secondnum)
    equalline  = "-"*(biggest+2)
    #additional condition
    if solve123 is True:
      if mark =="-":


        solution = firstnum-secondnum
      if mark =="+":
        solution = firstnum+secondnum 


      #4 digits
    if (type(firstnum) is int) and (type(secondnum) is int):
      if (firstnum>9999)or(secondnum>9999):
        return "Error: Numbers cannot be more than four digits."

    elif (type(firstnum) is  str) or (type(secondnum) is str) :

      return "Error: Numbers must only contain digits."
    #print

    if biggest==len(str(firstnum)):

      #print(" ",firstnum)
      firstline = " "+" "+str(firstnum)



    else:
      #print(" "*(dif+1),firstnum)
      firstline = " "*(dif+1) +" "+str(firstnum)
    if biggest==len(str(secondnum)):
      #print(mark,secondnum,"")
      secondline = mark+" "+str(secondnum)+" "+""

    else:
      #print(mark," "*(dif-1),secondnum)
      secondline = mark+ " "*(dif-1)+ " "+ str(secondnum)



    #solution
    #print(firstline)
    #print(secondline)
    #print(equalline)

    top.append(firstline)
    bottom.append(secondline)
    lines.append(equalline)




    if solve123 is True:

      solutline = " "+" "+str(solution)
      #print(solutline)
      solving.append(solutline)
  arranged_problems = '\n'.join(['    '.join(i)
                                   for i in (top, bottom, lines)])
  if solve123:
    arranged_problems += '\n' + '    '.join(solving)








  return arranged_problems
