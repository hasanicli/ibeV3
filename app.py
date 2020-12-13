import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QAction, QFileDialog
from screens import *
import os
from openpyxl import Workbook, load_workbook, worksheet
from openpyxl.worksheet.datavalidation import DataValidation
from connectionDB import DbManager
from control_page import *
from helper_function import *

class App(MainWindow):
    def __init__(self):
        super().__init__()
        self.connection = DbManager()
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)



        # Triggered signals
        self.ui.act_branch.triggered.connect(lambda: self.open(BranchWindow))
        self.ui.act_cause.triggered.connect(lambda: self.open(CauseWindow))
        self.ui.act_class.triggered.connect(lambda: self.open(ClassWindow))
        self.ui.act_add_class_to_parent.triggered.connect(lambda: self.open(AddClassWindow))
        self.ui.act_degree.triggered.connect(lambda: self.open(DegreeWindow))
        self.ui.act_department.triggered.connect(lambda: self.open(DepartmentWindow))
        self.ui.act_disconnection.triggered.connect(lambda: self.open(DisconnectionWindow))
        self.ui.act_institutation_info.triggered.connect(lambda: self.open(InstitutionWindow))
        self.ui.act_neighborhood.triggered.connect(lambda: self.open(NeighborhoodWindow))
        self.ui.act_parent_class.triggered.connect(lambda: self.open(ParentClassWindow))
        self.ui.act_staff_branch.triggered.connect(lambda: self.open(StaffBranchWindow))
        self.ui.act_staff.triggered.connect(lambda: self.open(StaffWindow))
        self.ui.act_pull_sutudent.triggered.connect(lambda: self.open(StudentFromArchiveWindow))
        self.ui.act_student.triggered.connect(lambda: self.open(StudentWindow))
        self.ui.act_workplace.triggered.connect(lambda: self.open(WorkplaceWindow))
        self.ui.act_staff_workplace.triggered.connect(lambda: self.open(AddWorkplaceToStaff))

        self.ui.act_load_workplaces.triggered.connect(self.load_workplaces_file)
        self.ui.act_download_sample_workplaces.triggered.connect(self.save_excel_for_wp)

    def open(self, param_class):
        self.inst = param_class()
        self.inst.setWindowModality(Qt.ApplicationModal)
        self.inst.show()

    def read_wp_excel_file(self, path):
        loaded_wp_list = [i[0] for i in self.connection.selector(f"""SELECT name FROM workplaces""")]
        wp = load_workbook(path)
        active_page = wp['isletme']

        new_wp_list = []
        for row in range(2, 10000):
            if active_page.cell(row=row, column=1).value is None:
                break
            else:
                wp_name = tr_capitalize(stripper(str(active_page.cell(row, 1).value)))

                wp_boss = ""
                if active_page.cell(row, 2).value is not None:
                    wp_boss = tr_capitalize(stripper(str(active_page.cell(row, 2).value)))

                depart_name = active_page.cell(row, 3).value

                wp_mi = ""
                if active_page.cell(row, 4).value is not None:
                    wp_mi = tr_capitalize(stripper(str(active_page.cell(row, 4).value)))

                neigh_name = active_page.cell(row, 5).value

                add1 = ""
                if active_page.cell(row, 6).value is not None:
                    add1 = str(active_page.cell(row, 6).value)

                add2 = ""
                if active_page.cell(row, 7).value is not None:
                    add2 = str(active_page.cell(row, 7).value)

                tel1 = ""
                if active_page.cell(row, 8).value is not None:
                    tel1 = str(active_page.cell(row, 8).value)

                tel2 = ""
                if active_page.cell(row, 9).value is not None:
                    tel2 = str(active_page.cell(row, 9).value)

                email = ""
                if active_page.cell(row, 10).value is not None:
                    email = str(active_page.cell(row, 10).value)

                gov_ins = active_page.cell(row, 11).value

                control_list = [general_name_control(wp_name, loaded_wp_list), name_control(wp_boss), name_control(wp_mi), depart_name is not None, neigh_name is not None, gov_ins is not None]
                if False not in control_list:
                    new_wp_list.append((wp_name, wp_boss, depart_name, wp_mi, neigh_name, add1, add2, tel1, tel2, email, gov_ins))
                else:
                    print(str(row) + ". sattırda hata var")
                    new_wp_list = []
                    break
        print(new_wp_list)

    def load_workplaces_file(self):
        path, ok = QFileDialog.getOpenFileName(self, caption="Aç", directory=os.getcwd(), filter="Excel Files(*.xls, *.xlsx)")
        if ok:
            wp = load_workbook(path, read_only=True)
            if "isletme" in wp.sheetnames:
                self.read_wp_excel_file(path)
            else:
                QMessageBox.warning(None, "Uyarı", "dosya içinde gerekli sayfalar yok sayfayı yeniden indiriniz.")

    def save_excel_for_wp(self):
        if not os.path.isdir(os.path.join(os.getcwd(), "helper_files")):
            os.mkdir(os.path.join(os.getcwd(), "helper_files"))

        title_list = ["İşyeri Adı*", "İşyeri Sahibi*", "Alan Adı*", "Usta Öğretici*", "Mahalle Adı*", "adres satırı 1", "adres satırı 2", "telefon1", "telefon2", "email", "devlet desteği*"]
        neighborhoods_list = self.connection.selector(f"""SELECT * FROM neighborhoods""")
        departments_list = self.connection.selector(f"""SELECT * FROM departments""")
        wp_list = self.connection.selector(f"""SELECT * FROM workplaces""")

        excel_path = os.path.join(os.getcwd(), "helper_files/workplaces.xlsx")

        wb = Workbook()

        wb.create_sheet("isletme", 0)
        active_page = wb["isletme"]
        active_page.append(title_list)

        active_page.cell(row=1, column=13, value="id")
        active_page.cell(row=1, column=14, value="Alan Adı")
        for i in range(2, len(departments_list)+2):
            active_page.cell(row=i, column=13, value=departments_list[i-2][0])
            active_page.cell(row=i, column=14, value=departments_list[i-2][1])

        active_page.cell(row=1, column=15, value="id")
        active_page.cell(row=1, column=16, value="Mahalle Adı")
        for i in range(2, len(neighborhoods_list) + 2):
            active_page.cell(row=i, column=15, value=neighborhoods_list[i - 2][0])
            active_page.cell(row=i, column=16, value=neighborhoods_list[i - 2][1])

        active_page.cell(row=1, column=17, value="id")
        active_page.cell(row=1, column=18, value="Varolan İşletme Adı")
        for i in range(2, len(wp_list) + 2):
            active_page.cell(row=i, column=17, value=wp_list[i - 2][0])
            active_page.cell(row=i, column=18, value=wp_list[i - 2][1])

        del wb["Sheet"]

        dv_depart = DataValidation(type="list", formula1=f'=$N$2:$N${len(departments_list) + 1}', allow_blank=False)
        dv_neigh = DataValidation(type="list", formula1=f'=$P$2:$P${len(neighborhoods_list) + 1}', allow_blank=False)
        dv_yes_no = DataValidation(type="list", formula1='"E,H"', allow_blank=False)
        active_page.add_data_validation(dv_neigh)
        active_page.add_data_validation(dv_depart)
        active_page.add_data_validation(dv_yes_no)
        dv_depart.add("C2:C10000")
        dv_neigh.add("E2:E10000")
        dv_yes_no.add("K2:K10000")

        wb.save(excel_path)
        wb.close()

        wb = load_workbook(excel_path)
        path, ok = QFileDialog.getSaveFileName(self, caption="Kaydet", directory=excel_path, filter="Excel files (*.xls, *.xlsx)")
        if ok:
            wb.save(path)

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    sys.exit(app.exec())
