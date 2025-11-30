import sys
import os
from transcriber import Transcriber

def main():
    # 1. Input Validation
    if len(sys.argv) < 2:
        print("Error: Missing input file.")
        print("Usage: python get_transcript.py <path_to_mp3>")
        sys.exit(1)

    input_path = sys.argv[1]

    if not os.path.exists(input_path):
        print(f"Error: File not found.")
        print(f"Cause: The path '{input_path}' does not exist.")
        sys.exit(1)

    # 2. Processing Start
    print(f"Transcribing '{os.path.basename(input_path)}'...")

    try:
        # Load AI Model
        transcriber = Transcriber()
        
        # We only care about the second return value (transcript_text)
        # We ignore the segments variable using '_'
        _, transcript_text = transcriber.transcribe(input_path)

        if not transcript_text:
            print("Warning: No text was detected.")

        # 3. Save the Transcript
        base_name, _ = os.path.splitext(input_path)
        output_path = f"{base_name}_transcript.txt"
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(transcript_text.strip())
            
        print("Success!")
        print(f"Saved to: {output_path}")

    except Exception as e:
        print("Error: An unexpected error occurred.")
        print(f"Cause: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()