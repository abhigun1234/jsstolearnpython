import matplotlib.pyplot as plt
import numpy as np
my_list=[1,2,3,4,5,6]
x=np.array(my_list)
y=x**2
plt.plot(x,y)
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('graph')
# plt.show()
#oo methods
fig=plt.figure()
axes=fig.add_axes([1,2,3,4])
axes.plot()
