# qrscan.py

#### Requirements
- Python3+
```cmd
pip install Pillow pyzbar
```

#### Usage
```cmd
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


usage: qrscan.py -i [full image path]

positional arguments:
  -i, --image        full image path to scan. Example: C:\Users\griimnak\Desktop\qr_code.png

optional arguments:
  --2fa              prints the extracted 16 digit 2fa code in human readable form.
  --cleanup          deletes the QR image when complete.
```
