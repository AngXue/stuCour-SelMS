import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QMenu, QAction
from PyQt5 import QtCore


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['课程名', '教师', '时间'])

        data = [['高等数学', '李老师', '星期一'],
                ['线性代数', '王老师', '星期二'],
                ['大学英语', '赵老师', '星期三'],
                ['体育', '张老师', '星期四'],
                ['计算机科学', '孙老师', '星期五']]

        for i in range(5):
            for j in range(3):
                self.table.setItem(i, j, QTableWidgetItem(data[i][j]))

        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.on_context_menu)

        self.popMenu = QMenu(self)
        self.unsub = QAction('退选课程', self)
        self.unsub.triggered.connect(self.unsubscribe)
        self.popMenu.addAction(self.unsub)

    def on_context_menu(self, point):
        self.popMenu.exec_(self.table.mapToGlobal(point))

    def unsubscribe(self):
        items = self.table.selectedItems()
        row = self.table.row(items[0])
        self.table.removeRow(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
