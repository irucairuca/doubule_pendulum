import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import japanize_matplotlib
import math

# アニメ
fig = plt.figure()

ims = []

# パラメータと定数
g=9.8


n=100

m_1=1.0
m_2=2.0

# 振り子の長さ
l_1=2
l_2=1

#時刻の初期値
t=0
#角度の初期値と角速度の初期値
theta_1 = math.pi/2
d_theta_dt_1=0
dd_theta_dd_t_1=0

theta_2 = 0
d_theta_dt_2=0
dd_theta_dd_t_2=0

#微小時間
dt =0.01

while(t<10):
 
  dd_theta_dd_t_1 = -((m_1+m_2)*g*l_1*np.sin(theta_1)+m_2*l_1*l_2*(dd_theta_dd_t_2*np.cos(theta_1-theta_2)+((d_theta_dt_2)**2)*np.sin(theta_1-theta_2)))/((m_1+m_2)*l_1**2)

  dd_theta_dd_t_2 = -(m_2*g*l_2*np.sin(theta_2)+m_2*l_1*l_2*(dd_theta_dd_t_1*np.cos(theta_1-theta_2)-((d_theta_dt_1)**2)*np.sin(theta_1-theta_2)))/(m_2*l_2**2)


  d_theta_dt_1 = d_theta_dt_1 + dd_theta_dd_t_1*dt
  theta_1 = theta_1 + d_theta_dt_1*dt

  d_theta_dt_2 = d_theta_dt_2 + dd_theta_dd_t_2*dt
  theta_2 = theta_2 + d_theta_dt_2*dt

  t = t+dt
  
  

  x_1=l_1*np.sin(theta_1)
  y_1=-l_1*np.cos(theta_1)
  
  x_2= l_1*np.sin(theta_1)+l_2*np.sin(theta_2)
  y_2= -l_1*np.cos(theta_1)-l_2*np.cos(theta_2)

  X_1= np.linspace(0,x_1,n)
  Y_1= np.linspace(0,y_1,n)

  X_2= np.linspace(x_1,x_2,n)
  Y_2= np.linspace(y_1,y_2,n)

  im1=plt.plot(X_1,Y_1,'-')
  im2=plt.plot(X_2,Y_2,'-')
  ims.append(im1+im2)


# 10枚のプロットを 100ms ごとに表示
ani = animation.ArtistAnimation(fig, ims, interval=100)
#保存
ani.save("furiko_2tai_simple.gif", writer="pillow")
plt.show()