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

