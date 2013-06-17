
python-screenshot
=======================
Python library to make screen captures and save the images to the current working directory.

Usage:
==========

- Importing the library:

```python
from screenshot import ScreenShot

screen = ScreenShot()
```

- To take two screenshots, 1 second apart:

```python
import time
screen.grab()
time.sleep(1)
screen.grab()
```

This will save the two screenshots, using the system time as the filename

- To check for all screenshot files in the current working directory, and get the file names as well as
corresponding system times:

```python
from screenshot import get_times

print get_times()
```

This will return a list of (system time, filename) tuples.