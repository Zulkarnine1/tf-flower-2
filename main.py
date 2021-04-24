# Imports
from fastapi import FastAPI, HTTPException, UploadFile,File
from PIL import  UnidentifiedImageError
from pydantic import BaseModel
import sys
import uvicorn

# Local imports
from imageProcessor import ImageProcessor
from predictionManager import PredictionManager




# Constants
SIZE = 150


# Objects
image_processor = ImageProcessor()
prediction_manager = PredictionManager()


# Server app start
app = FastAPI()

# Define the Response


class Prediction(BaseModel):
  prediction: str

class Item(BaseModel):
  file: str

# Define the main route
@app.get('/')
def root_route():
  return {'Message': 'Please post the image you want to predict at /prediction route as json data or at /predictionform as formdata.'}


# Define the /prediction route
@app.post('/prediction', response_model=Prediction)
async def prediction_route(item:Item):

  try:
      # Image processing

      processed_image = image_processor.process_image(item.file,SIZE)

      # Making prediction
      likely_class = prediction_manager.predict(processed_image)
      print(likely_class)

      return {
          'prediction': likely_class
      }
  except  UnidentifiedImageError:
      raise HTTPException(status_code=500, detail=str("File is not of image format. Please upload an image file."))
  except :
      e = sys.exc_info()[1]
      print(sys.exc_info())
      raise HTTPException(status_code=500, detail=str(e))


# Define the /predictionform route
@app.post('/predictionform', response_model=Prediction)
async def predictionform_route(file: UploadFile = File(...)):

  try:
      # Image processing

      contents = await file.read()
      processed_image = image_processor.process_imageform(contents, SIZE)

      # Making prediction
      likely_class = prediction_manager.predict(processed_image)
      print(likely_class)

      return {
          'prediction': likely_class
      }
  except  UnidentifiedImageError:
      raise HTTPException(status_code=500, detail=str("File is not of image format. Please upload an image file."))
  except :
      e = sys.exc_info()[1]
      print(sys.exc_info())
      raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    uvicorn.run(app)








