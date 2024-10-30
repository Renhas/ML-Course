import kagglehub
import shutil

def download(dataset_name, file_name=None):
    path_to_file = kagglehub.dataset_download(dataset_name, path=file_name)
    return shutil.move(path_to_file, "./")
