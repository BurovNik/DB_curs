import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QDialogButtonBox, QMessageBox
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# диалоговое окно для получения информации о департаменте
class DepartmentInputDialog(QDialog):
    def __init__(self, parent=None):
        super(DepartmentInputDialog, self).__init__(parent)

        self.setWindowTitle("Введите номер отдела")

        self.department_label = QLabel("Номер отдела:")
        self.department_edit = QLineEdit()
        self.department_buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.department_buttonBox.accepted.connect(self.accept)
        self.department_buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.department_label)
        layout.addWidget(self.department_edit)
        layout.addWidget(self.department_buttonBox)
        self.setLayout(layout)

    def get_department_number(self):
        return self.department_edit.text()

# диалоговое окно для вывод информации о клиенте
class ClientListDialog(QDialog):
    def __init__(self, results, parent=None):
        super(ClientListDialog, self).__init__(parent)

        self.setWindowTitle("Список клиентов")
        self.setGeometry(100, 100, 500, 200)

        layout = QVBoxLayout()
        table_widget = QTableWidget()
        table_widget.setColumnCount(4)
        table_widget.setHorizontalHeaderLabels(["ID", "Name", "Surname", "Patronymic"])
        table_widget.setRowCount(len(results))

        for row, result in enumerate(results):
            for col in range(4):
                item = QTableWidgetItem(str(result[col]))
                table_widget.setItem(row, col, item)

        layout.addWidget(table_widget)
        self.setLayout(layout)

# диалоговое окно для получения названия города
class CityInputDialog(QDialog):
    def __init__(self, parent=None):
        super(CityInputDialog, self).__init__(parent)

        self.setWindowTitle("Город отправления")

        self.city_label = QLabel("Введите город:")
        self.city_edit = QLineEdit()
        self.city_buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.city_buttonBox.accepted.connect(self.accept)
        self.city_buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_edit)
        layout.addWidget(self.city_buttonBox)
        self.setLayout(layout)

    def get_cty_name(self):
        return self.city_edit.text()

#диалоговое окно для получения информации о Городе и должности
class CargoByCityAndJobTitleDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Введите город и должность")
        self.city_edit = QLineEdit()
        self.job_title_edit = QLineEdit()
        self.ok_button = QPushButton("OK")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Город:"))
        layout.addWidget(self.city_edit)
        layout.addWidget(QLabel("Должность:"))
        layout.addWidget(self.job_title_edit)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept)

    def get_city(self):
        return self.city_edit.text()

    def get_job_title(self):
        return self.job_title_edit.text()

