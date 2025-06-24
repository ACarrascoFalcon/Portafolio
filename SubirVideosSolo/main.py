# BOT DE TIKTOK AUTOMATICO PARA CONTENIDO DE TECNOLOGIA

# --- IMPORTACIONES ---
import openai
import requests
from moviepy.editor import VideoFileClip, AudioFileClip
from datetime import datetime
import os

# --- CONFIGURACION ---
openai.api_key = "TU_OPENAI_API_KEY"
ELEVEN_API_KEY = "TU_ELEVENLABS_API_KEY"
VOZ_ID = "21m00Tcm4TlvDq8ikWAM"  # Ejemplo: voz "Rachel" de ElevenLabs

# --- FUNCION PARA GENERAR GUIÓN CON CHATGPT ---
def generar_guion_tiktok():
    prompt = (
        "Crea un guion viral de TikTok (60 segundos) sobre una tendencia tecnologica actual. "
        "Incluye un gancho fuerte al inicio y termina con una pregunta al público."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# --- FUNCION PARA GENERAR VOZ DESDE TEXTO CON ELEVENLABS ---
def convertir_a_voz(texto, salida="voz.mp3"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOZ_ID}"
    headers = {
        "xi-api-key": ELEVEN_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": texto,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.4, "similarity_boost": 0.75}
    }
    response = requests.post(url, json=data, headers=headers)
    with open(salida, "wb") as f:
        f.write(response.content)
    return salida

# --- FUNCION PARA CREAR VIDEO CON AUDIO Y VIDEO BASE ---
def generar_video(voz_path, video_base="tech_clip.mp4", salida="video_final.mp4"):
    fondo = VideoFileClip(video_base).subclip(0, 60)
    audio = AudioFileClip(voz_path)
    video = fondo.set_audio(audio)
    video.write_videofile(salida, codec="libx264", audio_codec="aac")
    return salida

# --- FUNCION PRINCIPAL PARA FLUJO COMPLETO ---
def crear_video_tiktok():
    print("\n[1] Generando guion...")
    guion = generar_guion_tiktok()
    with open("guion.txt", "w", encoding="utf-8") as f:
        f.write(guion)

    print("\n[2] Convirtiendo guion a voz...")
    voz = convertir_a_voz(guion)

    print("\n[3] Generando video...")
    nombre_video = f"video_tech_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    video = generar_video(voz, salida=nombre_video)

    print(f"\n[✅] Video generado: {video}")
    return video

# --- EJECUCION ---
if __name__ == "__main__":
    crear_video_tiktok()
