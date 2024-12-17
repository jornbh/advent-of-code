import numpy as np
import math
from collections import defaultdict
import json
import matplotlib.pyplot as plt
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]

outputs = []

def get_reg(line):
    return int(line.split()[-1])
def get_registers(lines):
    a = get_reg(lines[0])
    b = get_reg(lines[1])
    c = get_reg(lines[2])
    return a,b,c

# Set and reset the registers
a,b,c = get_registers(lines)
program_line = lines[4]
print("program_line = " , program_line)
program_string = program_line.split()[-1].strip()
print("program_string = " , program_string)
program_substrings = program_string.split(",")
program = [int(el)   for ind,el in enumerate(program_substrings )]
print("program = " , program)


#    Combo operands 0 through 3 represent literal values 0 through 3.
#    Combo operand 4 represents the value of register A.
#    Combo operand 5 represents the value of register B.
#    Combo operand 6 represents the value of register C.
#    Combo operand 7 is reserved and will not appear in valid programs.




def literal(arg):
    return arg





#The adv instruction (opcode 0) performs division. The numerator
#is the value in the A register. The denominator is found by
#raising 2 to the power of the instruction's combo operand. (So, an
#operand of 2 would divide A by 4 (2^2); an operand of 5 would
#divide A by 2^B.) The result of the division operation is
#truncated to an integer and then written to the A register.
def adv(arg, num=None):
    global a
    if num is None:
        num =  a
    den = pow(2, combo(arg))
    result  =  ( num // den )
    a = result

#The bxl instruction (opcode 1) calculates the bitwise XOR of
#register B and the instruction's literal operand, then stores the
#result in register B.
def bxl(arg):
    global b
    result = b ^ literal(arg)
    b = result


#The bst instruction (opcode 2) calculates the value of its combo
#operand modulo 8 (thereby keeping only its lowest 3 bits), then
#writes that value to the B register.
def bst(arg):
    global b
    result = combo(arg) % 8
    b = result



# The jnz instruction (opcode 3) does nothing if the A register is 0. However, if
# the A register is not zero, it jumps by setting the instruction pointer to the
# value of its literal operand; if this instruction jumps, the instruction
# pointer is not increased by 2 after this instruction.
def jnz(arg):
    if a == 0:
        return
    return literal(arg)

# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and
# register C, then stores the result in register B. (For legacy reasons, this
# instruction reads an operand but ignores it.)
def bxc(_arg):
    global b
    global c
    result = b ^ c
    b = result

# The out instruction (opcode 5) calculates the value of its combo operand
# modulo 8, then outputs that value. (If a program outputs multiple values,
# they are separated by commas.)
def out(arg):
    result = combo(arg) % 8
    outputs.append(result)

# The bdv instruction (opcode 6) works exactly like the adv instruction except
# that the result is stored in the B register. (The numerator is still read from the A register.)
def bdv(arg):
    global a
    global b
    num = a
    den = pow(2, combo(arg) )
    result  =  ( num // den )
    b = result

# The cdv instruction (opcode 7) works exactly like the adv instruction except
# that the result is stored in the C register. (The numerator is still read from
                                          # the A register.)
def cdv(arg):
    global a
    global c
    num = a
    den = pow(2, combo(arg)  )
    result  =  ( num // den )
    c = result


# Main reference sheet
#################################
def combo(arg):
    retval = {
    # Litterals
    0 : 0,
    1 : 1,
    2 : 2,
    3 : 3,
    # Registers
    4 : a ,
    5 : b ,
    6 : c ,
    # 7 is a failure
    }[arg]
    return retval

op2foo = {
        0: adv, # A << op to A
        1: bxl, # b xor to b
        2: bst, # mod 8 to b
        3: jnz, # Jump if A!=0
        4: bxc, # B xor C to B
        5: out, # Print A mod 8
        6: bdv, # A << op to B
        7: cdv, # A << op to C
        }

#################################
def execute_program(program, a_par,b_par,c_par):
    global a,b,c
    a = a_par
    b = b_par
    c = c_par
    global outputs
    outputs = []
    pc = 0
    while pc < len(program):
        op = program[pc]
        arg = program[pc +1]
        ret = op2foo[op](arg)
        if ret is None:
            pc +=2
        else:
            pc = ret
    return outputs

def attempt_program(i):
    a,b,c = get_registers(lines)
    outputs = execute_program(program, i,b,c)
    return outputs

#i = 0
#outputs = execute_program(program, i,b,c)
#while outputs != program:
#    outputs = attempt_program(i)
#    print("outputs = " , oct(i), outputs)
#    i +=1

#assert program == outputs, f"{program ,  outputs}"

def print_outputs(outputs):
    outputs_mapped_1 = [str(el)  for ind,el in enumerate(outputs)]

    res_string = ",".join(outputs_mapped_1)
    print("res_string = " , res_string)
    ref_string = "4,6,3,5,6,3,5,2,1,0"

def octal_digits_to_num(octal_list):
    out = 0
    for el in octal_list:
        out *= 8
        out += el
    return out


# Test octal transformation
assert octal_digits_to_num([2,1]) == 0o21
assert octal_digits_to_num([3,2,1]) == 0o321

def add_to_basis(basis, new_num):
    return    [new_num] + basis
#    return   basis + [new_num]
basis = []
#for j in range(len(program)):
# The last num may be wierd?
depth = 1

"""
DESCRIPTION OF EXPERIMENT


The algorithm can be show to take some bits form the A register, do some stuff
and then throw the rest of it. As a result, you can build the output vector using bit-shifting.


But since the way it is done was kind of hard to undestand, I did it manually

1. The lowest parts of the input only changes the leftmost part of the output
2. If you find the first 2 parts, you can look for the next
3. There are some times multiple candidates, not all of them lead to somewhere sensible, so you may have to try all of them
4. By going 2 octals at a time, you can work your way back to the original.
5. Look at the lines bellow to see  how you may progress. Some of the commented out or masked lines are dead ends


"""

base = 0o1035 * (2**6)
base = 0o103551 * (2**6)

base = 0o10355100* (2**6)
#base = 0o10355102* (2**6)
#base = 0o10355162* (2**6)
base = 0o1035510065* (2**6)

#0o1035510066

base = 0o103551006513* (2**6)


base = 0o10355100651362* (2**6)
base = 0o10355100651365* (2**6)
base = 0o10355100651367* (2**6)

# NOTE: This is the solution on octal form
result = 0o1035510065136764

0o1035510065136764
37221274271220
#
#

exp = 0
for i in range(2**6):
    diff = (2**exp) *i
    outputs = attempt_program(base+diff)
    print("outputs = " , oct(base+diff), outputs)
print("outputs = " , outputs)

raise Exception("I was not able to solve this automatically, so a semi-manual solution was faster. See the code for details: The result was 37221274271220")
def search_for_possibilities(basis, depth):
    possibilities = []
    any_true = False
    for end_val in range(2**10):
        attempt =  add_to_basis(basis ,end_val)
        program_int = octal_digits_to_num(attempt)
        outputs = attempt_program(program_int)
        ref = program[:depth]
        ev = ref == outputs[:depth]
        if ev:
            any_true = True
            possibilities.append(end_val)
    return possibilities

def search_rec(basis, program, depth):
    if depth == len(program):
        return {basis}
    possibilities = search_for_possibilities(basis, depth)
    # Only care about the last byte
    possibilities_mapped_2 = {(el % 8)   for ind,el in enumerate(possibilities)}
    possibilities_mapped_3 = [basis + [el]   for ind,el in enumerate(possibilities_mapped_2)]
    total_pos = {}
    for new_basis in possibilities_mapped_3:
        new_pos = search_rec( new_basis, program, depth +1 )
        total_pos.update(new_pos)
    return total_pos





pos = search_rec(basis, program , 1)
print("pos = " , pos)

#for pos in possibilities_mapped_2:

# 16 levels are required






#2,4, B=A mod 8  # Take the lower 3 bits
#1,2, B=B^2 # Flip the middle
#7,5, C=A/2**5
#4,7, B=B^C
#1,3, B=B^3
#5,5, print
#0,3, A=A//2**3
#3,0  Jump if A!=0
