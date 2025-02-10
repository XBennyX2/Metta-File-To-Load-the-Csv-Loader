import csv
from hyperon import *
from hyperon.ext import register_atoms
import random
import string
import time
from hyperon.atoms import OperationAtom, V
from hyperon.ext import register_atoms
import itertools
from itertools import combinations
import csv
from hyperon import MeTTa, OperationAtom

def load_csv_data_to_newspace(metta, csv_file_path):

    # # Create a MeTTa instance
    # metta = MeTTa()

    # # Bind a new space with the given name
    # metta.run(f"!(bind! &{space_name} (new-space))")
    filename = str(csv_file_path)
    arr = []
    # Open and read the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        
        # Process each row in the CSV file
        for row in reader:
            # Start with the TruthValue (last column)
            expr = f"({row[-1]} "  
            # Add each header-value pair as a sub-expression
            for i, value in enumerate(row[:-1]):
                expr += f" ({headers[i]} {value})"
            expr += ")"  # Close the expression
            arr.append(expr)
    b = "("   
    for a in arr:
        b += a
    b += ")"
    # print(b)
    return metta.parse_all(b)
           
    #         try:
    #             # Load the expression into the new space
    #             metta.run(f"!(add-atom &{space_name} {expr})")
    #         except Exception as e:
    #             print(f"Failed to load: {expr}\nError: {e}")
    
    # return metta


@register_atoms(pass_metta=True)
def cnj_exp(metta):
    loadCsv = OperationAtom('load_csv', lambda var1: load_csv_data_to_newspace(metta, var1), 
                                 ['Atom', 'Expression'],unwrap=False)
    return {
        r"load_csv": loadCsv
    }


# #Checking The Function
# metta_instance = load_csv_data_to_newspace("truth.csv", "myNewSpace")

# result = metta_instance.run("!(match &myNewSpace ($tv $a $b $c $d) ($tv $a $b $c $d))")
# print("Query Results:", result)

