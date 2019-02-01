import numpy as np
import matplotlib.pyplot as plt

x_coords = np.linspace(-100, 100, 500)
y_coords = np.linspace(-100, 100, 500)
points = []
for y in y_coords:
    for x in x_coords:
        if ((x*0.03)**2+(y*0.03)**2-1)**3-(x*0.03)**2*(y*0.03)**3 <= 0:
            points.append({"x": x, "y": y})
heart_x = list(map(lambda point: point["x"], points))
heart_y = list(map(lambda point: point["y"], points))

plt.scatter(heart_x, heart_y, s=10, alpha=0.5, c=range(len(heart_x)), cmap="gist_rainbow")
plt.show()

#<cmap="autumn"> 橙色的爱心
#<cmap="cool"> 紫色的爱心
#<cmap="magma"> 晚霞般的爱心
#<cmap="rainbow"> 彩虹般的爱心
#<cmap="Reds"> 炽热的爱心
#<cmap="spring">青春的爱心
#<cmap="viridis"> 翡翠色的爱心
#<cmap="gist_rainbow"> 五彩缤纷的爱心