from fastapi import FastAPI, File, UploadFile, Form
from PIL import Image
import torch
from transformers import AutoProcessor, AutoModelForVision2Seq
import io

app = FastAPI()

# Load model
processor = AutoProcessor.from_pretrained("vikhyatk/moondream2")
model = AutoModelForVision2Seq.from_pretrained("vikhyatk/moondream2")

@app.post("/analyze")
async def analyze(image: UploadFile = File(...), prompt: str = Form(...)):
    image_data = await image.read()
    img = Image.open(io.BytesIO(image_data)).convert("RGB")
    inputs = processor(images=img, text=prompt, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=64)
    result = processor.batch_decode(output, skip_special_tokens=True)[0]
    return {"response": result}
