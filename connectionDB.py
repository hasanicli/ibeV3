from PyQt5.QtWidgets import QMessageBox
import sqlite3
import os


class DbManager:
    def __init__(self):
        current_file_path = os.path.abspath(__file__)
        current_directory = os.path.abspath(os.path.join(current_file_path, os.pardir))
        db_path = os.path.join(current_directory, "ime.db")
        if os.path.isfile(db_path):
            self.db = sqlite3.connect(db_path)
            self.cur = self.db.cursor()
            self.cur.execute("PRAGMA foreign_keys = ON")
        else:
            self.create_database()

    def create_database(self):
        print("geldim")
        current_file_path = os.path.abspath(__file__)
        current_directory = os.path.abspath(os.path.join(current_file_path, os.pardir))
        db_path = os.path.join(current_directory, "ime.db")
        self.db = sqlite3.connect(db_path)
        self.cur = self.db.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "causes" ("id" INTEGER NOT NULL UNIQUE, "name" TEXT NOT NULL UNIQUE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "days" ("id"	INTEGER NOT NULL UNIQUE, "name"	TEXT NOT NULL UNIQUE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "departments" ("id" INTEGER NOT NULL UNIQUE, "name" TEXT NOT NULL UNIQUE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "neighborhoods" ("id" INTEGER NOT NULL UNIQUE, "name" TEXT NOT NULL UNIQUE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "parent_classes" ("id" INTEGER NOT NULL UNIQUE,"name" TEXT NOT NULL UNIQUE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "staff_branches" ("id" INTEGER NOT NULL UNIQUE,"name" TEXT NOT NULL UNIQUE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "staff_degrees" ("id" INTEGER NOT NULL UNIQUE,"name"	TEXT NOT NULL UNIQUE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "branches" ("id"	INTEGER NOT NULL UNIQUE,"name"	TEXT NOT NULL UNIQUE, "departmentID" INTEGER NOT NULL,
                        FOREIGN KEY("departmentID") REFERENCES "departments"("id") ON DELETE RESTRICT ON UPDATE CASCADE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "classes" ("id" INTEGER NOT NULL UNIQUE, "name" TEXT NOT NULL UNIQUE, "parentID"	INTEGER,
                        "departmentID" INTEGER NOT NULL, FOREIGN KEY("parentID") REFERENCES "parent_classes"("id") ON DELETE RESTRICT ON UPDATE CASCADE,
                        FOREIGN KEY("departmentID") REFERENCES "departments"("id") ON DELETE RESTRICT ON UPDATE CASCADE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "classes_days" ("classID" INTEGER NOT NULL, "dayID" INTEGER NOT NULL,
                        FOREIGN KEY("dayID") REFERENCES "days"("id") ON DELETE RESTRICT ON UPDATE CASCADE, FOREIGN KEY("classID") REFERENCES "classes"("id") ON DELETE CASCADE ON UPDATE CASCADE,
                        PRIMARY KEY("classID","dayID"))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "staffs" ("id_number" TEXT NOT NULL UNIQUE,"name" TEXT NOT NULL,"surname" TEXT NOT NULL,"staff_branchID"	INTEGER NOT NULL,
                        "staff_degreeID" INTEGER NOT NULL, "phone_number" TEXT, "email"	TEXT, FOREIGN KEY("staff_degreeID") REFERENCES "staff_degrees"("id") ON DELETE RESTRICT ON UPDATE CASCADE,
                        FOREIGN KEY("staff_branchID") REFERENCES "staff_branches"("id") ON DELETE RESTRICT ON UPDATE CASCADE, PRIMARY KEY("id_number"))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "school_info" ("id" INTEGER NOT NULL UNIQUE, "city" TEXT NOT NULL, "county" TEXT NOT NULL, "name" TEXT NOT NULL UNIQUE,
                        "managerID"	TEXT UNIQUE, "coordinator_managerID" TEXT UNIQUE, "phone_number1" TEXT, "phone_number2"	TEXT, "email" TEXT,
                        FOREIGN KEY("coordinator_managerID") REFERENCES "staffs"("id_number") ON DELETE SET NULL ON UPDATE CASCADE,
                        FOREIGN KEY("managerID") REFERENCES "staffs"("id_number") ON DELETE SET NULL ON UPDATE CASCADE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "staffs_days" ("dayID" INTEGER NOT NULL, "staffID" TEXT NOT NULL,
                        FOREIGN KEY("dayID") REFERENCES "days"("id") ON DELETE RESTRICT ON UPDATE CASCADE, FOREIGN KEY("staffID") REFERENCES "staffs"("id_number") ON DELETE CASCADE ON UPDATE CASCADE,
                        PRIMARY KEY("dayID","staffID"))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "students" ("id_number"	TEXT NOT NULL UNIQUE, "name" TEXT NOT NULL, "surname" TEXT NOT NULL, "school_number" TEXT NOT NULL,
                        "branchID" INTEGER NOT NULL, "classID" INTEGER, "record_date" TEXT NOT NULL, "father_name" TEXT, "mother_name" TEXT, "birthdate" TEXT, "birth_place" TEXT,
                        "is_going" TEXT NOT NULL, "self_phone" TEXT, "parent_phone1" TEXT, "parent_phone2" TEXT, "email" TEXT, "photo_address" TEXT, "is_active" TEXT NOT NULL,
                        "gender" TEXT NOT NULL, FOREIGN KEY("branchID") REFERENCES "branches"("id") ON DELETE RESTRICT ON UPDATE CASCADE,
                        FOREIGN KEY("classID") REFERENCES "classes"("id") ON DELETE RESTRICT ON UPDATE CASCADE, PRIMARY KEY("id_number"))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "archive" ("id" INTEGER NOT NULL UNIQUE, "studentID"	TEXT NOT NULL, "starting_date" TEXT NOT NULL, "disconnection_date" TEXT NOT NULL,
                        "disconnection_causeID"	INTEGER NOT NULL, "document_number"	TEXT NOT NULL, FOREIGN KEY("studentID") REFERENCES "students"("id_number") ON DELETE RESTRICT ON UPDATE CASCADE,
                        FOREIGN KEY("disconnection_causeID") REFERENCES "causes"("id") ON DELETE RESTRICT ON UPDATE CASCADE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "temp_workplace" ("id" INTEGER NOT NULL UNIQUE, "studentID" TEXT NOT NULL, "staffID"	TEXT,
                        "starting_date"	TEXT NOT NULL, FOREIGN KEY("studentID") REFERENCES "students"("id_number") ON DELETE CASCADE ON UPDATE CASCADE,
                        FOREIGN KEY("staffID") REFERENCES "staffs"("id_number") ON DELETE CASCADE ON UPDATE CASCADE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "history" ("id" INTEGER NOT NULL UNIQUE, "studentID"	TEXT NOT NULL, "workplaceID" INTEGER NOT NULL, "starting_date" TEXT NOT NULL,
                        "leaving_date" TEXT, FOREIGN KEY("studentID") REFERENCES "students"("id_number") ON DELETE RESTRICT ON UPDATE CASCADE,
                        FOREIGN KEY("workplaceID") REFERENCES "workplaces"("id") ON DELETE RESTRICT ON UPDATE CASCADE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS "workplaces" ("id" INTEGER NOT NULL UNIQUE, "name" TEXT NOT NULL UNIQUE, "boss" TEXT NOT NULL, "departmentID" INTEGER NOT NULL,
                        "master_instructive" TEXT NOT NULL, "neighborhoodID" INTEGER NOT NULL, "street"	TEXT, "address_number" TEXT, "phone_number1" TEXT, "phone_number2" TEXT, "email" TEXT,
                        "government_contribution" TEXT NOT NULL, "dayID" INTEGER, "staffID"	TEXT, FOREIGN KEY("neighborhoodID") REFERENCES "neighborhoods"("id") ON DELETE RESTRICT ON UPDATE CASCADE,
                        FOREIGN KEY("dayID") REFERENCES "days"("id") ON DELETE SET NULL ON UPDATE CASCADE, FOREIGN KEY("staffID") REFERENCES "staffs"("id_number") ON DELETE SET NULL ON UPDATE CASCADE,
                        FOREIGN KEY("departmentID") REFERENCES "departments"("id") ON DELETE RESTRICT ON UPDATE CASCADE, PRIMARY KEY("id" AUTOINCREMENT))""")
        self.cur.execute("""INSERT INTO "days" VALUES (1,'Pazartesi')""")
        self.cur.execute("""INSERT INTO "days" VALUES (2,'Salı')""")
        self.cur.execute("""INSERT INTO "days" VALUES (3,'Çarşamba')""")
        self.cur.execute("""INSERT INTO "days" VALUES (4,'Perşembe')""")
        self.cur.execute("""INSERT INTO "days" VALUES (5,'Cuma')""")
        self.cur.execute("""INSERT INTO "days" VALUES (6,'Cumartesi')""")
        self.cur.execute("""INSERT INTO "days" VALUES (7,'Pazar')""")
        self.db.commit()

    @staticmethod
    def message_box(p_text):
        QMessageBox.warning(None, "Uyarı", "Bir hataya raslanıldı.\nProgram kapanacak.\n" + p_text)

    def recorder(self, p_text):
        try:
            self.cur.execute(p_text)
            self.db.commit()
        except sqlite3.Error as err:
            if "constraint failed" in str(err):
                QMessageBox.warning(None, "UYARI !!!", "Bu kayıt daha önce girilmiş. Dal ismi tek olmalı")
            else:
                self.message_box(str(err))

    def poly_recorder(self, p_text, p_list):
        try:
            self.cur.executemany(p_text, p_list)
            self.db.commit()
        except sqlite3.Error as err:
            self.message_box(str(err))

    def updater(self, p_text):
        try:
            self.cur.execute(p_text)
            self.db.commit()
        except sqlite3.Error as err:
            self.message_box(str(err))

    def deleter(self, p_text):
        try:
            self.cur.execute(p_text)
            self.db.commit()
        except sqlite3.Error as err:
            if "constraint failed" in str(err):
                QMessageBox.warning(None, "UYARI !!!", "Bu kayıtla ilişkili kayıtlar var.\nKaydı silemezsiniz.\nSadece güncelleme yapabilirsiniz.")
            else:
                self.message_box(str(err))

    def selector(self, p_text):
        try:
            self.cur.execute(p_text)
            return self.cur.fetchall()
        except sqlite3.Error as err:
            self.message_box(str(err))

    def find(self, p_text):
        try:
            self.cur.execute(p_text)
            return self.cur.fetchone()[0]
        except sqlite3.Error as err:
            self.message_box(str(err))

    def db_closer(self):
        self.cur.execute("PRAGMA foreign_keys = OFF")
        self.db.close()

    def connection_state(self):
        pass
        # return self.db.


if __name__ == "__main__":
    db_manager = DbManager()