# диалоговое окно где выводится информация о посылках в город оформленных сотрудником с должностью
class CargoListDialog(QDialog):
    def __init__(self, results, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Список посылок")

        layout = QVBoxLayout()
        table_widget = QTableWidget()
        table_widget.setColumnCount(11)
        table_widget.setHorizontalHeaderLabels(['ID', 'Тип', 'Номер отделения', 'Отправитель', 'Получатель', 'Куда', 'Откуда', 'Дата получения', 'Дата отправки', 'Сотрудник', 'Цена'])
        table_widget.setRowCount(len(results))

        for row, result in enumerate(results):
            for col in range(11):
                item = QTableWidgetItem(str(result[col]))
                table_widget.setItem(row, col, item)

        layout.addWidget(table_widget)
        self.setLayout(layout)

class BestSenders(QDialog):
    def __init__(self, results, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Статистика по посылкам")

        layout = QVBoxLayout()
        table_widget = QTableWidget()
        table_widget.setColumnCount(2)
        table_widget.setHorizontalHeaderLabels(['Сотрудник', 'Количество посылок'])
        table_widget.setRowCount(len(results))

        for row, result in enumerate(results):
            for col in range(2):
                item = QTableWidgetItem(str(result[col]))
                table_widget.setItem(row, col, item)

        layout.addWidget(table_widget)
        self.setLayout(layout)

class FisrtCargo(QDialog):
    def __init__(self, results, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Первая посылка")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        table_widget = QTableWidget()
        table_widget.setColumnCount(3)
        table_widget.setHorizontalHeaderLabels(['Дата', 'Откуда', 'Куда'])
        table_widget.setRowCount(len(results))

        for row, result in enumerate(results):
            for col in range(3):
                item = QTableWidgetItem(str(result[col]))
                table_widget.setItem(row, col, item)

        layout.addWidget(table_widget)
        self.setLayout(layout)

class ClientInputDialog(QDialog):
    def __init__(self, parent=None):
        super(ClientInputDialog, self).__init__(parent)

        self.setWindowTitle("Введите имя клиента")

        self.client_label = QLabel("ФИО клиента:")
        self.client_edit = QLineEdit()
        self.client_buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.client_buttonBox.accepted.connect(self.accept)
        self.client_buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.client_label)
        layout.addWidget(self.client_edit)
        layout.addWidget(self.client_buttonBox)
        self.setLayout(layout)

    def get_client_fio(self):
        return self.client_edit.text()

class WorkingDay(QDialog):
    def __init__(self, results, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Рабочие дни")

        layout = QVBoxLayout()
        table_widget = QTableWidget()
        table_widget.setColumnCount(2)
        table_widget.setHorizontalHeaderLabels(['Дата отправки', 'Дата получения'])
        table_widget.setRowCount(len(results))

        for row, result in enumerate(results):
            for col in range(2):
                item = QTableWidgetItem(str(result[col]))
                table_widget.setItem(row, col, item)

        layout.addWidget(table_widget)
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='KfMtged7',
            database='post_service_db'
        )

        self.setWindowTitle("Программа для Почты")
        self.setGeometry(100, 100, 800, 600)
        self.cursor = self.connection.cursor()
        sql = "SELECT * FROM employers;"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.cursor.close()
        self.employers_df = pd.DataFrame(results)
        layout = QHBoxLayout()

        # Левая часть - Таблица сотрудников
        table_widget = QTableWidget()
        table_widget.setColumnCount(len(self.employers_df.columns))
        table_widget.setHorizontalHeaderLabels(["ID", "Имя", "Фамилия", "Отчество", "Паспорт", "Должность", "Отделение"])
        table_widget.setRowCount(len(self.employers_df))
        for row in range(len(self.employers_df)):
            for col in range(len(self.employers_df.columns)):

                item = QTableWidgetItem(str(self.employers_df[col][row]))
                table_widget.setItem(row, col, item)

        layout.addWidget(table_widget)

        # Правая часть - поля для заполнения и кнопки
        right_panel_layout = QVBoxLayout()

        label1 = QLabel("Имя:")
        edit1 = QLineEdit()
        right_panel_layout.addWidget(label1)
        right_panel_layout.addWidget(edit1)

        label2 = QLabel("Фамилия:")
        edit2 = QLineEdit()
        right_panel_layout.addWidget(label2)
        right_panel_layout.addWidget(edit2)

        label3 = QLabel("Отчество:")
        edit3 = QLineEdit()
        right_panel_layout.addWidget(label3)
        right_panel_layout.addWidget(edit3)

        label4 = QLabel("Паспорт:")
        edit4 = QLineEdit()
        right_panel_layout.addWidget(label4)
        right_panel_layout.addWidget(edit4)

        label5 = QLabel("Должность:")
        edit5 = QLineEdit()
        right_panel_layout.addWidget(label5)
        right_panel_layout.addWidget(edit5)

        label6 = QLabel("Отделение:")
        edit6 = QLineEdit()
        right_panel_layout.addWidget(label6)
        right_panel_layout.addWidget(edit6)

        cargo_by_type_button = QPushButton("Показать распределение по типам посылки")
        cargo_by_type_button.clicked.connect(self.show_department_dialog)
        right_panel_layout.addWidget(cargo_by_type_button)

        cargo_sender_from_NWFA_button = QPushButton("Посылки c отправителями из СЗФО")
        cargo_sender_from_NWFA_button.clicked.connect(self.show_city_dialog)
        right_panel_layout.addWidget(cargo_sender_from_NWFA_button)

        acg_cargo_by_region_button = QPushButton("Среднее количество посылок в день по регионам")
        acg_cargo_by_region_button.clicked.connect(self.show_avg_cargo)
        right_panel_layout.addWidget(acg_cargo_by_region_button)

        cargo_in_city_from_job_title_button = QPushButton("Посыки в город от должности")
        cargo_in_city_from_job_title_button.clicked.connect(self.city_job_dialog)
        right_panel_layout.addWidget(cargo_in_city_from_job_title_button)

        first_client_cargo_button = QPushButton("Дата первого отправления клиента")
        first_client_cargo_button.clicked.connect(self.first_client_cargo_dialog)
        right_panel_layout.addWidget(first_client_cargo_button)

        first_cargo_button = QPushButton("Первая посылка")
        first_cargo_button.clicked.connect(self.first_cargo_info_dialog)
        right_panel_layout.addWidget(first_cargo_button)

        best_employer_by_cargo_type_button = QPushButton("Лучший сотрудник по каждой категории")
        best_employer_by_cargo_type_button.clicked.connect(self.best_employer_dialog)
        right_panel_layout.addWidget(best_employer_by_cargo_type_button)

        employers_cargo_type = QPushButton("Распределение посылок по сотрудникам в зависимости от типа")
        employers_cargo_type.clicked.connect(self.show_employers_cargo_type)
        right_panel_layout.addWidget(employers_cargo_type)

        cargo_to_Moskow_button = QPushButton("Посылки в Москву")
        cargo_to_Moskow_button.clicked.connect(self.cargo_to_Moskow)
        right_panel_layout.addWidget(cargo_to_Moskow_button)

        get_employer_workdays_button = QPushButton("Показать рабочие дни сотрудника")
        get_employer_workdays_button.clicked.connect(self.get_employer_work_day)
        right_panel_layout.addWidget(get_employer_workdays_button)

        layout.addLayout(right_panel_layout)

        self.setLayout(layout)

    def fill_main_table(self, table_widget):
        self.cursor = self.connection.cursor()
        sql = "SELECT * FROM employers;"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.cursor.close()
        self.employers_df = pd.DataFrame(results)

        table_widget.setColumnCount(len(self.employers_df.columns))
        table_widget.setHorizontalHeaderLabels(
            ["ID", "Имя", "Фамилия", "Отчество", "Паспорт", "Должность", "Отделение"])
        table_widget.setRowCount(len(self.employers_df))
        for row in range(len(self.employers_df)):
            for col in range(len(self.employers_df.columns)):
                item = QTableWidgetItem(str(self.employers_df[col][row]))
                table_widget.setItem(row, col, item)


    def show_department_dialog(self):
        department_dialog = DepartmentInputDialog(self)
        if department_dialog.exec_():
            department_number = int(department_dialog.get_department_number())

            self.cursor = self.connection.cursor()
            self.cursor.callproc('GetCargoByDepartment', [department_number])
            results = self.cursor.fetchall()
            print(f"Выбран город: {results}")
            self.cursor.close()

            cargo_types = [result[0] for result in results]
            quantities = [result[1] for result in results]

            self.plot_pie_chart(cargo_types, quantities)

    def plot_pie_chart(self, labels, sizes):
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.show()

    def show_city_dialog(self):
        city_dialog = CityInputDialog(self)
        if city_dialog.exec_():
            city = str(city_dialog.get_cty_name())
            cursor = self.connection.cursor()
            cursor.callproc('GetClientsByCityandRegion', [city])
            results = cursor.fetchall()
            cursor.close()
            if len(results[0]) == 4:
                self.show_client_list_dialog(results)
            else:
                QMessageBox.warning(self, "Ошибка", results[0][0])

    def show_client_list_dialog(self, results):
        client_list_dialog = ClientListDialog(results, self)
        client_list_dialog.exec_()

    def city_job_dialog(self):
        city_job_dialog = CargoByCityAndJobTitleDialog(self)
        if city_job_dialog.exec_():
            city = city_job_dialog.get_city()
            job_title = city_job_dialog.get_job_title()
            self.get_cargo_data_by_city_and_job_title(city, job_title)

    def get_cargo_data_by_city_and_job_title(self, city, job_title):
        cursor = self.connection.cursor()
        cursor.callproc('GetCargoByCityAndJobTitle', [city, job_title])
        results = cursor.fetchall()
        cursor.close()

        if len(results) > 0:
            if len(results[0]) == 1:  # Проверяем, является ли результат ошибкой
                QMessageBox.warning(self, "Ошибка", results[0][0])
            else:
                self.show_cargo_list_dialog(results)
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось получить данные.")

    def show_cargo_list_dialog(self, results):
        cargo_list_dialog = CargoListDialog(results, self)
        cargo_list_dialog.exec_()

    def show_avg_cargo(self):
        cursor = self.connection.cursor()
        cursor.callproc('CalculateAvgNumOfCargoPerDay')
        results = cursor.fetchall()
        cursor.close()
        areas = [result[0] for result in results]
        avg_cargo = [result[1] for result in results]
        plt.bar(areas, avg_cargo)
        plt.xlabel('Регион')
        plt.ylabel('Среднее количество посылок в день')
        plt.title('Среднее количество посылок в день по регионам')
        plt.xticks(rotation=20)

        plt.show()

    def best_employer_dialog(self):
        cursor = self.connection.cursor()
        cursor.callproc('FindBestSenderForEachType')
        results = cursor.fetchall()
        cursor.close()
        best_senders_dialog = BestSenders(results, self)
        best_senders_dialog.exec_()

    def first_cargo_info_dialog(self):
        cursor = self.connection.cursor()
        cursor.callproc('GetFirstCargoDepartureInfo')
        results = cursor.fetchall()
        cursor.close()
        first_cargo_dialog = FisrtCargo(results, self)
        first_cargo_dialog.exec_()

    def show_employers_cargo_type(self):
        cursor = self.connection.cursor()
        cursor.callproc('GetCargoData')
        results = cursor.fetchall()
        cursor.close()
        df = pd.DataFrame(results)

        # Построение графика
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df, x=df[0], y=df[2], hue=df[1], dodge=True)
        plt.xlabel('ФИО')
        plt.ylabel('Количество посылок')
        plt.legend(title='Тип посылки', loc='upper right')
        plt.show()
        #plt.scatter(results[0], results[2], hue= results[1])
        #plt.show()

    def first_client_cargo_dialog(self):
        first_client_dialog = ClientInputDialog(self)
        if first_client_dialog.exec_():
            client_fio = first_client_dialog.get_client_fio()

            self.cursor = self.connection.cursor()
            client = client_fio.split()
            self.cursor.callproc('GetFirstCargoDepartureDateByClientName', [client[0], client[1], client[2]])
            results = self.cursor.fetchall()
            #print(results)
            self.cursor.close()
            QMessageBox.information(self, "Дата Первой отправки", f"{results[0][0]}")

    def cargo_to_Moskow(self):
        department_dialog = DepartmentInputDialog(self)
        if department_dialog.exec_():
            department_number = int(department_dialog.get_department_number())

            self.cursor = self.connection.cursor()
            self.cursor.callproc('CheckCargoCountForMoscow', [department_number])
            results = self.cursor.fetchall()
            self.cursor.close()
            QMessageBox.information(self, "Количество посылок", f"{results[0][0]}")

    def get_employer_work_day(self):
        client_dialog = ClientInputDialog(self)
        if client_dialog.exec_():
            client_fio = client_dialog.get_client_fio()

            self.cursor = self.connection.cursor()
            client = client_fio.split()
            self.cursor.callproc('sp_CheckEmployeeAndGetDates', [client[0], client[1], client[2]])
            results = self.cursor.fetchall()
            # print(results)
            self.cursor.close()
            if len(results[0]) == 2:
                working_day_dialog = WorkingDay(results, self)
                working_day_dialog.exec_()
            else:
                QMessageBox.warning(self, "Ошибка", results[0][0])


    def CloseEvent(self, event):
        self.connection.close()
        event.accept()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
