







class Context():
    def __init__(self):
        self.project    = project          # arpipeline

        self.path       = path             # D:/project/asset/file.format

        self.step       = step             # shot or asset
        self.task       = task             # ANIMATION

        self.resolution = resolution       # [1920, 1080]
        self.fps        = fps              # 25

        self.author     = author           # arichter
        self.comment    = comment          # "Broken scene"


    #*******************
    # VARIABLE
    @property
    def project(self):
        return self.project


    #*******************
    # FUNCTIONS
    def open_path(self):
        return libFileFolder.openFolder(self.file_path)
