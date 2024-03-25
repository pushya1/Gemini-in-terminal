
# Gemini-in-terminal

This repository contains a Python file and a Bash script that allow you to use Google's "Gemini" via its free API directly in your terminal.

### Instructions:

1. **Download the Files:**
   - Download `gemini.py` and `gemini.sh` from this repository and place them in a folder in your home directory.

2. **Edit `gemini.py`:**
   - Open `gemini.py` in a text editor and add your Google API key where specified.

3. **Edit `gemini.sh`:**
   - Open `gemini.sh` in a text editor and update the `ABSOLUTE_PATH_TO_GEMINI_PY` variable with the absolute path to your `gemini.py` file.

4. **Set Execute Permissions:**
   - Open a terminal and navigate to the folder where you placed `gemini.py` and `gemini.sh`.
   - Run the following commands to give execute permissions:
     ```bash
     chmod +x gemini.sh
     chmod +x gemini.py
     ```

5. **Create a Symbolic Link:**
   - To make the script accessible as a global command, create a symbolic link to the Bash script:
     ```bash
     sudo ln -s /path/to/gemini.sh /usr/local/bin/gemini
     ```
     Replace `/path/to/gemini.sh` with the absolute path to your `gemini.sh` file.

6. **Usage:**
   - Now you can use the `gemini` command in your terminal to access Gemini via the terminal.
   - Enter `gemini` to start the program.
   - When inside the program, enter `exit` as input to exit.



