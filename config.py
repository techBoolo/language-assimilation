import os

class Config:
    # Default: base.en (Fast and accurate enough for clear English)
    WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base.en")
    
    # Default: 0.5 seconds end padding
    try:
        END_PADDING = float(os.getenv("END_PADDING", "0.5"))
    except ValueError:
        END_PADDING = 0.5

    # Hardcoded constants
    START_PADDING = 0.1  # seconds
    MIN_SEGMENT_DURATION = 0.5  # seconds