import sys
import os
from config import Config
from transcriber import Transcriber
from audio_processor import AudioBuilder
from pydub import AudioSegment

def main():
    # 1. Input Validation
    if len(sys.argv) < 2:
        print("Error: Missing input file.")
        print("Usage: python main.py <path_to_mp3>")
        sys.exit(1)

    input_path = sys.argv[1]

    if not os.path.exists(input_path):
        print(f"Error: File not found.")
        print(f"Cause: The path '{input_path}' does not exist.")
        sys.exit(1)

    # 2. Processing Start
    print("Processing...")

    try:
        # Load AI Model and Transcribe
        transcriber = Transcriber()
        segments, transcript_text = transcriber.transcribe(input_path)

        if not segments:
            print("Error: No speech detected.")
            print("Cause: The AI found no valid English sentences longer than 0.5s.")
            sys.exit(0)

        base_name, _ = os.path.splitext(input_path)
        transcript_path = f"{base_name}_transcript.txt"
        
        print(f"Saving transcript to: {transcript_path}")
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(transcript_text.strip())
            
        # Load Audio for Processing
        builder = AudioBuilder(input_path)
        final_track = AudioSegment.empty()

        # 3. Build the Drill Track
        for segment in segments:
            drill_block = builder.create_drill_block(segment['start'], segment['end'])
            final_track += drill_block

        # 4. Export File
        base_name, _ = os.path.splitext(input_path)
        output_path = f"{base_name}_drill.mp3"

        # Export (overwrites automatically)
        final_track.export(output_path, format="mp3")
        
        # Silent success (script ends)
        print(f"Done! Created: {output_path}")

    except FileNotFoundError:
        print("Error: System dependency missing.")
        print("Cause: FFmpeg is likely not installed or not in PATH.")
        sys.exit(1)
    except Exception as e:
        print("Error: An unexpected error occurred.")
        print(f"Cause: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()