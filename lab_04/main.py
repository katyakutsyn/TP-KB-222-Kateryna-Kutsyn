
input_str = '( 18 * 2 ) + ( 64 / 8 ) ^ 4'

digits = ('1','2','3','4','5','6','7','8','9','0')
opertions = ('+','-','*','/','^')

charr_arr = []
def is_num(unit):
    is_num = True
    for i in unit:
        if not i in digits:
            is_num = False
    return is_num

def get_opertion_power(opertion):
    if opertion in ('+','-'):
        return 0 
    if opertion in ('*','/'):
        return 1
    if opertion == '^':
        return 2

def get_rpn(input_str):
    stack = []
    out_str = []

    for i in input_str.split(' '):
        
        if is_num(i):
            out_str.append(i)
            continue
        if i == '(':
            stack.append(i)
            continue
        
        if i == ')':

            for j in reversed(stack):
                if j == '(':
                    del stack[stack.index(j)]
                    break
                out_str.append(j)
                del stack[stack.index(j)]
            continue

        if i in opertions:
            op_power = get_opertion_power(i)
            if len(stack) >= 1 and stack[-1] in opertions:

                last_op_in_stack_power = get_opertion_power(stack[-1])
                if last_op_in_stack_power >= op_power:
                    out_str.append(stack[-1])
                    del stack[-1]
            stack.append(i)

    for i in reversed(stack):
        out_str.append(i)

    return out_str
def calc_rpn(rpn):
    stack = []
    for i in rpn:
        if is_num(i):
            stack.append(i)
        else:
            num_2 = float(stack[-1])
            num_1 = float(stack[-2])
            match i:
                case '+':
                    ans = num_1 + num_2
                case '-':
                    ans = num_1 - num_2
                case '/':
                    ans = num_1 / num_2
                case '*':
                    ans = num_1 * num_2
                case '^':
                    ans = num_1 ** num_2
            del stack[-1]
            del stack[-1]
            stack.append(ans)
    return stack
if __name__ == '__main__':
    rpn = get_rpn(input_str)
    print(rpn)
    print(calc_rpn(rpn))