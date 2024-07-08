import os
import wave
from pathlib import Path

import pyaudio
from dotenv import load_dotenv
from gradio_client import Client, handle_file

load_dotenv()

COSY_VOICE_BASE_URL = os.getenv("COSY_VOICE_BASE_URL", "http://192.168.1.180:50000/")
SENSE_VOICE_BASE_URL = os.getenv("SENSE_VOICE_BASE_URL", "http://192.168.1.180:57860/")

gradio_tts_client = Client(COSY_VOICE_BASE_URL)
gradio_asr_client = Client(SENSE_VOICE_BASE_URL)

prompt_text = """
hello,大家好，我在上期视频当中呢有给大家提一个建议，就是一定要在求职的时候选好适合自己的赛道。那么就有很多朋友后台私信我说，这个赛道到底该怎么选。
"""

prompt_wav_upload_path = "prompt_wav_upload.wav"


def play_audio(file_path: str):
    # Open the WAV file
    wf = wave.open(file_path, "rb")

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open a stream
    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True,
    )

    # Read data in chunks
    chunk_size = 1024
    data = wf.readframes(chunk_size)

    # Play the audio
    while data:
        stream.write(data)
        data = wf.readframes(chunk_size)

    # Clean up
    stream.stop_stream()
    stream.close()
    p.terminate()


def gradio_tts(tts_text: str, seed: int = 0, **kwargs):
    # logger.debug("提交 @tts 任务")
    result = gradio_tts_client.predict(
        tts_text=tts_text,
        mode_checkbox_group="3s极速复刻",
        sft_dropdown="中文女",
        prompt_text=prompt_text.strip(),
        prompt_wav_upload=handle_file(prompt_wav_upload_path),
        prompt_wav_record=None,
        instruct_text="",
        seed=seed,
        api_name="/generate_audio",
    )
    # logger.debug("任务结束")

    # logger.debug("正在播放音频...")
    audio_path = Path(result)
    if audio_path.is_file():
        play_audio(str(audio_path.resolve()))


def gradio_asr(input_wav, language: str = "zh", **kwargs):
    result = gradio_asr_client.predict(
        input_wav=handle_file(input_wav), language=language, api_name="/model_inference"
    )
    return result
