import os
import time
import ImageGrab

class ScreenShot(object):
    """
    Object representing the current screen
    """
    def __init__(self, resize=(800,450), file_type="png"):
        self.resize = resize
        self.file_type = ''.join([".", file_type])
    
    def grab(self):
        t = str(time.time()).replace('.','-')
        tt = time.time()
        img=ImageGrab.grab()
        img = img.resize(self.resize)
        img.save(''.join([t, self.file_type]))

def get_time(st):
    """
    Converts file name to timestamp for images
    taken using ScreenShot() class instances
    """
    st = st.split('.')[0]
    return float(st.replace('-','.'))

def get_times():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and "png" in f]
    
    t_files, times = [], []
    for f in files:
        try:
            t = get_time(f)
            times.append(t)
            t_files.append(f)
        except:
            pass
    return zip(times, t_files)
    
if __name__ == "__main__":
    print get_times()
