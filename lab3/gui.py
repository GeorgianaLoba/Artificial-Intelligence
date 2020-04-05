# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:24:55 2020

@author: GeoLoba
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QTableView,QLabel, QTableWidget,QTableWidgetItem
from Controller import EA, HC, PSO
import matplotlib.pyplot as plt
import matplotlib
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 40, 634, 467))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.horizontalLayout_12.addWidget(self.tableWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_EA = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_EA.setObjectName("pushButton_EA")
        self.horizontalLayout_6.addWidget(self.pushButton_EA)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_EA_population_size = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_EA_population_size.setObjectName("lineEdit_EA_population_size")
        self.horizontalLayout_5.addWidget(self.lineEdit_EA_population_size)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_EA_mutation = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_EA_mutation.setObjectName("lineEdit_EA_mutation")
        self.horizontalLayout_4.addWidget(self.lineEdit_EA_mutation)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.pushButton_HC = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_HC.setObjectName("pushButton_HC")
        self.verticalLayout_3.addWidget(self.pushButton_HC)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_PSO = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_PSO.setObjectName("pushButton_PSO")
        self.horizontalLayout_11.addWidget(self.pushButton_PSO)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.lineEdit_PSO_population_size = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_PSO_population_size.setObjectName("lineEdit_PSO_population_size")
        self.horizontalLayout_10.addWidget(self.lineEdit_PSO_population_size)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_PSO_size_neigh = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_PSO_size_neigh.setObjectName("lineEdit_PSO_size_neigh")
        self.horizontalLayout_3.addWidget(self.lineEdit_PSO_size_neigh)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.lineEdit_PSO_w = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_PSO_w.setObjectName("lineEdit_PSO_w")
        self.horizontalLayout_7.addWidget(self.lineEdit_PSO_w)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.lineEdit_PSO_c1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_PSO_c1.setObjectName("lineEdit_PSO_c1")
        self.horizontalLayout_8.addWidget(self.lineEdit_PSO_c1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.lineEdit_PSO_c2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_PSO_c2.setObjectName("lineEdit_PSO_c2")
        self.horizontalLayout_9.addWidget(self.lineEdit_PSO_c2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12.addLayout(self.verticalLayout_3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_number_iterations = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_number_iterations.setObjectName("lineEdit_number_iterations")
        self.horizontalLayout.addWidget(self.lineEdit_number_iterations)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_n = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.horizontalLayout_2.addWidget(self.lineEdit_n)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_14.addWidget(self.label_12)
        self.label_deviation = QtWidgets.QLabel(self.layoutWidget)
        self.label_deviation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_deviation.setObjectName("label_deviation")
        self.horizontalLayout_14.addWidget(self.label_deviation)
        self.verticalLayout_8.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_15.addWidget(self.label_13)
        self.label_average = QtWidgets.QLabel(self.layoutWidget)
        self.label_average.setAlignment(QtCore.Qt.AlignCenter)
        self.label_average.setObjectName("label_average")
        self.horizontalLayout_15.addWidget(self.label_average)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_16.addLayout(self.verticalLayout_9)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.tableWidget_best = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget_best.setObjectName("tableWidget_best")
        self.tableWidget_best.setColumnCount(0)
        self.tableWidget_best.setRowCount(0)
        self.verticalLayout_7.addWidget(self.tableWidget_best)
        self.horizontalLayout_13.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_stop = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout_6.addWidget(self.pushButton_stop)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.label_fitness = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_fitness.setFont(font)
        self.label_fitness.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fitness.setObjectName("label_fitness")
        self.verticalLayout_5.addWidget(self.label_fitness)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_13.addLayout(self.verticalLayout_6)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_13)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)    
        
        self.__connect_buttons()

        fig = plt.figure()
        self.ax = fig.add_subplot(211)
        


        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_EA.setText(_translate("MainWindow", "Start EA"))
        self.label_5.setText(_translate("MainWindow", "Population Size:"))
        self.label_4.setText(_translate("MainWindow", "Mutation:"))
        self.pushButton_HC.setText(_translate("MainWindow", "Start HC"))
        self.pushButton_PSO.setText(_translate("MainWindow", "Start PSO"))
        self.label_9.setText(_translate("MainWindow", "Population Size:"))
        self.label_3.setText(_translate("MainWindow", "Size of neighbourhoods:"))
        self.label_6.setText(_translate("MainWindow", "W:"))
        self.label_7.setText(_translate("MainWindow", "C1:"))
        self.label_8.setText(_translate("MainWindow", "C2:"))
        self.label.setText(_translate("MainWindow", "Number of Iterations: "))
        self.label_2.setText(_translate("MainWindow", "Size of Individual/Particle:"))
        self.label_12.setText(_translate("MainWindow", "Standard Deviation"))
        self.label_deviation.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "Average"))
        self.label_average.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "Current Best"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.label_11.setText(_translate("MainWindow", "Best fitness:"))
        self.label_fitness.setText(_translate("MainWindow", "0"))

    def __connect_buttons(self):
        self.pushButton_EA.clicked.connect(self.__start_EA)
        self.pushButton_HC.clicked.connect(self.__start_HC)
        self.pushButton_PSO.clicked.connect(self.__start_PSO)
        self.pushButton_stop.clicked.connect(self.__stop_fction)

    def __stop_fction(self):
        pass
        #TODO

    def __update(self, n, individ):
        ind_vals = individ.get_individual()
        self.tableWidget_best.setRowCount(n)
        self.tableWidget_best.setColumnCount(n)
        for i in range(n):
            for j in range(n):
                self.tableWidget_best.setItem(i, j, QTableWidgetItem(str((ind_vals[i][j], ind_vals[i+n][j]))));
        self.label_fitness.setText(str(individ.fitness()))
        
        
    def __start_EA(self):
        number_generations = int(self.lineEdit_number_iterations.text())
        n = int(self.lineEdit_n.text())
        mutation= float(self.lineEdit_EA_mutation.text())
        population_size = int(self.lineEdit_EA_population_size.text())
        controller = EA(number_generations, mutation, population_size, n)
        fitnesses=[]
        trials=[]
        trial = 0
        for i in range(number_generations):
            deviation, average=controller.new_generation()
            self.label_deviation.setText(str(deviation))
            self.label_average.setText(str(average))
            if controller.is_solution()== True:
                break
            if trial<30:
                fitnesses.append(controller.get_repository().get_population()[0].fitness())
                trials.append(trial)
                trial+=1
        self.__update(n, controller.get_repository().get_population()[0])
        self.ax.plot(fitnesses, trials, "-b", "EA")

    def __start_HC(self):
        number_generations = int(self.lineEdit_number_iterations.text())
        n = int(self.lineEdit_n.text())
        controller = HC(n)
        fitnesses=[]
        trials=[]
        trial = 0
        for i in range(number_generations):
            out, deviation, average=controller.new_generation()
            self.label_deviation.setText(str(deviation))
            self.label_average.setText(str(average))
            if controller.is_solution()== True:
  
                break;
            if trial<30:
                fitnesses.append(controller.get_individual().fitness())
                trials.append(trial)
                trial+=1
        self.__update(n, controller.get_individual())
        self.ax.plot(fitnesses, trials, "-r", "HC")
        #TODO no success
        
    def __start_PSO(self):
        number_generations = int(self.lineEdit_number_iterations.text())
        n = int(self.lineEdit_n.text())
        population_size=int(self.lineEdit_PSO_population_size.text())
        w = float(self.lineEdit_PSO_w.text())
        c1=float(self.lineEdit_PSO_c1.text())
        c2=float(self.lineEdit_PSO_c2.text())
        neigh_size = int(self.lineEdit_PSO_size_neigh.text())

        controller=PSO(population_size,neigh_size, n, w, c1,c2)
        for i in range(number_generations):
            deviation, average=controller.iteration()
            self.label_deviation.setText(str(deviation))
            self.label_average.setText(str(average))
        best = 0 
        population = controller.get_repository().get_population()
        for i in range(population_size):
            if (population[i].fitness()<population[best].fitness()):
                best= i 
        self.__update(n, population[best])
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
