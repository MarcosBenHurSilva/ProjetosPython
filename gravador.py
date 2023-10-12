import cv2
import numpy as np
import pyautogui
import pyaudio
import wave
import threading
import time
import os

# Defina a pasta de destino para o arquivo MP4
output_folder = "C:\\Users\\Usuario\\Desktop\\python"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Inicialize as configurações de tela
screen_width, screen_height = pyautogui.size()
screen_resolution = (screen_width, screen_height)

# Inicialize as configurações de captura de tela e áudio
fps = 30
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_filename = os.path.join(output_folder, f"screen_record_{time.strftime('%Y%m%d-%H%M%S')}.mp4")
audio_filename = os.path.join(output_folder, "temp_audio.wav")
video_writer = cv2.VideoWriter(video_filename, fourcc, fps, screen_resolution)
audio_frames = []

# Inicialize o PyAudio para captura de áudio do microfone
audio = pyaudio.PyAudio()
microphone_index = None  # Defina o índice do microfone
microphone_format = pyaudio.paInt16
microphone_channels = 1
microphone_rate = 44100
microphone_chunk = 1024

def record_microphone():
    global audio_frames
    microphone_stream = audio.open(
        format=microphone_format,
        channels=microphone_channels,
        rate=microphone_rate,
        input=True,
        frames_per_buffer=microphone_chunk,
        input_device_index=microphone_index
    )
    while True:
        audio_data = microphone_stream.read(microphone_chunk)
        audio_frames.append(audio_data)

# Função para iniciar/parar a gravação
recording = False

def start_stop_recording():
    global recording
    if recording:
        recording = False
    else:
        recording = True

# Monitorar a tecla F1 para iniciar/parar a gravação em uma thread separada
def monitor_key():
    while True:
        if pyautogui.hotkey("f1"):
            start_stop_recording()

# Crie uma thread para monitorar a tecla F1
key_monitor_thread = threading.Thread(target=monitor_key)
key_monitor_thread.daemon = True
key_monitor_thread.start()

# Loop principal para captura de tela e áudio
while True:
    if recording:
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_writer.write(frame)

    # Monitorar a tecla F2 para encerrar a gravação
    if pyautogui.hotkey("f2"):
        break

# Quando a gravação for encerrada
video_writer.release()

# Salve o áudio do microfone em um arquivo WAV temporário
with wave.open(audio_filename, 'wb') as wf:
    wf.setnchannels(microphone_channels)
    wf.setsampwidth(audio.get_sample_size(microphone_format))
    wf.setframerate(microphone_rate)
    wf.writeframes(b''.join(audio_frames))

# Combine o vídeo e o áudio em um único arquivo MP4
os.system(f'ffmpeg -i "{video_filename}" -i "{audio_filename}" -c:v copy -c:a aac -strict experimental "{video_filename}"')

# Remova o arquivo de áudio temporário
os.remove(audio_filename)

print(f"Gravação concluída. Vídeo salvo em {video_filename}")
