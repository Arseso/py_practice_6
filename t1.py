from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import sys
#
# Window for dynamic plotting train & val losses
#

class PlotWindow(QMainWindow):
    def __init__(self, dotes_s, dotes_c):
        super().__init__()

        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.plot(dotes_s, dotes_c)

    def plot(self, sinus: list, cosinus: list):
        self.figure.clear()

        # Строим график
        ax = self.figure.add_subplot()
        ax.plot(sinus, color='blue', label='Sinus')
        ax.plot(cosinus, color='red', label='Cosinus')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Functions')
        ax.legend()

        self.canvas.draw()


def sin_dotes_generator(num_dotes):
    dotes = []
    for i in range(num_dotes):

        dotes.append(np.sin((i)/num_dotes*np.pi))
    return dotes

def cosin_dotes_generator(num_dotes):
    dotes = []
    for i in range(num_dotes):
        dotes.append(np.cos((i)/num_dotes*np.pi))
    return dotes

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = PlotWindow(dotes_s= sin_dotes_generator(100),
                             dotes_c=cosin_dotes_generator(100))
    main_window.show()
    sys.exit(app.exec())
