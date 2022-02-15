def sequence (line):

    line = list(map(int, line.split(',')))
    if line[-1] - line[-2] == line[1] - line[0]:
        line.append(line[-1] + (line[-1] - line[-2]))
    elif line[-1] / line[-2] == line[1] / line[0]:
        line.append(line[-1] * (line[-1] // line[-2]))
    elif line[-1]** .5 - line[-2]** .5 == line[1]** .5 - line[0]** .5:
        line.append(int((line[-1]** .5 + (line[-1]** .5 - line[-2]** .5))**2))
    elif round(line[-1]**(1/3)) - round(line[-2]**(1/3)) == round(line[1]**(1/3)) - round(line[0]**(1/3)):
        line.append(round((line[-1]**(1/3) + (line[-1]**(1/3)- line[-2]**(1/3)))**3))
    return (line[-1])
    
x = input("Enter sequence: ")
print (sequence (x))