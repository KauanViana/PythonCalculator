def calc(first_operand, second_operand, operator):
    if operator == '+':
        return first_operand + second_operand   
    elif operator == '-':
        return first_operand - second_operand   
    elif operator == '*':
        return first_operand * second_operand   
    elif operator == '/':
        return first_operand / second_operand   

def first_reorder():
    value_index = 0
    for i in user_input:
        if i not in ['+', '-']:
            values.append('')
            values[value_index] += i
        else:
            value_index += 1
            operators.append(i)
        if '' in values:
            del values[-1]
            
def second_reorder():
    for i in values:
        value_index = 0
        sub_values = []
        sub_operators = []
        for y in range(len(i)):
            if i[y] not in ['*', '/']:
                sub_values.append('')
                sub_values[value_index] += i[y]
            else:
                value_index += 1
                sub_operators.append(i[y])
            if '' in sub_values:
                del sub_values[-1]
        sub_result = sub_values[0]
        for y in range(len(sub_operators)):
            sub_result = calc(float(sub_result), float(sub_values[y+1]), sub_operators[y])
        sub_results.append(sub_result)

print('Calculadora no Terminal\n')
user_input = input('=> ').replace(' ', '')
values = []
operators = []
sub_result = 0
sub_results = []

first_reorder()
second_reorder()

for i in range(len(values)):
    values[i] = sub_results[i]


result = values[0]
for i in range(len(operators)):
    result = calc(float(result), float(values[i+1]), operators[i])

result = float(result) if result - int(result) != 0 else int(result)
