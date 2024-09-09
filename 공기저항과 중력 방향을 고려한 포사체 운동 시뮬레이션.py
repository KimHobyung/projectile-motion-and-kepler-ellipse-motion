import matplotlib.pyplot as plt
import numpy as np

# 기본 설정
g = 9.8
vx0 = 2000  # 초기 속도 (x 방향)
vy0 = 2000  # 초기 속도 (y 방향)
gamma = 0.001  # 공기 저항 상수
x0 = 0.1  # 초기 위치 (x 방향)
y0 = 6400*1000 +1000  # 초기 위치 (y 방향)

# 공기 저항 고려, 중력 방향 고려X
t_vals = np.linspace(0, 500, 1000)
X = x0 + (vx0 / gamma) * (1 - np.exp(-gamma * t_vals))
Y = y0 + (vy0 / gamma + g / gamma**2) * (1 - np.exp(-gamma * t_vals)) - (g / gamma) * t_vals

# 단순 포물선 운동
X2 = x0 + vx0 * t_vals
Y2 = y0 + vy0 * t_vals - 0.5 * g * t_vals**2

# 공기 저항과 중력 방향 모두 고려
t = 0
dt = 0.5  # 시간 간격
position_x = [x0]
position_y = [y0]

while t < 500:
    t += dt 

    # 각도 psi 계산 
    psi = abs(np.arctan(position_y[-1]/position_x[-1]))

    # 새로운 위치 계산
    new_x = x0 + ((vx0 / gamma) + (g / gamma**2 * np.cos(psi))) * (1 - np.exp(-gamma * t)) - (g / gamma) * np.cos(psi) * t
    new_y = y0 + ((vy0 / gamma) + (g / gamma**2 * np.sin(psi))) * (1 - np.exp(-gamma * t)) - (g / gamma) * np.sin(psi) * t

    position_x.append(new_x)
    position_y.append(new_y)
print(psi)

plt.rcParams['font.family'] = 'Malgun Gothic'  # 맑은 고딕으로 설정
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 그래프 그리기
plt.plot(X, Y, label="공기저항 고려 (지표면의 곡률을 고려하지 않음)")
plt.plot(X2, Y2, label="공기저항 없는 포사체 운동")
plt.plot(position_x, position_y, label="공기저항과 중력의 방향을 고려", linestyle='--')
plt.legend()
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('vx0 = 2000m/s , vy0 = 2000m/s')
plt.grid(True)
plt.show()

