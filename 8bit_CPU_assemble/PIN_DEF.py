'''寄存器的0-10位'''

MSR = 1
MAR = 2
MDR = 3
RAM = 4
IR = 5
DST = 6
SRC = 7
A = 8
B = 9
C = 10
D = 11
DI = 12
SI = 13
SP = 14
BP = 15
CS = 16
DS = 17
SS = 18
ES = 19
VEC = 20
T1 = 21
T2 = 22

# Output pin definitions 即将数据送到总线上
# 读寄存器的值到总线，对应指令最低的5位
MSR_OUT = MSR
MAR_OUT = MAR
MDR_OUT = MDR
RAM_OUT = RAM
IR_OUT = IR
DST_OUT = DST
SRC_OUT = SRC
A_OUT = A
B_OUT = B
C_OUT = C
D_OUT = D
DI_OUT = DI
SI_OUT = SI
SP_OUT = SP
BP_OUT = BP
CS_OUT = CS
DS_OUT = DS
SS_OUT = SS
ES_OUT = ES
VEC_OUT = VEC
T1_OUT = T1
T2_OUT = T2

# Input pin definitions 写到寄存器中
_DST_SHIFT = 5 # 低5位控制读，高5位控制写，因此将寄存器OUT的引脚值左移5位即可得到对应的寄存器IN

MSR_IN = MSR << _DST_SHIFT 
MAR_IN = MAR << _DST_SHIFT 
MDR_IN = MDR << _DST_SHIFT 
RAM_IN = RAM << _DST_SHIFT 
IR_IN = IR << _DST_SHIFT 
DST_IN = DST << _DST_SHIFT 
SRC_IN = SRC << _DST_SHIFT 
A_IN = A << _DST_SHIFT 
B_IN = B << _DST_SHIFT 
C_IN = C << _DST_SHIFT 
D_IN = D << _DST_SHIFT 
DI_IN = DI << _DST_SHIFT 
SI_IN = SI << _DST_SHIFT 
SP_IN = SP << _DST_SHIFT 
BP_IN = BP << _DST_SHIFT 
CS_IN = CS << _DST_SHIFT 
DS_IN = DS << _DST_SHIFT 
SS_IN = SS << _DST_SHIFT 
ES_IN = ES << _DST_SHIFT 
VEC_IN = VEC << _DST_SHIFT 
T1_IN = T1 << _DST_SHIFT 
T2_IN = T2 << _DST_SHIFT 

'''寄存器11-14位'''
# DST和SRC的读写控制引脚
SRC_R = 0x01 << 10
SRC_W = 0x01 << 11
DST_R = 0x01 << 12
DST_W = 0x01 << 13

'''寄存器15-17位'''
# PC的读写控制引脚
PC_WE = 0x01 << 14 
PC_CS = 0x01 << 15 
PC_EN = 0x01 << 16

PC_OUT = PC_CS
PC_IN  = PC_WE | PC_CS 
PC_INC = PC_WE | PC_CS | PC_EN #PC自增

'''停止位，也即最高位（低32位）'''
HLT = 0x01 << 31