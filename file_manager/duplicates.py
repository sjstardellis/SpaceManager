import hashlib

from file_manager.scanner import scan_folder

def hash_file(file_path, chunk_size=8192):
    # creates hash object
    h = hashlib.sha256()

    # opens the file, reading the bytes
    with open(file_path, "rb") as f:
        # reading the file in chunks
        while chunk := f.read(chunk_size):
            # updating the hash
            h.update(chunk)
    # final hex string
    return h.hexdigest()

def find_duplicates(files):
    # list of file paths with that hash
    # key: hash, value: list of file paths
    hash_map = {}

    # looping through every file
    for file in files:

        # file path string from hash_map
        path = file["path"]

        # calculate the hash of the file content
        file_hash = hash_file(path)

        # if the hash is not yet in the dictionary, add it with an empty list
        if file_hash not in hash_map:
            # add to hashmap
            hash_map[file_hash] = []
        # add the path to list of paths of the current key
        hash_map[file_hash].append(path)

    # keeping only those hashes with more than one file (duplicates)
    duplicates = {h: paths for h, paths in hash_map.items() if len(paths) > 1}

    # returns the duplicates
    return duplicates