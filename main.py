
from PIL import Image
from PIL import ImageFilter

class ImageEditor():
    def __init__(self,name):
        self.name = name
        self.original = Image.open(name)
        self.imagelist = []      
    def left(self):
        save_rotate = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.imagelist.append(save_rotate)
    

    #создай конструктор класса

    #создай метод "открыть и показать оригинал"

    #создай методы для редактирования оригинала

#создай объект класса ImageEditor с данными картинки-оригинала
image = ImageEditor('original.jpg')
image.left()
image.imagelist[0].show()
#отредактируй изображение и сохрани результат