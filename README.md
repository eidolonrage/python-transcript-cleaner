# Transcript Cleaner

A simple Python GUI application to clean up transcript files by removing timestamps and speaker attributions, leaving only the content text.

## Features

- **Simple GUI**: Easy-to-use graphical interface with file picker
- **Automatic Cleaning**: Removes timestamps (e.g., "00:00:01:58 - 00:00:41:11") and speaker attributions
- **Preview**: Shows cleaned text before saving
- **Save Function**: Saves cleaned text to a new file

## Requirements

- Python 3.x
- tkinter (usually included with Python)

## Usage

1. **Run the application**:
   ```bash
   python transcript_cleaner.py
   ```

2. **Select a transcript file**:
   - Click the "Browse" button
   - Select your transcript .txt file

3. **Clean the transcript**:
   - Click "Clean Transcript" button
   - The cleaned text will appear in the preview area

4. **Save the cleaned text**:
   - Click "Save as New File" to save to a new location (recommended)
   - OR click "Overwrite Original" to replace the original file (creates a backup first)

## Input Format

The script expects transcript files in this format:

```
00:00:01:58 - 00:00:41:11
Unknown
Hi everyone, I'm Indi and welcome to the course...

00:00:41:16 - 00:01:10:44
Unknown
And in particularly in companies that trade on stock markets...
```

## Output Format

The cleaned output will contain only the content text, with paragraphs separated by double newlines:

```
Hi everyone, I'm Indi and welcome to the course...

And in particularly in companies that trade on stock markets...
```

## Files

- `transcript_cleaner.py` - Main GUI application
- `test_cleaner.py` - Test script to verify cleaning logic
- `README.md` - This documentation file

## Testing

You can test the cleaning logic without the GUI using:

```bash
python test_cleaner.py
```

This will process the `TS_1-01v_think_bigger.txt` file and create a `test_cleaned_output.txt` file for inspection.
