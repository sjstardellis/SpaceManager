from pathlib import Path
from datetime import datetime

def scan_folder(folder_path):
    # folder to be the path of the folder
    folder = Path(folder_path)

    # if it doesn't exist, throw error
    if not folder.exists() or not folder.is_dir():
        raise ValueError("Invalid folder path")

    # array of objects to represent our files in this folder
    files = []

    # looping through all the files
    for file in folder.rglob("*"):
        # if the file is a file
        if file.is_file():
            # returns metadata for the current file
            stat = file.stat()
            # append every statistic together
            files.append({
                "name": file.name,
                "extension": file.suffix,
                "path": str(file),
                "size_bytes": stat.st_size,
                "size_kb": round(stat.st_size / 1024, 2),
                "last_modified": datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                "last_modified_ts": stat.st_mtime
            })
    # return all files in the folder with their statistics
    return files