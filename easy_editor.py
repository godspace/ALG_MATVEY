from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os
from PIL import Image, ImageFilter

#
app = QApplication([])
window = QWidget()
window.resize(1600, 800)

#
mainlayout = QHBoxLayout()
window.setLayout(mainlayout)

#
leftlayout = QVBoxLayout()
rightlayout = QVBoxLayout()
buttonslayout = QHBoxLayout()

#
mainlayout.addLayout(leftlayout)
mainlayout.addLayout(rightlayout)

#
open_folder_btn = QPushButton("Открыть папку")
pic_list_widget = QListWidget()

#
leftlayout.addWidget(open_folder_btn)
leftlayout.addWidget(pic_list_widget)

#
img_placeholder = QLabel("МЕСТО ДЛЯ КАРТИНКИ")
w, h = img_placeholder.width(), img_placeholder.height()
rightlayout.addWidget(img_placeholder)

#
left_btn = QPushButton("Влево 90")
right_btn = QPushButton("Вправо 90")
mirror_btn = QPushButton("Зеркало")
sharpness_btn = QPushButton("Резкость")
bw_btn = QPushButton("Ч/Б")

#
buttonslayout.addWidget(left_btn)
buttonslayout.addWidget(right_btn)
buttonslayout.addWidget(mirror_btn)
buttonslayout.addWidget(sharpness_btn)
buttonslayout.addWidget(bw_btn)
rightlayout.addLayout(buttonslayout)

source_dir = "переменная для хранения адреса исходной папки с картинками"
edited_dir = "переменная для хранения адреса новой папки для изменённых картинок"
full_file_name = "полное имя файла"

#
def open_folder():
    global source_dir, edited_dir
    pic_list_widget.clear()
    source_dir = QFileDialog.getExistingDirectory(window)
    files = os.listdir(source_dir)
    print(files)
    filter_list = ('jpg','jpeg', 'png', 'gif', 'bmp')
    for file in files:
        for filter in filter_list:
            if file.lower().endswith(filter):
                pic_list_widget.addItem(file)

#
open_folder_btn.clicked.connect(open_folder)

#
def open_img_for_preview():
    global source_dir, edited_dir, full_file_name
    #
    file_name = pic_list_widget.currentItem().text()
    #
    full_file_name = os.path.join(source_dir,file_name)
    #
    image = QPixmap(full_file_name).scaled(w, h, Qt.KeepAspectRatio)
    img_placeholder.setPixmap(image)
    open_img_for_edit(file_name)

#    
def open_img_for_edit(file_name):    
    global source_dir, edited_dir, full_file_name
    #
    edited_dir = os.path.join(source_dir,'Edited')
    #
    if os.path.exists(edited_dir):
        pass
    else:
        os.mkdir(edited_dir)
    #
    image = Image.open(full_file_name)
    
    #
    full_file_name = os.path.join(edited_dir,file_name)
    image.save(full_file_name)
    
#
pic_list_widget.clicked.connect(open_img_for_preview)

def show_edited():
    global source_dir, edited_dir, full_file_name
    image = QPixmap(full_file_name).scaled(w, h, Qt.KeepAspectRatio)
    img_placeholder.setPixmap(image)
    
def left_90():
    global source_dir, edited_dir, full_file_name
    image = Image.open(full_file_name)
    rotate = image.rotate(90, expand=1)
    rotate.save(full_file_name)
    show_edited()
left_btn.clicked.connect(left_90)

#
window.show()
app.exec()