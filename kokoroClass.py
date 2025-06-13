from kokoro_onnx import Kokoro
import simpleaudio as sa
import soundfile as sf
import tempfile
import os

class KokoroTTS:
    def __init__(self):
        # Initialize Kokoro
        self.kokoro = Kokoro("../models/kokoro-v0_19.onnx", "../models/voices-v1.0.bin")
        # Available voices
        self.voices = [
            'af', 'af_bella', 'af_nicole', 'af_sarah', 'af_sky',
            'am_adam', 'am_michael', 'bf_emma', 'bf_isabella',
            'bm_george', 'bm_lewis'
        ]
        self.audio_path = None
        
    def generate_speech(self, text, voice, speed):
        try:
            # Generate audio
            samples, sample_rate = self.kokoro.create(
                text,
                voice=voice,
                speed=float(speed)
            )
            # Create temporary file
            temp_dir = tempfile.mkdtemp()
            temp_path = os.path.join(temp_dir, "output.wav")
            # Save to temporary file
            sf.write(temp_path, samples, sample_rate)
            self.audio_path = temp_path
            return temp_path
        except Exception as e:
            return f"Error: {str(e)}"
    
    def play_audio(self):
        try:
            print("Playing the audio file...")
            wave_obj = sa.WaveObject.from_wave_file(self.audio_path)
            play_obj = wave_obj.play()
            play_obj.wait_done()
        except Exception as e:
            print(f"An error occurred while playing the audio: {e}")
            
def main():
    app = KokoroTTS()
    app.generate_speech(
        text="Hello, this is a test of the Kokoro text-to-speech system.",
        voice='af_bella',
        speed=1.0
    )
    app.play_audio()

# if __name__ == "__main__":
#     main()