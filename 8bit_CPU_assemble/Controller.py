from PIN_DEF import *
import Assembly as ASM
import os
dirname = os.path.dirname(__file__)
file_path = os.path.join(dirname + "/build", 'micro.bin')

micro = [HLT for _ in range(2**16)]  # 初始化所有指令为HLT指令

for addr in range(2**16):
    ir = addr >> 8  # IR是指令的高8位
    psw = (addr >> 4) & 0x0F  # PSW是指令的第4到7位
    cyc = addr & 0x0F  # CYC是指令的低4位
    # 注意，此处CYC是位指令周期，4位也即16个周期。意味每个程序指令最多可以有16个微指令周期

    '''写入fetch指令'''
    if cyc < len(ASM.fetch):
        micro[addr] = ASM.fetch[cyc]
        
with open(file_path, 'wb') as f:
    for ins in micro:
        f.write(ins.to_bytes(4, byteorder='little'))

print("Compile instruction finished")