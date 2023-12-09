#!/usr/bin/python3
import cProfile
import os
import json
from analyse_files import AnalyseFiles
from handle_zip_files import HandleFiles as hf
import argparse


def main(file_path: str, file_extension: str):
    """
    Main method to send the content of each file, get a json response, and write the converted code and it dependencies.

    Args:
        file_path: Path of the zip file.
        file_extension: Extension of the files wanted to analyse.
    """

    # Next commented lines need to be included in case you want to send args from command line.
        # parser = argparse.ArgumentParser()
        # parser.add_argument("file_path", type=str, help='Path of the folder scripts. It could be a directory or a zip file')
        # parser.add_argument("file_extension", type=str, help='File extension to convert')
        # args = parser.parse_args()
        # file_path = args.file_path
        # file_extension = args.file_extension

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
                
                output_script = f"OUTPUTS/{folder}/{file_name}"
                os.makedirs(os.path.dirname(output_script), exist_ok=True)
                # Open a file for writing
                with open(output_script, 'w') as file:
                    # Write some content to the file
                    file.write(converted_script)
                
                if len(dependencies) >0:
                    output_dep = f"OUTPUTS/{folder}/dependencies_{file_name}"
                    # Open a file for writing
                    with open(output_dep, 'w') as file:
                        # Write some content to the file
                        file.write(dependencies)

if  __name__ == "__main__":
    #  main()

    # Case 1) Python source code inside a zip file
    # we expect an output on OUTPUS/GO  folder
    main('INPUTS/Registration_Form_In_Tkinter_Python_With_Source_Code.zip', '.py')

    # Case 2) GO source code inside a zip file
    # we expect an output on OUTPUS/Python folder
    main('INPUTS/GO.zip', ".go")

    # Case 3) Python source code inside a folder, but extension is .txt
    # we expect an output on OUTPUS/GO  folder
    main('INPUTS/Registration_Form_In_Tkinter_Python_With_Source_Code/Registration_Form_with_GUI', "txt")
    
    # Case 3) Python source code inside a folder, but extension isn't .py
    # we expect an exception raised
    main('INPUTS/Registration_Form_In_Tkinter_Python_With_Source_Code/Registration_Form_with_GUI', ".py")

    