from random import choice
import matplotlib.pyplot as plt


class RandomWalk:
	"""
	生成随机漫步数据的类
	"""

	def __init__(self, numpoints=5000):
		"""初始化随机漫步属性"""
		self.numpoints = numpoints
		# 随机漫步都始于(0, 0)
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		"""计算随机漫步包含的所有的点"""
		while len(self.x_values) < self.numpoints:
			# 决定前进方向以及沿这个方向前进的距离
			x_direction = choice([1, -1])
			x_distance = choice([0, 1, 2, 3, 4])
			x_step = x_distance * x_direction
			y_direction = choice([1, -1])
			y_distance = choice([0, 1, 2, 3, 4])
			y_step = y_distance * y_direction
			# 拒绝原地踏步
			if x_step == 0 and y_step == 0:
				continue
			# 计算下一个点的x值和y值
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step
			self.x_values.append(x)
			self.y_values.append(y)


# 创建一个RandomWalk实例
rw = RandomWalk()
rw.fill_walk()
# 绘制随机漫步图
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
