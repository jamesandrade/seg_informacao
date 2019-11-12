import pyping
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import datetime

i = 1
y = []
tempos = []
while i < 30:
	r = pyping.ping('baidu.com')
	y.append(r.avg_rtt)
	tempos.append((datetime.datetime.now()).strftime('%M:%S'))
	print(i)
	i+= 1   

y = np.asarray(y)
y = y.astype('float64')
y = np.nan_to_num(y)
tempos = np.asarray(tempos)

style.use('ggplot')
plt.xlabel('tempo')
plt.ylabel('media')
plt.plot(tempos, y, c = 'blue', label = 'pacotes', alpha = 0.5)
plt.scatter(tempos[y == 0.], y[y == 0.], label = 'falha', c = 'red')
plt.scatter(tempos[y > 0.], y[y > 0.], label = 'concluido', c = 'green')
plt.ylim(bottom = -1, top = max(1000, (y.max() + 40)))
plt.gcf().autofmt_xdate()
plt.legend()
plt.show()
