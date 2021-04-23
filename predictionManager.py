# Imports
from tensorflow.keras.models import load_model, model_from_json
import numpy as np

# Constants
FILEPATH = './saved_models/conv_model1.h5'
CLASSES = ['sunflower', 'tulip', 'daisy', 'rose', 'dandelion']




# Class to make prediciton from the pretrained model
class PredictionManager:
    def __init__(self):
        with open('./saved_models/model.json', 'r') as json_file:
            json_savedModel = json_file.read()
        model = model_from_json(json_savedModel)
        model.load_weights("./saved_models/weights.h5")
        self.model = model

    def predict(self, image):
        # Generate prediction
        prediction_array = np.array([image])
        predictions = self.model.predict(prediction_array)
        prediction = predictions[0]
        likely_class_i = np.argmax(prediction)
        likely_class = CLASSES[likely_class_i]
        return likely_class