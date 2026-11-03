import matplotlib.pyplot as plt
import numpy as np

#霍尔电流Is (mA)
Is = np.array([0.00, 0.50, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00])
# |UH|霍尔电压绝对值(mV)
Uh_abs = np.array([0.00,0.29,0.60,0.91,1.23,1.55,1.86,2.16,2.48])

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(8,5),dpi=120)
plt.scatter(Is, Uh_abs, color="#1f77b4", label="实验测量点", zorder=5)
k,b = np.polyfit(Is, Uh_abs,1)
fit = np.poly1d([k,b])
x_line = np.linspace(0,4.1,100)
plt.plot(x_line, fit(x_line), "r--", label=f"拟合直线 $U_H={k:.2f}\cdot I_S$")

plt.xlabel("霍尔电流 $I_S$ (mA)")
plt.ylabel("霍尔电压 $|U_H|$ (mV)")
plt.title("霍尔效应 $U_H-I_S$ 曲线")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
print(f"拟合斜率k={k:.3f} mV/mA")
