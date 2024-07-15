import numpy as np
import sounddevice as sd
import wave


def read_audio_file(file_path):
    with wave.open(file_path, "rb") as wf:
        sample_rate = wf.getframerate()
        channels = wf.getnchannels()
        frames = wf.readframes(wf.getnframes())
        audio_data = np.frombuffer(frames, dtype=np.int16)
        if channels > 1:
            audio_data = audio_data.reshape((-1, channels))
        return audio_data, sample_rate


def play_audio_to_virtual_mic(audio_data, sample_rate=44100):
    # 查找 VB-Audio Virtual Cable 设备索引
    virtual_mic_index = None
    for i, device in enumerate(sd.query_devices()):
        if "Virtual" in device["name"] and device["max_output_channels"] > 0:
            virtual_mic_index = i
            break

    if virtual_mic_index is None:
        raise Exception("VB-Audio Virtual Cable not found")

    # 播放音频数据到虚拟麦克风设备
    sd.play(audio_data, samplerate=sample_rate, device=virtual_mic_index)
    sd.wait()


if __name__ == "__main__":
    file_path = (
        "../assets/Ado COVER《unravel》2023 武道館 LIVE.WAV"  # 替换为你的音频文件路径
    )

    # 读取音频文件
    audio_data, sample_rate = read_audio_file(file_path)

    # 播放音频数据到虚拟麦克风设备
    play_audio_to_virtual_mic(audio_data, sample_rate)
