from ultralytics import YOLO
from PIL import Image
import os

model= YOLO('UgurKavalstaj.pt')
path = "Test"

for i in os.listdir(path=path):
    dosya = os.path.join(path, i)
    dosya = Image.open(dosya)
    sonuc = model.predict(conf=0.6, source=dosya, save=True)

