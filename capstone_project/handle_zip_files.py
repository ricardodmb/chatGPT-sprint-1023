#!/usr/bin/python3
import zipfile
import io
import os


class HandleFiles:
    def __init__(self):
        pass
    
    @staticmethod
    def zip_file_content(zip_file_path: str, file_extension: str) -> dict :
        # Unzip the file
        zip_ref = zipfile.ZipFile(zip_file_path, 'r')
        zip_file_list = zip_ref.namelist()
        
        # Read each file inside the zip
        if len(file_extension.strip()) or file_extension == None:
            raise Exception("File extension needed")

        file_contents = {}
        for file_name in zip_file_list:
            if file_name.endswith(file_extension):
                with zip_ref.open(file_name) as file:
                    content = file.read().decode('utf-8')  # Read the content of the file
                    file_contents[file_name] = content  # Store the content in a dictionary

        # Close the zip file
        zip_ref.close()
        return file_contents
    

    @staticmethod
    def dir_content(file_path: str, file_extension: str) -> dict :
        # Read each file inside the zip
        file_contents = {}
        for file_name in os.listdir(file_path):
            if file_name.endswith(file_extension):
                with open(os.path.join(file_path,file_name)) as file:
                    content = file.read()  # Read the content of the file
                    file_contents[file_name] = content  # Store the content in a dictionary
        return file_contents
    
    @staticmethod
    def file_content(file_path: str, file_extension: str) -> dict :
        if os.path.isdir(file_path):
            file_contents = HandleFiles.dir_content(file_path, file_extension)
            if len(file_contents) > 0:
                return file_contents
            else: 
                raise Exception(f"no files with extension {file_extension} were found")
        elif zipfile.is_zipfile(file_path):
            file_contents = HandleFiles.zip_file_content(file_path, file_extension) 
            if len(file_contents) > 0:
                return file_contents
            else: 
                raise Exception(f"no files with extension {file_extension} were found")
        else:
            raise Exception("Impossible to handle this folder")
