#!/usr/bin/python3
import cProfile
import os
import json
from analyse_files import AnalyseFiles
from handle_zip_files import HandleFiles as hf
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=str, help='Path of the folder scripts. It could be a directory or a zip file')
    parser.add_argument("file_extension", type=str, help='File extension to convert')
    args = parser.parse_args()
    file_path = args.file_path
    file_extension = args.file_extension

    af = AnalyseFiles
    files = hf.file_content(file_path, file_extension)

    for name, content in files.items(): 
                response = af.analyze_source_file(content)                
                json_response = json.loads(response)                
                converted_script = json_response['code']
                file_name = json_response['suggested_script_name']
                dependecies_list = json_response['dependencies_list_from_converted_converted']
                folder = json_response['converted_programming_language']
                dependencies = ' '
                if 'No dependencies' not in dependecies_list:
                    dependencies = ' '.join([str(elem)+'\n' for elem in dependecies_list])
                
                # Open a file for writing
                with open(f"OUTPUTS/{folder}/{file_name}", 'w') as file:
                    # Write some content to the file
                    file.write(converted_script)
                
                if dependencies is None:
                    # Open a file for writing
                    with open(f"OUTPUTS/{folder}/dependencies_{file_name}", 'w') as file:
                        # Write some content to the file
                        file.write(dependencies)

if  __name__ == "__main__":
     main()
    # main('INPUTS/Registration_Form_In_Tkinter_Python_With_Source_Code/Registration Form with GUI', ".py")
    # main('../files/Registration_Form_In_Tkinter_Python_With_Source_Code.zip', ".py")
    # main('../filesGO.zip', ".go")
