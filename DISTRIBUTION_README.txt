TRANSCRIPT CLEANER - STANDALONE EXECUTABLE
==========================================

This package contains a standalone executable version of the Transcript Cleaner tool.
No Python installation is required to run this application.

CONTENTS:
---------
- TranscriptCleaner.exe    (The main application - 10.3 MB)
- DISTRIBUTION_README.txt  (This file)

HOW TO USE:
-----------
1. Double-click "TranscriptCleaner.exe" to launch the application
2. Click "Browse" to select your transcript file (.txt format)
3. Click "Clean Transcript" to process the file
4. Choose how to save:
   - "Save as New File" - Save to a new location
   - "Overwrite Original" - Replace the original file (creates backup)

SUPPORTED TRANSCRIPT FORMAT:
----------------------------
The tool expects transcript files in this format:

00:00:01:58 - 00:00:41:11
Unknown
Hi everyone, I'm Indi and welcome to the course...

00:00:41:16 - 00:01:10:44
Unknown
And in particularly in companies that trade on stock markets...

OUTPUT:
-------
The cleaned output will contain only the content text:

Hi everyone, I'm Indi and welcome to the course...

And in particularly in companies that trade on stock markets...

SYSTEM REQUIREMENTS:
--------------------
- Windows 10 or later (64-bit)
- No additional software required

TROUBLESHOOTING:
---------------
- If Windows shows a security warning, click "More info" then "Run anyway"
- The first launch may take a few seconds as Windows scans the executable
- If the application doesn't start, try running as administrator

TECHNICAL DETAILS:
-----------------
- File size: ~10.3 MB
- Built with PyInstaller
- Self-contained executable (no dependencies)
- Includes Python runtime and all required libraries

For questions or issues, please contact the developer.

Version: 1.0
Created: August 2025
