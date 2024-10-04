import os


class Settings:
    def __init__(self, namespace='minecraft',
                 lang='eng.json',
                 datapack='datapack',
                 resourcepack='resourcepack'):
        self.namespace = namespace
        self.lang = lang
        self.datapack = os.path.normpath(datapack)
        self.resourcepack = os.path.normpath(resourcepack)

    def __repr__(self):
        return (
            f"Settings(namespace={self.namespace}, lang={self.lang}, "
            f"datapack={self.datapack}, resourcepack={self.resourcepack})")
