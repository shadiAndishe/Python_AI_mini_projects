import threading
import time
import random

class image_classifier:
    total_images = 0 #Class var

    def __init__(self, model_name , image_size):
        self.model_name = model_name #instance var(unique to each model)
        self.image_size = image_size #instance var(different models may use different sizes)
        self.processed_image = [] #tack images processed by this instance

    def preprocess_image(self, image_name):
        time.sleep(1)
        image_classifier.total_images +=1 #modify class var
        self.processed_image.append(image_name) #modify instance var

    def classify_image(self, image_name):
        time.sleep(1)
        classes = ["meat","Fish","chicken", "vegeteraian"]
        return random.choice(classes)

    @classmethod
    def get_total_images(cls):
        """Returns the total number of processed images (class-level info)."""
        return f"Total images processed: {cls.total_images}"

    @staticmethod
    def get_supported_models():
        """Lists available AI models (not specific to any instance)."""
        return ["ResNet", "MobileNet"]

class ResNetClassifier(image_classifier):
    def __init__(self):
        super().__init__("ResNet", (224, 224))  # Call base constructor
    def classify_image(self, image_name):
        time.sleep(1)
        prediction = "ResNet Prediction: " + random.choice(["Bird", "Fish", "Car"])

class ModelFactory:
    @staticmethod
    def create_model(model_type):
        """Dynamically creates a classifier instance based on input."""
        model_mapping = {
            "ResNet": ResNetClassifier,
            "MobileNet": lambda: image_classifier("MobileNet", (128, 128))
        }
        return model_mapping.get(model_type, lambda: None)()

def process_images(model, images):
    """Runs preprocessing and classification sequentially."""
    for image in images:
        model.preprocess_image(image)
        model.classify_image(image)

if __name__ == "__main__":
    image_batch_1 = ["img1.jpg", "img2.jpg", "img3.jpg"]
    image_batch_2 = ["img4.jpg", "img5.jpg", "img6.jpg"]
    model1 = ModelFactory.create_model("ResNet")
    model2 = ModelFactory.create_model("MobileNet")
    process_images(model1, image_batch_1)
    process_images(model2, image_batch_2)
    print("\n✅ Final Statistics:")
    print(image_classifier.get_total_images())