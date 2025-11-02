import sys
from PyQt5.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget, QApplication, QPushButton, QMessageBox, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import os


class again(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Deneme")
        self.setFixedSize(1200,900)


        self.mevcut_dizin = QLabel("Mevcut dizin:", self)
        self.mevcut_dizin.move(60, 250)


        self.path = QLabel("C:\\Users\\cagla\\OneDrive\\Masaüstü", self)
        self.path.move(130, 246)
        self.path.resize(690,20)


        self.baslik = QLabel("Dosya listeleme aracı", self)
        self.baslik.move(300, 10)
        self.baslik.setFont(QFont('arial', 50))
        self.baslik.setStyleSheet("color: blue")


        self.dosya_sayisi_basligi = QLabel("Dosya:", self)
        self.dosya_sayisi_basligi.move(800, 225)

        self.dosya_sayisi = QLabel("0", self)
        self.dosya_sayisi.move(840, 225)
        self.dosya_sayisi.resize(30,10)


        self.klasor_sayisi_basligi = QLabel("Klasör:", self)
        self.klasor_sayisi_basligi.move(800, 245)


        self.klasor_sayisi = QLabel("0", self)
        self.klasor_sayisi.move(840, 245)
        self.klasor_sayisi.resize(30,10)


        self.dizin = QLineEdit(self)
        self.dizin.setPlaceholderText("Enter a directory")
        self.dizin.move(80,120)
        self.dizin.resize(1000,50)
        self.dizin.setStyleSheet("border: 1px solid black; padding: 10px; border-radius: 20px; font-size: 20px")


        self.start_button = QPushButton("Başlat", self)
        self.start_button.clicked.connect(self.start_action)
        self.start_button.setCursor(Qt.PointingHandCursor)# imlecin butonun üstüne geldiği zaman değişmesini sağlıyoruz
        self.start_button.move(500,180)
        self.start_button.resize(103,55)
        self.start_button.setStyleSheet("background-color: aqua; color: black; border-radius: 20px; border: none;")



        self.liste = QListWidget(self)
        widgetItem = QListWidgetItem(f"{self.dizin.text()}")
        self.liste.addItem(widgetItem)
        self.liste.move(60,270)
        self.liste.resize(800,600)


    def start_action(self):
        try:
            self.liste.clear()
            dizin = self.dizin.text().strip() # kullanıcını girdiği dizini alıyoruz
            path = str(dizin)
            self.path.setText(path)
            if dizin:
                dosyalar = os.listdir(dizin)
                
                dosya_sayisi = 0
                klasor_sayisi = 0

                for dosya in dosyalar:
                    dosya_yolu = os.path.join(dizin, dosya) # tam yolu oluşturuyoruz

                    if os.path.isdir(dosya_yolu):
                        klasor_sayisi += 1
                    
                    elif os.path.isfile(dosya_yolu):
                        dosya_sayisi += 1

                    self.liste.addItem(dosya) # her bir dosyayı QlistWidget'ta göstermek için döngüden faydalanıyoruz
                self.dosya_sayisi.setText(str(dosya_sayisi))
                self.klasor_sayisi.setText(str(klasor_sayisi))
                
        except FileNotFoundError:
            QMessageBox.warning(self, "uyarı", "Dizin veya dosya adı hatalı!")
        except PermissionError:
            QMessageBox.critical(self, "Hata", "Dizine erişim izniniz yok!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = again()
    pencere.show()
    sys.exit(app.exec_())

    