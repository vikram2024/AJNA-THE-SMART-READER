import pyttsx3
import argparse
import traceback
import sys
from PIL import Image
import pytesseract

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional arguments
parser.add_argument("-t", "--text", help="string input")
parser.add_argument("-a", "--accent", help="indian, australian, us & uk")
parser.add_argument("-g", "--gender", help="male or female")
parser.add_argument("-i", "--index", help="reader index, start from zero.")
parser.add_argument("-o", "--output", help="output audio file name")
parser.add_argument("-f", "--file", help="input image file")

# Read arguments from command line
args = parser.parse_args()

# Default values
text_to_read = "Hi there! I'll read text for you."
gender = "male"
accent = "us"
output_file = "output.mp3"

# if text args passed in cli
if args.text:
    text_to_read = args.text
elif args.file:
    # Read text from the image using Tesseract OCR
    try:
        image = Image.open(args.file)
        text_to_read = pytesseract.image_to_string(image)
    except Exception as e:
        print(f"Error reading text from the image: {e}")
        sys.exit(1)

# if accent args passed in cli
if args.accent:
    accent = args.accent

# if gender args passed in cli
if args.gender:
    gender = args.gender

# if output args passed in cli
if args.output:
    output_file = args.output

# ...

try:
    # ...

    # updating readers accent and gender before reading text.
    update_language(reader, "english", accent, gender)

    # save spoken text to an audio file
    reader.save_to_file(text_to_read, output_file)

    # Execution of saving process
    reader.runAndWait()

    print(f"Audio saved to {output_file}")

    # Finish the saving process
    reader.stop()

except OSError as error:
    traceback.print_exception(*sys.exc_info())
    print("There is a chance that some required system lib is missing, install the lib and try again")

except Exception as error:
    traceback.print_exception(*sys.exc_info())
    print("Something went wrong; please report the issue at https://github.com/vishalnagda1/text-to-speech/issues")
