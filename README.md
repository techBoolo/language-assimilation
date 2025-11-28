# Audio Assimilation Drill Tool

A local command-line tool that automatically transforms spoken English audio files into **"Listen & Repeat"** drills for language shadowing and assimilation practice.

## 📖 How It Works

This tool uses OpenAI's **Whisper** (running locally on your machine) to detect sentences in an MP3 conversation. It then reconstructs the audio into a drill format:

1.  **Listens:** Plays the sentence.
2.  **Pauses:** Inserts a silence gap exactly equal to the length of that sentence.
3.  **Repeats:** You speak during the gap to practice intonation and rhythm.

### Drill Block Structure
For every sentence detected, the audio is generated as follows:
```text
[0.1s Start Pad] + [Sentence Audio] + [End Pad (Default 0.5s)] + [Repetition Silence Gap]
```
*The "Repetition Silence Gap" is calculated automatically to match the total duration of the audio block, ensuring you have exactly enough time to repeat what was said.*

---

## 🛠 Prerequisites

Before running the tool, you must have the following installed:

1.  **Python 3.10+**
2.  **FFmpeg** (Required for audio processing)
    *   **macOS:** `brew install ffmpeg`
    *   **Ubuntu/Debian:** `sudo apt install ffmpeg`
    *   **Windows:** [Download and add to PATH](https://ffmpeg.org/download.html)

---

## 🚀 Installation

1.  **Clone or Download this repository**
    ```bash
    git clone <your-repo-url>
    cd drill-tool
    ```

2.  **Create a Virtual Environment (Recommended)**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## 💻 Usage

Run the script by passing your source MP3 file as an argument:

```bash
python main.py my_lesson.mp3
```

### Output
The tool will process the file and generate a new MP3 in the **same directory** with the suffix `_drill`.

*   **Input:** `my_lesson.mp3`
*   **Output:** `my_lesson_drill.mp3`

*(Note: If the output file already exists, it will be overwritten automatically.)*

---

## ⚙️ Configuration

You can customize the behavior using **Environment Variables** without changing the code.

| Variable | Default | Description |
| :--- | :--- | :--- |
| `WHISPER_MODEL` | `base.en` | The AI model size. Options: `base.en` (Fast), `small.en` (Balanced), `medium.en` (Accurate). |
| `END_PADDING` | `0.5` | The silence (in seconds) added immediately after the sentence audio, before the repetition gap starts. |

### Example: Running with Custom Settings

**Mac/Linux:**
```bash
# Use a larger model and longer padding
WHISPER_MODEL=small.en END_PADDING=1.0 python main.py my_lesson.mp3
```

**Windows (PowerShell):**
```powershell
$env:WHISPER_MODEL="small.en"; python main.py my_lesson.mp3
```

---

## 📂 Project Structure

*   **`main.py`**: The entry point. Handles arguments and orchestrates the process.
*   **`config.py`**: Manages environment variables and default settings.
*   **`transcriber.py`**: Wraps OpenAI Whisper to detect and filter sentences.
*   **`audio_processor.py`**: Uses `pydub` to slice, pad, and concatenate audio.
*   **`requirements.txt`**: List of Python dependencies.

---

## ❓ Troubleshooting

**Error: `System dependency missing. Cause: FFmpeg is likely not installed...`**
*   This means `pydub` cannot find FFmpeg on your system. Please verify you installed FFmpeg and that it is accessible in your system's PATH. Type `ffmpeg -version` in your terminal to check.

**Error: `AttributeError: module 'whisper' has no attribute 'load_model'`**
*   This usually happens if you have a file named `whisper.py` in your folder (rename it!), or if you installed the wrong library. Ensure you ran `pip install -r requirements.txt` (which installs `openai-whisper`, not `whisper`).

---

## 📄 License
MIT License. Feel free to modify and use for your personal language learning journey.