import matplotlib.pyplot as plt


#plt.figure() Figureインスタンスを作成する
#Figureインスタンスは、描画全体の領域を確保する
# 引数では以下を指定できる。
#figsize,dpi,facecolor,edgecolor
fig = plt.figure()
fig.add_subplot(1,1,1)


fig = plt.figure()
fig.add_subplot(1, 1, 1)
fig.add_subplot(3, 3, 1)   # 3x3の1つめ(左上)
fig.add_subplot(3, 3, 3)   # 3x3の3つめ(右上)
fig.add_subplot(3, 3, 8)   # 3x3の8つめ(真ん中下)


plt.subplot(3,3,1)
plt.subplot(3,3,3)
plt.subplot(3,3,5)
plt.subplot(3,3,9)


plt.plot([1,2,3])


plt.subplot(211) 


plt.plot(range(12))
plt.subplot(212)


fig = plt.figure()


fig, axes = plt.subplots(2,2)
axes[0][0].plot([1,2,3])
axes[1][0].plot([4,5,4,5])


''' 
Axesオブジェクトは、実際のデータの描画の役割を持っている。
Axesオブジェクトに対して描画するデータを与えたり、
set_xlabel、set_ylabel、set_titleで
ラベルやタイトルの設定をできる。'''

ax1 = plt.subplot(2,2,1)
ax4 = plt.subplot(2,2,4)

ax1.plot([1,2,3,4])
ax1.plot([2,3,2,3])

ax4.plot([x for x in range(0,100)])



