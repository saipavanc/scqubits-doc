import os
import json
import sys


import scqubits.core.diag as diag
from inspect import getmembers, isfunction

# from somemodule import foo
method_names = [i[0] for i in getmembers(diag, isfunction) if i[0][0] !="_"]
replace_str = lambda x: '{:obj}`' + "~scqubits.core.diag." + x + '`'

for method_name in method_names:
    print(replace_str(method_name))

def replace_strs_in_line(line, method_names):
    for method_name in method_names:
        line = line.replace(method_name, replace_str(method_name))
    return line

############# if you want to run this script from the command line, you can use the following code #############
# original_str = sys.argv[1]
# replacement_str = sys.argv[2]
# print(f'original_str: {original_str}')
# print(f'replacement_str: {replacement_str}')
#########################################

# # # Define the path to search and the replacement string
project_directory = '.'  # Change this to your project path if needed

# Function to replace instances of Transmon with the replacement string in .ipynb files
file_updated = False
for root, dirs, files in os.walk(project_directory):
    if "api-doc" in dirs:
        dirs.remove("api-doc")
    for file in files:
        if file.endswith('.ipynb'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                notebook = json.load(f)
            
            # Iterate through cells and replace 'Transmon' in source
            for cell in notebook['cells']:
                if cell['cell_type'] == 'markdown':
                    cell['source'] = [replace_strs_in_line(line, method_names) for line in cell['source']]
            
            # Write the updated content back to the file
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, indent=1)
            
            print(f'Updated file: {filepath}')