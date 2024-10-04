import os


class Item:
    def __init__(self, file_path, **data):
        file_name = os.path.basename(file_path)
        parent_dir = os.path.basename(os.path.dirname(file_path))

        # Extract the ID (filename without extension)
        self.id = os.path.splitext(file_name)[0]

        # Determine the type (parent directory) if it isn't the root directory
        self.type = parent_dir if parent_dir != 'items' else None

        # Dynamically set attributes from the passed keyword arguments
        for key, value in data.items():
            setattr(self, key, value)

    def __repr__(self):
        return (
            f"Settings(id={self.id}, type={self.type})")
