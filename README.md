
# ajna the smart reader



## Requirements

##### System requirements:

- You must have [Python 3](https://www.python.org) installed in your system.
- All commands should be run in [Python 3](https://www.python.org) environment.
- Python:

Make sure you have Python installed on your system. You can download the latest version of Python from the official website: Python Downloads.
Required Libraries:

Install the necessary Python libraries using the following commands:

pip install pyttsx3
Operating System:

The code is designed to work on any operating system (Windows, macOS, Linux).
Hardware:

The code itself is not resource-intensive, so it should work on most modern computers without any specific hardware requirements.
Text Input:

The code takes text input from the user through the console. Ensure that your system has a functional command-line interface or terminal.
Remember to adapt the code or add additional dependencies if you plan to extend its functionality, especially if you're integrating with external APIs or services for more advanced natural language processing or speech recognition features.

For specific requirements related to advanced functionalities or additional libraries, you should refer to the documentation of the libraries or services you plan to integrate into your smart reader application

##### Prerequisite knowledge:

- Basic understanding of [Python](https://www.python.org)
- Basic understanding of **Terminal** or **Command Prompt**
- Python Basics:

Familiarity with basic Python syntax, data types, control structures (if statements, loops), and functions.
Libraries:

Understanding how to install and use external libraries in Python using tools like pip.
Basic knowledge of the libraries used in the code (e.g., pyttsx3) or a willingness to explore their documentation.

Python Official Documentation
pip - The Python Package Installer
pyttsx3 Documentation
Command Line Crash Course
Git - Getting Started

### Getting Started

1. _Install the required python packages_

```sh
pip install pyttsx3
pip install pypiwin32 # Windows only
```

2. _Run the project_

```sh
python main.py
```

#### Command Line Options

1. Install the gTTS library:
```sh
pip install gtts
```


2.Create a Python script (e.g., text_to_speech.py) with the following code:
```sh
from gtts import gTTS
import os

def text_to_speech(text, language='en', filename='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    return filename

if __name__ == "__main__":
    input_text = input("Enter the text you want to convert to speech: ")
    output_file = text_to_speech(input_text)

    print(f"Text-to-speech conversion complete. Saved as {output_file}")


    # Optionally, play the generated audio file
    try:
        os.system(f"start {output_file}")  # Opens the file with the default audio player on Windows
    except:
        pass
```


3.Save the script and run it using python text_to_speech.py. Enter the text when prompted, and the script will generate an audio file (output.mp3 by default).


4. Initialize a Git repository in your project folder:
```sh
git init
```

5. Create a .gitignore file to exclude unnecessary files (e.g., __pycache__, *.pyc, output.mp3, etc.):

6.
```sh
 __pycache__/
*.pyc
output.mp3
```

NOTE : Sometimes there might be chances that the readers are not available for specific gender or language or accent. In that case, it tries to find alternative or else it will read by the default reader which has English language, US accent and voice gender is male.

###Troubleshooting

OSError: libespeak.so.1: cannot open shared object file: No such file or directory. Install libespeak library in your system. If you're using ubuntu you can do it by sudo apt install libespeak1.

aplay: not found your system needs alsa utils library. If you're on ubuntu you can do it by sudo apt-get install alsa-utils.

aplay: main:788: audio open error: No such file or directory or any other aplay related error. Your system should have soundcard on it. You can check this by aplay -l. As a result of this command if you see something like aplay: device_list:270: no soundcards found... this application will not work for you.







