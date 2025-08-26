#!/usr/bin/env python3
"""
Transcript Cleaner - A GUI tool to clean up transcript files
Removes timestamps and speaker attributions, keeping only the content text.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import re
import os


class TranscriptCleaner:
    def __init__(self, root):
        self.root = root
        self.root.title("Transcript Cleaner")
        self.root.geometry("800x600")
        
        # Variables
        self.input_file_path = tk.StringVar()
        self.cleaned_text = ""
        
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface"""
        # Main frame
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="Transcript Cleaner", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 20))
        
        # File selection frame
        file_frame = tk.Frame(main_frame)
        file_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(file_frame, text="Select transcript file:").pack(anchor=tk.W)
        
        file_input_frame = tk.Frame(file_frame)
        file_input_frame.pack(fill=tk.X, pady=(5, 0))
        
        self.file_entry = tk.Entry(file_input_frame, textvariable=self.input_file_path, 
                                  state="readonly", width=60)
        self.file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        browse_button = tk.Button(file_input_frame, text="Browse", 
                                 command=self.browse_file)
        browse_button.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Clean button
        clean_button = tk.Button(main_frame, text="Clean Transcript", 
                                command=self.clean_transcript, 
                                bg="#4CAF50", fg="white", font=("Arial", 12))
        clean_button.pack(pady=(0, 20))
        
        # Preview frame
        preview_frame = tk.Frame(main_frame)
        preview_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(preview_frame, text="Cleaned Text Preview:").pack(anchor=tk.W)
        
        # Text area with scrollbar
        self.text_area = scrolledtext.ScrolledText(preview_frame, wrap=tk.WORD, 
                                                  height=15, width=80)
        self.text_area.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # Save buttons frame
        save_frame = tk.Frame(main_frame)
        save_frame.pack(pady=(20, 0))

        save_new_button = tk.Button(save_frame, text="Save as New File",
                                   command=self.save_cleaned_text,
                                   bg="#2196F3", fg="white", font=("Arial", 12))
        save_new_button.pack(side=tk.LEFT, padx=(0, 10))

        save_original_button = tk.Button(save_frame, text="Overwrite Original",
                                        command=self.save_to_original,
                                        bg="#FF9800", fg="white", font=("Arial", 12))
        save_original_button.pack(side=tk.LEFT)
    
    def browse_file(self):
        """Open file dialog to select transcript file"""
        file_path = filedialog.askopenfilename(
            title="Select Transcript File",
            filetypes=[
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.input_file_path.set(file_path)
    
    def clean_transcript(self):
        """Clean the selected transcript file"""
        if not self.input_file_path.get():
            messagebox.showerror("Error", "Please select a transcript file first.")
            return
        
        try:
            with open(self.input_file_path.get(), 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Clean the transcript
            self.cleaned_text = self.process_transcript(content)
            
            # Display in text area
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, self.cleaned_text)
            
            messagebox.showinfo("Success", "Transcript cleaned successfully!")
            
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def process_transcript(self, content):
        """
        Process the transcript content to remove timestamps and speaker attributions
        
        Args:
            content (str): Raw transcript content
            
        Returns:
            str: Cleaned transcript content
        """
        lines = content.split('\n')
        cleaned_lines = []
        
        # Regex pattern for timestamp (e.g., "00:00:01:58 - 00:00:41:11")
        timestamp_pattern = re.compile(r'^\d{2}:\d{2}:\d{2}:\d{2}\s*-\s*\d{2}:\d{2}:\d{2}:\d{2}$')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines
            if not line:
                i += 1
                continue
            
            # Check if this line is a timestamp
            if timestamp_pattern.match(line):
                # Skip timestamp line
                i += 1
                
                # Skip speaker attribution line (next non-empty line after timestamp)
                while i < len(lines) and not lines[i].strip():
                    i += 1
                
                if i < len(lines):
                    # This should be the speaker attribution line - skip it
                    i += 1
                    
                    # Now collect the content text until we hit the next timestamp or end
                    content_lines = []
                    while i < len(lines):
                        next_line = lines[i].strip()
                        
                        # If we hit another timestamp, break
                        if timestamp_pattern.match(next_line):
                            break
                        
                        # If it's not empty, add to content
                        if next_line:
                            content_lines.append(next_line)
                        
                        i += 1
                    
                    # Join content lines and add to cleaned text
                    if content_lines:
                        cleaned_lines.append(' '.join(content_lines))
            else:
                # If it's not a timestamp, just add the line (fallback)
                cleaned_lines.append(line)
                i += 1
        
        # Join all cleaned content with double newlines for paragraph separation
        return '\n\n'.join(cleaned_lines)
    
    def save_cleaned_text(self):
        """Save the cleaned text to a new file"""
        if not self.cleaned_text:
            messagebox.showerror("Error", "No cleaned text to save. Please clean a transcript first.")
            return
        
        # Suggest a filename based on the input file
        input_file = self.input_file_path.get()
        if input_file:
            base_name = os.path.splitext(os.path.basename(input_file))[0]
            suggested_name = f"{base_name}_cleaned.txt"
        else:
            suggested_name = "cleaned_transcript.txt"
        
        # Open save dialog
        save_path = filedialog.asksaveasfilename(
            title="Save Cleaned Transcript",
            defaultextension=".txt",
            initialfile=suggested_name,
            filetypes=[
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )

        if save_path:
            try:
                with open(save_path, 'w', encoding='utf-8') as file:
                    file.write(self.cleaned_text)

                # File saved successfully - no popup needed

            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")

    def save_to_original(self):
        """Save the cleaned text back to the original file (overwrite)"""
        if not self.cleaned_text:
            messagebox.showerror("Error", "No cleaned text to save. Please clean a transcript first.")
            return

        input_file = self.input_file_path.get()
        if not input_file:
            messagebox.showerror("Error", "No original file selected.")
            return

        # Confirm overwrite
        result = messagebox.askyesno(
            "Confirm Overwrite",
            f"This will overwrite the original file:\n{input_file}\n\nAre you sure you want to continue?"
        )

        if result:
            try:
                # Create backup first
                backup_path = f"{input_file}.backup"
                with open(input_file, 'r', encoding='utf-8') as original:
                    with open(backup_path, 'w', encoding='utf-8') as backup:
                        backup.write(original.read())

                # Write cleaned text to original file
                with open(input_file, 'w', encoding='utf-8') as file:
                    file.write(self.cleaned_text)

                messagebox.showinfo("Success",
                    f"Original file has been overwritten with cleaned text.\n"
                    f"Backup saved as: {backup_path}")

            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = TranscriptCleaner(root)
    root.mainloop()


if __name__ == "__main__":
    main()
