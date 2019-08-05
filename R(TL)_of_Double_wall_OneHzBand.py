print("This is a small program that can calculate the sound insulation of double-walled walls.")
# 这是个可以计算双层板墙隔声量的小程序。
# 涉及变量：M1,M2 是两面板的面密度（Kg/m2）；Frequency是声波频率（Hz）；Rmid 是夹层里的隔声材料隔声量（dB）；deltaR是双层结构带来的附加隔声量（dB）；Rair 是墙板夹层只有空气时的总隔声量（dB）；Rtot 是含夹层材料的墙板总隔声量（dB）。

# 引入math库，用于引用数学函数来运算（主要是为了使用log函数）。
import math

# 说明该计算需要输入的数据。
print("M1 and M2 are the areal densities of the two panels, and Frequency is the acoustic frequency,Rmid is the sound insulation of the interlayer material")

# 以变量M记录输入的数据。
M = input("Please input 'M1(Kg/m2) M2(Kg/m2) Frequency(Hz) Rmid(dB)' (Separate the value entered with a space):")

# 把M里的字符串用空格来分割成多个变量赋值给列表Mlist。[Python键盘输入转换为列表的实例,https://www.jb51.net/article/142493.htm]
Mlist = M.split(" ")
#print(Mlist)

# for循环，把列表Mlist里的每个元素转成float值（浮点数值），使列表Mlist变成数组，可以用于数值计算。[Python键盘输入转换为列表的实例,https://www.jb51.net/article/142493.htm]
Mlist = [float(Mlist[i]) for i in range(len(Mlist))]
#print(Mlist)

# 将已转换为数组的键盘输入 赋值给公式中的各个变量
M1 = Mlist[0]
M2 = Mlist[1]
Frequency = Mlist[2]
Rmid = Mlist[3]

#另外一种一个一个地从键盘输入赋值的方法
# M1 = float(input("input M1:"))
# M2 = float(input("input M2:"))
# Frequency = float(input("input Frequency:"))
# Rmid = float(input("input Rmid:"))

# 双层板墙因双层结构获得的附加隔声量 [《建筑吸声材料与隔声材料》p80]
deltaR = 8

# 无夹层的双层板结构隔声量经验公式表达式 [《建筑吸声材料与隔声材料》p79]
R1 = 16 * math.log((M1 + M2),10) + 16 * math.log(Frequency,10) - 30
Rair = 16 * math.log((M1 + M2),10) + 16 * math.log(Frequency,10) - 30 + deltaR

# 在双层板基础上，添加了隔声量为 Rmid 的夹层材料后，总隔声量 Rtot 的表达式 [基于声电类比的多层结构隔声量算法《声学技术》29卷第4期 p345-348]
Rtot = 10 * math.log(2 * (10 ** (R1 / 10) + 10 ** (Rmid / 10)),10) + deltaR

# 显示结果
print("Sound insulation of double wall without inter-layer material added : Rair = %f dB" % round(Rair,1))
print("Sound insulation of double wall with inter-layer material added : Rtot = %f dB" % round(Rtot,1))
print("Sound insulation of double wall with interlayer material and keel gasket added : Rtot' = %f dB" % round(Rtot+2,1))