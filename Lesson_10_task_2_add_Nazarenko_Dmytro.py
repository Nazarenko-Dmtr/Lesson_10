mult_list = []
sum_list = []
for i in range (100, 1000):
    for j in range (100, 1000):
        my_list = list(str(i*j))
        reversed_list = my_list[::-1]
        if reversed_list == my_list:
            mult_list.append(i*j)
            sum_list.append(i+j)
# i_max + j_max = max(sum_list); i_max*j_max = max(mult_list)
# i_max = max(sum_list) - j_max;
# j_max*(max(sum_list) - j_max) - max(mult_list) = 0
# j_max**2 - max(sum_list)*j_max + max(mult_list) = 0
discr = max(sum_list)**2 - 4*max(mult_list) 
i_max = int((max(sum_list) + discr** .5) / 2)
j_max = int(max(sum_list) - i_max)
print (i_max, j_max, max(mult_list))