from pydub import AudioSegment
from config import Config

class AudioBuilder:
    def __init__(self, audio_path):
        # Load the full audio file into memory
        self.original_audio = AudioSegment.from_file(audio_path)

    def create_drill_block(self, start_sec, end_sec):
        """
        Creates a block: [0.1s Silence] + [Audio] + [End Pad] + [Repetition Silence]
        """
        # Convert seconds to milliseconds for pydub
        start_ms = start_sec * 1000
        end_ms = end_sec * 1000
        
        # 1. Slice the original audio
        segment_audio = self.original_audio[start_ms:end_ms]
        
        # 2. Generate Silence Segments
        # Pydub works in milliseconds
        start_pad_ms = Config.START_PADDING * 1000
        end_pad_ms = Config.END_PADDING * 1000
        
        silence_start = AudioSegment.silent(duration=start_pad_ms)
        silence_end = AudioSegment.silent(duration=end_pad_ms)
        
        # 3. Construct the Audio Portion
        # Logic: Start Pad + Audio Slice + End Pad
        audio_portion = silence_start + segment_audio + silence_end
        
        # 4. Calculate Repetition Gap
        # The gap must be exactly as long as the audio portion we just built
        repetition_gap_duration = len(audio_portion)
        repetition_gap = AudioSegment.silent(duration=repetition_gap_duration)
        
        # 5. Combine and Return
        return audio_portion + repetition_gap