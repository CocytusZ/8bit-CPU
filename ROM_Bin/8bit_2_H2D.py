"""
从8位2进制转换为3位10进制。生成一个文档提供给ROM导入。
    由于ROM导入是16进制, 但是TXT文档是10进制, 所以需要将“3位10进制结果”的数码以16进制转化为十进制再写入txt。

"""

data = ""
val = 0
for i in range(16):
    for j in range(16):
        ret = int(str(val), 16)
        data += str(ret) + " "
        val = val + 1
    data += "\n"
     
with open("8bit_2_3Dec.txt", "w") as f:
    f.write(data)