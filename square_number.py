def square_number(num):
    output = []
    sqrt_num = num ** 0.5
    if int(sqrt_num) ** 2 == num:
        return [num]
    else:
        sq_list = get_squares(num)
        for sq_num in sq_list:
            curr_op = square_number(num - sq_num) + [sq_num]
            if not output or len(curr_op) < len(output):
                output = curr_op
        return output
      
def get_squares(num):
    i = 1
    sq_list = []
    while i*i <= num:
        sq_list.append(i*i)
        i += 1
    return sq_list
    

for i in range(1,100):
	print i, square_number(i)
