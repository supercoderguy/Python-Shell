def init():
    equation = input('Enter equation (must be \'x + y\'): ')
    equationparts = []
    equationparts = equation.split(' ')
    if equationparts[1] == '+':
        ans = int(equationparts[0]) + int(equationparts[2])
    elif equationparts[1] == '-':
        ans = int(equationparts[0]) - int(equationparts[2])
    elif equationparts[1] == '*':
        ans = int(equationparts[0]) * int(equationparts[2])
    elif equationparts[1] == '/':
        ans = int(equationparts[0]) / int(equationparts[2])
    else:
        ans = 'Error'
    print(ans)