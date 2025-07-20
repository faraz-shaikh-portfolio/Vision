# Vision API with Moondream2

This is a simple FastAPI application that uses Moondream2 vision-language model.

## How to run locally
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Endpoint
POST /analyze
- Form: `prompt` = your question
- File: `image` = image file (JPG/PNG)

## Example Prompt
"What is happening in this image?"
