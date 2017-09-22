
import os

import MaxPlus

import libFunc
import libFileFolder

def open_scene_folder():
    libFileFolder.open_folder(MaxPlus.Core.EvalMAXScript("sceneName = maxFilePath + maxFileName").Get())

def open_project_folder():
    libFileFolder.open_folder(os.getenv("PROJECT_PATH"))

def save():
    import arSave
    reload(arSave)
    arSave.start()

def load():
    import arLoad
    reload(arLoad)
    arLoad.start()

def get_report():
    libFunc.get_help('issues')

def get_help():
    libFunc.get_help()
