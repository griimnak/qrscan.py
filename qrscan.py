""" qrscan.py
    A simple python script for extracting data from QR images.

    requirements:
    pip install Pillow, pyzbar

    usage: qrscan.py -i [path/to/image] --pretty --cleanup
"""
import getopt
import os
import sys

try:
    from pyzbar.pyzbar import decode
    from PIL import Image
except ImportError as import_error:
    print("(%s)" % import_error)
    exit("Modules are missing. Run this: pip install -r requirements.txt")

def splash_text():
        print('''
 ▄▄▄▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄▄▄
 █ ▄▄▄ █  █▄▀  █ ▄▄▄ █
 █ ███ █  ▀█▀▄ █ ███ █
 █▄▄▄▄▄█ ▄ ▄▀█ █▄▄▄▄▄█     qrscan.py
 ▄▄ ▄▄ ▄ ▀██▀█ ▄     ▄     A simple python script for extracting data from QR images.
 █▄█▄▀ ▄▄▀   ▀▄█ █▄▀█▄
 ▀  ▀█▄▄███▄▀  ▄   ▀█▄
 ▄▄▄▄▄▄▄ ▀▀▀▀█▄▄▄▄▄▀       requirements:
 █ ▄▄▄ █ ▄▀▀██▀▄ ▄█▀▄▄     pip install Pillow, pyzbar
 █ ███ █ ▀██▀▀ ▄ ▄▀▀▄▄
 █▄▄▄▄▄█ ██▀▄ ▀▀█▄▀▀▀▀
            ''')
        print("\nusage: qrscan.py -i [full image path]")
        print("\npositional arguments:")
        print("  -i, --image        full image path to scan. Example: C:\\Users\\griimnak\\Desktop\\qr_code.png")
        print("\noptional arguments:")
        print("  --2fa              prints the extracted 16 digit 2fa code in human readable form.")
        print("  --cleanup          deletes the QR image when complete.")

def qrscan(argv):
    """ qrscan.py """
    try:
        opts, args = getopt.getopt(argv, "i:", ["image=", "2fa", "cleanup"])

    except getopt.GetoptError:
        print("usage: qrscan.py -i C:\\Users\\griimnak\\Desktop\\qr_image.png")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-i", "--image"):
            if arg == "":
                # Exit if -i has no argument
                exit("Invalid image path.")
            # else set image path and continue ..
            img_path = arg
            try:
                raw_decode = decode(Image.open(arg))
                print(raw_decode)
            except FileNotFoundError as file_error:
                # Die if FileNotFoundError is raised
                exit(str(file_error))

        elif opt in "--2fa":
            _pretty = str(raw_decode[0][0]).split("?secret=", 1)[1].split("&", 1)[0]
            print('\n\n2FA Code:\n'+' '.join(_pretty[i:i + 4] for i in range(0, len(_pretty), 4)))

        elif opt in "--cleanup":
            try:
                os.remove(img_path)
                print("\nQR image was deleted upon --cleanup request.")
            except FileNotFoundError as file_error:
                exit(str(file_error))

    if argv == []:
        splash_text()

qrscan(sys.argv[1:])
