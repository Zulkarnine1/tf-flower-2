# Imports
from PIL import Image, UnidentifiedImageError
import io
import numpy as np


# Class to preprocess the image before making prediction
class ImageProcessor:
    def __init__(self):
        pass

    def process_image(self,image,SIZE):
        pil_image = Image.open(io.BytesIO(image))
        print(pil_image)
        if pil_image.mode == 'RGBA':
            pil_image = pil_image.convert('RGB')
        elif pil_image.mode == 'P':
            pil_image = pil_image.convert('RGB')

        # Resize image to expected input shape
        pil_image = pil_image.resize((SIZE, SIZE))

        # Convert image into numpy format
        numpy_image = np.array(pil_image).reshape((SIZE, SIZE, 3))
        return numpy_image
