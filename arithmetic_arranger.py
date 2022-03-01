def arithmetic_arranger(*arguments):
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    #functions and expressions to support
    first_format = lambda x : (6 - len(x))*' '+x

    def second_format(x, o, y):
        if len(x)>=len(y):
            string = (4-len(x))*' '+o+ ' '+(len(x)-len(y))*' '+y
        else:
            string = ((4-len(y))*' '+o+' '+y)
        return string

    def third_format(x, y):
        lenghts = [len(x), len(y)]
        return ((4 - max(lenghts))*' '+(max(lenghts)+2)*'-')

    def fourth_format(x, o, y):
        int_x = int(x)
        int_y = int(y)
        if o == '-':
            result = int_x - int_y
        else:
            result = int_x + int_y
        str_result = str(result)
        return (6-len(str_result))*' '+str_result
    #raise the exeptions
    if len(arguments[0]) > 5:
        raise Exception('Error: Too many problems.')
    for problem in arguments[0]:
        x,o,y = problem.split() #o = operator
        if o not in ['+','-']:
            raise Exception("Error: Operator must be '+' or '-'.")
        if len(x)>4 or len(y)>4:
            raise Exception('Error: Numbers cannot be more than four digits.')
        try:
            x_int, y_int = int(x), int(y)
        except:
            raise Exception('Error: Numbers must only contain digits.')

        elements_lenght = [len(x), len(y)]
        first_line = first_line+(first_format(x)+' '*4)
        second_line = second_line +(second_format(x,o,y)+' '*4)
        third_line = third_line + (third_format(x, y)+' '*4)
        fourth_line = fourth_line + (fourth_format(x, o, y)+' '*4)

    l1 = first_line.rstrip()
    l2 = second_line.rstrip()
    l3 = third_line.rstrip()
    l4 = fourth_line.rstrip()
    arranged_problems =  l1+'\n'+l2+'\n'+l3+'\n'+l4
    try:
        arguments[1]
    except:
        arranged_problems = l1+'\n'+l2+'\n'+l3

    return arranged_problems


if __name__ == '__main__':
    print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
    print('   32         1      45      123      988\n'
    '- 698    - 3801    + 43    +  49    +  40\n'
    '-----    ------    ----    -----    -----\n'
    ' -666     -3800      88      172     1028')
