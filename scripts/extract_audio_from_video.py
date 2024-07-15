from moviepy.editor import VideoFileClip


def extract_audio_from_video(video_path, audio_output_path):
    # 加载视频文件
    video = VideoFileClip(video_path)

    # 提取音频部分
    audio = video.audio

    # 保存音频为 WAV 文件
    audio.write_audiofile(audio_output_path, codec="pcm_s16le")


if __name__ == "__main__":
    video_path = (
        "../assets/Ado COVER《unravel》2023 武道館 LIVE.mp4"  # 替换为你的视频文件路径
    )
    audio_output_path = (
        "Ado COVER《unravel》2023 武道館 LIVE.wav"  # 设置输出的音频文件路径
    )

    extract_audio_from_video(video_path, audio_output_path)
    print(f"音频已成功提取并保存到 {audio_output_path}")
