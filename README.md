# PIC (Pointmap Image Converter)

### What is this?
PIC takes an image as input and generates a pointcloud that can be used as a map for RP-SLAM.

### Installation
This uses Python 3.

Simply run `pip install -r requirements.txt` and then run it using `python run.py`.
The script will read from a file by default named `map.png` and will output to `map.txt`.

If you want to look at a visual representation of the pointmap, run `python run.py -visual`. You can close the window by
clicking anywhere on it.
