class Image_Processor:
    image_format = JPEG #class variable(shared)

    def __init__(self, model_name, img_size):
        self.model_name = model_name
        self.img_size = img_size

    def process_img(self):
        return