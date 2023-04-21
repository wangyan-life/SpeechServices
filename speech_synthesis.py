import os
import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# Note: the voice setting will not overwrite the voice element in input SSML.
# 代码                        姓名     性别   语言      备注
# zh-CN-XiaoxiaoNeural        晓晓     女    普通话    年轻人
# zh-CN-XiaoshuangNeural      晓双     女    普通话    儿童
# zh-CN-YunxiNeural           云希     男    普通话    年轻人
# zh-CN-YunyangNeural         云扬     男    普通话    年轻人
# zh-CN-shaanxi-XiaoniNeural  晓妮     女    陕西话    年轻人
# zh-HK-HiuMaanNeural         曉曼     女    粤语      年轻人
# de-DE-GiselaNeural          Gisela   女    德语      儿童
# de-DE-AmalaNeural           Amala    女    德语      年轻人
# ja-JP-AoiNeural             Aoi      女    日语      儿童
# ja-JP-MayuNeural            Mayu     女    日语      年轻人
# fr-FR-EloiseNeural          Eloise   女    法语      儿童
# fr-FR-BrigitteNeural        Brigitte 女    法语      年轻人
# en-US-AriaNeural            Aria     女    英语      年轻人
# en-US-AmberNeural           Amber    女    英语      年轻人
# es-ES-AbrilNeural           Abril    女    西班牙语  年轻人
# es-ES-IreneNeural           Irene    女    西班牙语  儿童
# ru-RU-DariyaNeural          Dariya   女    俄语      年轻人
speech_config.speech_synthesis_voice_name = "zh-CN-XiaoshuangNeural"
text = "风华正茂的年纪不该困在爱与不爱里，我希望你可以热烈而又温柔的生活，做你觉得要紧的事，走你认为善良的路。少理那些满身是嘴的怪物，别在意别人口中的自己，做喜欢的自己才是最重要的。没有结果的事就不要再执着那么久了，人生那么长，那一城一墙的得失，和想去的远方相比，实在不算什么。摆弄好手里的柴米油盐，保护好心中的诗和远方。葡萄树上开不出百合花，找不到答案的时候就找自己，风华正茂的年纪，你该所向披靡。​​"

# use the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
result = speech_synthesizer.speak_text_async(text).get()

# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))