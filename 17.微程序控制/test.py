WE_A = 1 << 0
CS_A = 1 << 1

WE_B = 1 << 2
CS_B = 1 << 3

WE_C = 1 << 4
CS_C = 1 << 5

ALU_OP = 1 << 6
ALU_EN = 1 << 7

WE_PC = 1 << 8
EN_PC = 1 << 9
CS_PC = 1 << 10

WE_MC = 1 << 11
CS_MC = 1 << 12

ANS = WE_B | CS_B | CS_MC | WE_PC | EN_PC | CS_PC
ADD = CS_MC | WE_MC | ALU_EN
MOV_C = CS_C | WE_C | ALU_EN

print(hex(MOV_C))