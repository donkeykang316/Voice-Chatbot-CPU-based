import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel

class FastWhisperSTT:
    def __init__(self, model_size="base", device="cpu", compute_type="int8", duration=5, sample_rate=44100, dtype='int16', language="en"):
        self.model = WhisperModel(model_size, device=device, compute_type=compute_type)
        self.duration = duration
        self.sample_rate = sample_rate
        self.filename = 'stt.wav'
        self.dtype = dtype
        self.language = language
        
    def record_audio(self):
        print(f"Recording for {self.duration} seconds...")
        audio_data = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=2, dtype=self.dtype)
        sd.wait()
        sf.write(self.filename, audio_data, self.sample_rate)
        print(f"End of recording.")
        return self.filename
    
    def transcribe_audio(self, filename=None):
        if filename is None:
            filename = self.record_audio()
        
        segments, info = self.model.transcribe(filename, beam_size=5, language=self.language, condition_on_previous_text=False)
        transcription = ""
        for segment in segments:
            transcription += segment.text
        return transcription

# if __name__ == "__main__":
#     fast_whisper_stt = FastWhisperSTT()
#     output = fast_whisper_stt.transcribe_audio()
#     print(f"Transcription: {output}")
