from numpy import arange, pi, sin, cos, tan, sqrt, arctan2
import matplotlib.pyplot as plt


def polar(point):
	[x, y] = point
	r = sqrt(x ** 2 + y ** 2)
	phi = arctan2(y, x)
	polar_point = [r, phi]
	return polar_point


def cartesian(point):
	[r, phi] = point
	x = r * cos(phi)
	y = r * sin(phi)
	cartesian_point = [x, y]
	return cartesian_point


def circle(center, radius, phi):
	[r0, phi0] = center
	r = r0 * cos(phi - phi0) + sqrt(radius ** 2 - (r0 * sin(phi - phi0)) ** 2)
	return r


def line_perp(point, phi):
	[r0, phi0] = point
	r = r0 * (cos(phi - phi0)) ** -1
	return r


def conic(e, l, phi):
	# e = eccentricity
	# l = semi-latus rectum
	r = l / (1 - e * cos(phi))
	return r


def archimedian_spiral(a, b, phi):
	r = a + b * phi
	return r


def log_spiral(a, b, phi):
	r = a * (b ** phi)
	return r


# Polar equation
a = 1
b = 6
radius = 0.5
center = [1, pi / 2]
def func(phi):
	r = circle(center, radius, phi)
	return r

# phi_initial = 0
# phi_final = 2*pi
# delta_phi = 0.01
# phis = arange(phi_initial, phi_final, delta_phi)

# for phi in phis:
# 	r = func(phi)
# 	point = [r, phi]
# 	x, y = cartesian(point)
# 	plt.plot(x, y, 'g.')
# plt.grid()
# plt.show()
