import whisper
import warnings
from config import Config

class Transcriber:
    def __init__(self):
        # Suppress FP16 warnings on CPU
        warnings.filterwarnings("ignore")
        self.model = whisper.load_model(Config.WHISPER_MODEL)

    def transcribe(self, audio_path):
        """
        Transcribes audio and returns filtered segments.
        Forces English language detection.
        """
        # language="en" forces English model behavior
        result = self.model.transcribe(audio_path, language="en")
        
        valid_segments = []
        
        for segment in result['segments']:
            duration = segment['end'] - segment['start']
            
            # Filter out short noises (breaths, clicks)
            if duration >= Config.MIN_SEGMENT_DURATION:
                valid_segments.append({
                    'start': segment['start'],
                    'end': segment['end'],
                    'text': segment['text'].strip() # Store text for potential future use
                })
                
        return valid_segments, result["text"]