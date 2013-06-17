import time
import ImageGrab

class ScreenShot(object):
    
    def __init__(self, resize=(800,600), path="", file_type="png"):
        self.resize = resize
        self.file_type = ''.join([".", file_type])
        self.path = path
    
    def grab(self):
        t = str(time.time()).replace('.','-')
        tt = time.time()
        img=ImageGrab.grab()
        img = img.resize(self.resize)
        save_path = ''.join([self.path,'\\'])
        img.save(''.join([save_path, t, self.file_type]))


if __name__ == "__main__":
    screen = ScreenShot()
    while True:
        time.sleep(0.5)
        screen.grab()
