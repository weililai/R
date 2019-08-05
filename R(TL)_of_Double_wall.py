print("This is a small program that can calculate the sound insulation of double-walled walls.")
# 这是个可以计算双层板墙隔声量的小程序。
# 涉及变量：M1,M2 是两面板的面密度（Kg/m2）；Frequency是声波频率（Hz）；Rmid 是夹层里的隔声材料隔声量（dB）；deltaR是双层结构带来的附加隔声量（dB）；Rair 是墙板夹层只有空气时的总隔声量（dB）；Rtot 是含夹层材料的墙板总隔声量（dB）。

# 引入math库，用于引用数学函数来运算（主要是为了使用log函数）。
import math

# 倍频带和1/3倍频带各带的中心频率
octave_band = [125,250,500,1000,2000,4000]
one_third_octave_band = [100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150,]

# 在屏幕说明该计算需要输入的数据。
print("M1 and M2 are the areal densities of the two panels, and Frequency is the acoustic frequency,Rmid is the sound insulation of the interlayer material")

# 以变量记录键盘输入的数据。
M = input("Please input 'M1(Kg/m2) M2(Kg/m2)' (Separate the value entered with a space):")
Fr = input("Octave or 1/3 Octave ? (Enter 1 or 1/3):")
Rmid = input("Rmid(dB) (Separate the value entered with a space):")

# 把 M 和 Rmid 里的字符串用空格来分割成多个变量赋值给 列表M 和 列表Rmid。[Python键盘输入转换为列表的实例,https://www.jb51.net/article/142493.htm]
M = M.split(" ")
Rmid = Rmid.split(" ")

# for循环，把 列表M 和 列表Rmid 里的每个元素转成float值（浮点数值），使列表变成数组，便于之后的数值计算。[Python键盘输入转换为列表的实例,https://www.jb51.net/article/142493.htm]
M = [float(M[i]) for i in range(len(M))]
Rmid = [float(Rmid[i]) for i in range(len(Rmid))]
# 根据问题‘Octave or 1/3 Octave ?’输入的频程选项来决定 Frequency 使用哪一个频带
if Fr == "1":
    Frequency = octave_band
elif Fr == "1/3":
    Frequency = one_third_octave_band
else:
    Frequency = [float(Fr)]
band_center_frequency = 'band center frequency:'+str(Frequency)
print(band_center_frequency)  # 显示当前选择的频程
# 上面这段运行后，可以得到 M 、Frequency、Rmid 三个数组（或向量？），他们就是处理好的的输入数据。

# 双层板墙因双层结构获得的附加隔声量，这里的附加隔声量表述有待改进，因为这个量是与板隙的大小有关的 [《建筑吸声材料与隔声材料》p80]
deltaR = 8
# 无夹层的双层板结构隔声量经验公式表达式 [《建筑吸声材料与隔声材料》p79]
R1 = [float(16 * math.log((M[0] + M[1]),10) + 16 * math.log(Frequency[i],10) - 30) for i in range(len(Frequency))] # R1 是没考虑附加隔声量的
Rair = [float(R1[i] + deltaR) for i in range(len(R1))]
# 在双层板基础上，添加了隔声量为 Rmid 的夹层材料后，总隔声量 Rtot 的表达式 [基于声电类比的多层结构隔声量算法《声学技术》29卷第4期 p345-348]
Rtot = [float(10 * math.log(2 * (10 ** (R1[i] / 10) + 10 ** (Rmid[i] / 10)),10) + deltaR) for i in range(len(R1))]
Rtot_with_gasket = [float(Rtot[i] + 2) for i in range(len(Rtot))]

# 显示结果
Rair = [round(Rair[i],1) for i in range(len(Rair))]
Rtot = [round(Rtot[i],1) for i in range(len(Rtot))]
Rtot_with_gasket = [round(Rtot_with_gasket[i],1) for i in range(len(Rtot_with_gasket))]
p1 = 'Sound insulation when the interlayer is air: Rair = '+str(Rair)
p2 = 'Sound insulation when the interlayer is sound insulation material: Rtot = '+str(Rtot)
p3 = 'Sound insulation when the interlayer is sound insulation material and the keel gasket is added: Rtot_with_gasket = '+str(Rtot_with_gasket)
print(p1)
print(p2)
print(p3)