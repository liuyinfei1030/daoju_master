import os
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# 创建GUI界面
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Excel Analyzer')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # 添加路径选择按钮
        self.btn_choose = QPushButton('选择文件')
        self.layout.addWidget(self.btn_choose)
        self.btn_choose.clicked.connect(self.choose_file)

        # 添加波形显示界面
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.layout.addWidget(self.canvas)

        # 添加特征提取按钮
        self.btn_mean = QPushButton('提取均值')
        self.btn_std = QPushButton('提取标准差')
        self.layout.addWidget(self.btn_mean)
        self.layout.addWidget(self.btn_std)
        self.btn_mean.clicked.connect(self.extract_mean)
        self.btn_std.clicked.connect(self.extract_std)

    # 打开文件选择对话框
    def choose_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择文件', '.', 'Excel files (*.xlsx)')
        if filename:
            self.filename = filename
            self.label_path = QLabel(filename)
            self.layout.addWidget(self.label_path)
            self.df = pd.read_excel(self.filename, index_col=0, header=[0, 1])
            self.ax.clear()
            self.ax.plot(self.df)
            self.canvas.draw()

    # 提取均值
    def extract_mean(self):
        if hasattr(self, 'df'):
            means = self.df.mean()
            self.ax.clear()
            self.ax.plot(means)
            self.canvas.draw()

    # 提取标准差
    def extract_std(self):
        if hasattr(self, 'df'):
            stds = self.df.std()
            self.ax.clear()
            self.ax.plot(stds)
            self.canvas.draw()

# 启动应用程序
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
