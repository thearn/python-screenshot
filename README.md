python-screenshot
=======================
Python library to make screen captures and save the images to the current working directory.

Installing:
===========
- Download the source, and run `python setup.py build install`

Examples:
==========

- Importing the library:

```python
from screenshot import ScreenShot

screen = ScreenShot()
```
- Output image size defaults to 800x450. A custom size can be set when the ScreenShot object is instantiated:

```python
screen = ScreenShot((640, 480))
```
- Taking a screenshot: this saves the screenshot to the current working directory as a .png file

```python
screen.grab()
```
The system time at the moment the screenshot was taken is used as the filename


- Taking two screenshots, 1 second apart:

```python
import time
screen.grab()
time.sleep(1)
screen.grab()
```

- To check for all screenshot files in the current working directory, and get the file names as well as
corresponding system times:

```python
from screenshot import get_times

print get_times()
```

This will return a list of (system time, filename) tuples.
