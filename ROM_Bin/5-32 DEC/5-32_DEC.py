"""简述
该程序用于生成一个基于ROM的5/32译码器电路的真值表。

Logic Circuit 加载时使用LoadText-HexDecimal。最后一位会溢出。需要手动在txt文件里面改小，然后再加载完成后在ROM
里面改回来。
"""

outs = ""

for i in range(32):
    val = 0x01 << i
    outs = outs + int.to_bytes(val,4,'big').hex() + " "
    if i % 16 == 15:
        outs = outs.rstrip(" ")  # 去掉最后一个空格
        outs = outs + "\n"
outs.rstrip("\n")  # 去掉最后一个换行符

with open("5-32 DEC/5-32_DEC.txt", "w") as f:
    f.write(outs)