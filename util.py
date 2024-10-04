import os, sys
def pyinstaller_compatible_path(path:str):
    try:
        return os.path.join(sys._MEIPASS, path)
    except AttributeError:
        return path