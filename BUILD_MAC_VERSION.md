# Building Mac Version of Transcript Cleaner

## Prerequisites
- macOS computer (Intel or Apple Silicon)
- Python 3.7+ installed (usually pre-installed on Mac)

## Step-by-Step Instructions

### 1. Transfer Files to Mac
Copy these files to your Mac:
- `transcript_cleaner.py`
- `TS_1-01v_think_bigger.txt` (for testing)

### 2. Install PyInstaller
Open Terminal and run:
```bash
pip3 install pyinstaller
```

If you get permission errors, try:
```bash
pip3 install --user pyinstaller
```

### 3. Navigate to Project Directory
```bash
cd /path/to/your/transcript-cleaner-files
```

### 4. Create Mac Executable
Run this command:
```bash
pyinstaller --onefile --windowed --name "TranscriptCleaner" transcript_cleaner.py
```

### 5. Find Your Executable
The Mac app will be created in:
```
dist/TranscriptCleaner
```

### 6. Test the Application
```bash
open dist/TranscriptCleaner
```

### 7. Create Distribution Package
```bash
mkdir TranscriptCleaner_Mac_Distribution
cp dist/TranscriptCleaner TranscriptCleaner_Mac_Distribution/
cp DISTRIBUTION_README.txt TranscriptCleaner_Mac_Distribution/
```

## Alternative Build Commands

### For Universal Binary (Intel + Apple Silicon):
```bash
pyinstaller --onefile --windowed --target-arch universal2 --name "TranscriptCleaner" transcript_cleaner.py
```

### For App Bundle (.app):
```bash
pyinstaller --onedir --windowed --name "TranscriptCleaner" transcript_cleaner.py
```
This creates `TranscriptCleaner.app` in the `dist` folder.

## Expected Results
- **File Size:** ~15-20 MB (larger than Windows due to Python runtime)
- **Format:** Unix executable or .app bundle
- **Compatibility:** macOS 10.13+ (depending on Python version)

## Distribution Notes
- Mac users can double-click to run (no installation needed)
- First run may show security warning - users need to right-click → "Open"
- For wider distribution, consider code signing (requires Apple Developer account)

## Troubleshooting

### If PyInstaller isn't found:
```bash
python3 -m pip install pyinstaller
python3 -m PyInstaller --onefile --windowed --name "TranscriptCleaner" transcript_cleaner.py
```

### If tkinter issues occur:
```bash
brew install python-tk
```

### For permission issues:
```bash
chmod +x dist/TranscriptCleaner
```

## Cross-Platform Distribution
Once you have both versions:
- Windows: `TranscriptCleaner.exe` (10.3 MB)
- Mac: `TranscriptCleaner` (15-20 MB)

You can distribute both in separate folders or create a unified package with platform-specific instructions.
