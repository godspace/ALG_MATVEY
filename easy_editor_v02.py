from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
 
 
import os
from PIL import Image, ImageFilter
import shutil
 
#создаём приложение, и окно с указанным размером
app = QApplication([])
window = QWidget()
window.resize(1600, 800)
 
#создаём основную направляющую линию
mainlayout = QHBoxLayout()
window.setLayout(mainlayout)
 
#создаём левую, правую направляющую линию и линию для кнопок снизу
leftlayout = QVBoxLayout()
rightlayout = QVBoxLayout()
buttonslayout = QHBoxLayout()
 
#вешаем на основную линию левую и правую линии 
mainlayout.addLayout(leftlayout)
mainlayout.addLayout(rightlayout)
 
#делаем кнопу и окно списка файлов
open_folder_btn = QPushButton("Открыть папку")
pic_list_widget = QListWidget()
 
#вешаем их на левую линию
leftlayout.addWidget(open_folder_btn)
leftlayout.addWidget(pic_list_widget)
 
#создаём рамку для картинки и запоминаем её ширину и высоту
img_placeholder = QLabel("МЕСТО ДЛЯ КАРТИНКИ")
w, h = img_placeholder.width(), img_placeholder.height()
rightlayout.addWidget(img_placeholder)
 
 
#делаем кнопки для редактирования
left_btn = QPushButton("Влево 90")
right_btn = QPushButton("Вправо 90")
mirror_btn = QPushButton("Зеркало")
sharpness_btn = QPushButton("Резкость")
bw_btn = QPushButton("Ч/Б")
 
#развешиваем кнопки для редактирования
buttonslayout.addWidget(left_btn)
buttonslayout.addWidget(right_btn)
buttonslayout.addWidget(mirror_btn)
buttonslayout.addWidget(sharpness_btn)
buttonslayout.addWidget(bw_btn)
rightlayout.addLayout(buttonslayout)
 
 
class Image_Processor():
    def __init__(self):
        self.source_dir = "адрес исходной папки с картинками"
        self.edited_dir = "адрес новой папки для изменённых картинок"
        self.file_name = "название файла с расширением(.png, .jpg и т.д.)"
        self.full_file_name = "полное имя файла(адрес папки + название файла)"
 
    def open_folder(self):
        pic_list_widget.clear()
        self.source_dir = QFileDialog.getExistingDirectory(window)
        self.edited_dir = os.path.join(self.source_dir,'Edited')
        if os.path.exists(self.edited_dir):
            print(False)
            pass
        else:
            os.mkdir(self.edited_dir)
        files = os.listdir(self.source_dir)
        filter_list = ('jpg','jpeg', 'png', 'gif', 'bmp')
        for file in files:
            for filter in filter_list:
                if file.lower().endswith(filter):
                    pic_list_widget.addItem(file)
                    src = os.path.join(self.source_dir,file)
                    dst = os.path.join(self.edited_dir,file)
                    shutil.copyfile(src, dst)
    def open_img_for_preview(self):
        #название файла
        self.file_name = pic_list_widget.currentItem().text()
        #полный путь к файлу
        self.full_file_name = os.path.join(self.edited_dir, self.file_name)
        #открытие картики и установка в окно
        image = QPixmap(self.full_file_name).scaled(w, h, Qt.KeepAspectRatio)
        img_placeholder.setPixmap(image)
    def left_90(self):
        image = Image.open(self.full_file_name)
        rotate = image.rotate(90, expand=1)
        rotate.save(self.full_file_name)
        self.open_img_for_preview()
 
 
editor = Image_Processor()
open_folder_btn.clicked.connect(editor.open_folder)
pic_list_widget.clicked.connect(editor.open_img_for_preview)
left_btn.clicked.connect(editor.left_90)
window.show()
app.exec()