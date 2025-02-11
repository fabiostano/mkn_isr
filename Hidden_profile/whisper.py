from fastapi import FastAPI, WebSocket
import whisper

app = FastAPI()
model = whisper.load_model("base")  # Load desired Whisper model

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        audio_data = await websocket.receive_bytes()
        result = model.transcribe(audio_data)
        await websocket.send_text(result["text"])
