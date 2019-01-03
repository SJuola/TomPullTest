import sys
import numpy as np
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from PyQt5.QtCore import QTime, QTimer
from PyQt5 import QtGui
from collections import deque

class MyApplication(QtGui.QApplication):
    def __init__(self, *args, **kwargs):
            super(MyApplication, self).__init__(*args, **kwargs)
            self.t = QTime()
            self.t.start()
            self.data = deque()

            self.win = pg.GraphicsWindow(title="Basic plotting examples")
            self.win.resize(600, 400)

            '''self.plot = self.win.addPlot(title='Timed data', axisItems={
                                         'bottom': TimeAxisItem(orientation='bottom')})'''
            self.plot = self.win.addPlot(title='Timed data')
            self.plot.setLabel('bottom', 'Time [ms]')
            self.plot.setLabel('left', 'Pulling Speed [in/s]')
            self.plot.setXRange(min=0, max=5000, padding=0.1)
            self.curve = self.plot.plot()

            self.tmr = QTimer()
            self.tmr.timeout.connect(self.update)
            self.tmr.start(20)

    def update(self):
            self.data.append(
                {'x': self.t.elapsed(), 'y': np.random.uniform(-1, 1)})
            x = [item['x'] for item in self.data]
            y = [item['y'] for item in self.data]
            self.curve.setData(x=x, y=y, pen= pg.mkPen('w', width=1, style=QtCore.Qt.DotLine))

            temp = self.t.elapsed()
            print(temp)
            if temp >=5000:
                self.tmr.stop()
                #Write data to file
                with open('log_test.csv','w') as file:
                    file.writelines('time [miliseconds], velocity [in/s] \n')
                    for item in self.data:
                        file.write(str(item['x']/1000.0) + ',' + str(item['y']) + '\n')
            self.processEvents()
def main():
        app = MyApplication(sys.argv)
        sys.exit(app.exec_())

if __name__ == '__main__':
        main()