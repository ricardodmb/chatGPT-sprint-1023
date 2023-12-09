#!/usr/bin/python3
import zipfile
import io
import os


class HandleFiles:
    """
    This class represents how it interacts with the path and the files it contains.
    """
    def __init__(self):
        pass
    
    @staticmethod
    def zip_file_content(zip_file_path: str, file_extension: str) -> dict :
        """
        This method will be used to open a zip file and read each of the files contained there if they have the extension indicated.

        Args:
            zip_file_path: Path of the zip file.
            file_extension: Extension of the files wanted to analyse.

        Returns:
            dict: {File name: File content}
        """
        # Unzip the file
        zip_ref = zipfile.ZipFile(zip_file_path, 'r')
        zip_file_list = zip_ref.namelist()
        
        # Read each file inside the zip
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
        """
        This method will be used to open files inside a folder and read each of the files contained there if they have the extension indicated.

        Args:
            file_path: Path of the zip file.
            file_extension: Extension of the files wanted to analyse.

        Returns:
            dict: {File name: File content}
        """
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
        """
        This method will choose wich of the previous methos are needed.

        Args:
            file_path: Path of the zip file.
            file_extension: Extension of the files wanted to analyse.

        Raises:
            Exception: If file_extension is not indicated or empty.
            Exception: If no files with extension file_extension were found.
            Exception: If no files with extension file_extension were found.
            Exception: If isn't a folder path or a zip file.

        Returns:
            _description_
        """
        if len(file_extension.strip()) == 0 or file_extension == None:
            raise Exception("File extension needed")
        else:
            pass

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
