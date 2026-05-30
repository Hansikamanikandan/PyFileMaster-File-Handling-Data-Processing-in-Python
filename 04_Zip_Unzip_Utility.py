import zipfile
import os

def zip_folder(folder_name, zip_name):
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_name):
            for file in files:
                filepath = os.path.join(root, file)
                zipf.write(filepath)

def unzip_folder(zip_name, extract_path):
    with zipfile.ZipFile(zip_name, "r") as zipf:
        zipf.extractall(extract_path)

folder = input("Enter folder name to zip: ")
zip_file = input("Enter zip file name: ")

zip_folder(folder, zip_file)
print("Folder zipped successfully")

extract_path = input("Enter extraction folder: ")

unzip_folder(zip_file, extract_path)
print("Folder unzipped successfully")
