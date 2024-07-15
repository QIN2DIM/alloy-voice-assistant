# Sample AI assistant

You need an `OPENAI_API_KEY` and a `GOOGLE_API_KEY` to run this code. Store them in a `.env` file in the root directory of the project, or set them as environment variables.


If you are running the code on Apple Silicon, run the following command:

```
$ brew install portaudio
```

Create a virtual environment, update pip, and install the required packages:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -U pip
$ pip install -r requirements.txt
```

Run the assistant:

```
$ python3 assistant.py
```

## S2S Request 复现 Video <问, 答>

1. 【1】Real-time @asr（SenseVoice）
2. [1] LLM Chain （GPT-4o） 处理视觉和文本，根据 prompt 和身份设定，output 口语化的中文内容
3. [1]CosyVoice @tts zero-shot 朗读中文内容

## WSS 双工通信复现 WebRTC

1. SenseVoice wss server，双向阀语音唤醒
2. [x] CosyVoice SFT 快速唤醒



### FunASR 实时语音识别服务

[Documentation](https://github.com/modelscope/FunASR/blob/main/runtime/docs/SDK_advanced_guide_online_zh.md)

```bash
cd FunASR/runtime
nohup bash run_server_2pass.sh \
  --download-model-dir /workspace/models \
  --vad-dir damo/speech_fsmn_vad_zh-cn-16k-common-onnx \
  --model-dir damo/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-onnx  \
  --online-model-dir damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-online-onnx  \
  --punc-dir damo/punc_ct-transformer_zh-cn-common-vad_realtime-vocab272727-onnx \
  --lm-dir damo/speech_ngram_lm_zh-cn-ai-wesp-fst \
  --itn-dir thuduj12/fst_itn_zh \
  --hotword /workspace/models/hotwords.txt > log.txt 2>&1 &
```

```bash
cd FunASR/runtime
nohup bash run_server.sh \
  --download-model-dir /workspace/models \
  --vad-dir damo/speech_fsmn_vad_zh-cn-16k-common-onnx \
  --model-dir iic/SenseVoiceSmall \
  --punc-dir damo/punc_ct-transformer_cn-en-common-vocab471067-large-onnx \
  --lm-dir damo/speech_ngram_lm_zh-cn-ai-wesp-fst \
  --itn-dir thuduj12/fst_itn_zh \
  --hotword /workspace/models/hotwords.txt > log.txt 2>&1 &
```

## TODO

1. 🎶 CABLE Output (VB-Audio Virtual Cable) microphone input device

   结论：系统内播放的音频，将通过 CABLE 传输到 microphone

2. `xhs 直播间`、`会议软件`、`WebRTC 泛用型场景` 音频输入接口

   结论：直接播放音频即可，在麦克风设置项选择 CABLE

3. LMM 语音交互 baseline

   - [ ] 音频文件写入测试，也即，“将离线音频文件通过 microphone 发送到 live”
   - [ ] (4~20s) 流式响应，也即，“模型输出能通过 microphone cable channel 发送到 live”
   - [ ] (<1s) 延时优化
   - [ ] (Nice TO Have) 双工通信

4. LMM 高级交互 best-cases

   1. “看见”弹幕，语音交互
   2. zero-shot 3s voice copy
   3. 用任意玩家音色唱歌
   4. GraphRAG + CV/NLP Toolkit
   5. （A+）24h 情感陪伴
















