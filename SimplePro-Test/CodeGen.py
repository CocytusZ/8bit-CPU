print(hex(0b0001111100000000))

codeList = []

# 给加法寄存器A赋值
codeList.append(0x1D03) ##读出到总线
codeList.append(0x1503) ##完成写入

# 给加法寄存器B赋值
codeList.append(0x1D0C)
codeList.append(0x150C)

codeList.append(0x1CD0) ## 将结果写到结果寄存器，并且内存控制器地址+1
codeList.append(0x1740) ## 从结果寄存器读出到总线，内存控制器写模式


out = ""

for i in range((len(codeList))):
    out += str((codeList[i])) + " "
    if i % 16 == 15: out += "\n"
    
with open("SimplePro-Test/ROM_PRO.txt", "w") as f:
    f.write(out)