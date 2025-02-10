import csv
from hyperon import MeTTa, OperationAtom

def load_csv_to_space(csv_file_path, space_name):
    """Load CSV file to a specified MeTTa space."""
    metta = MeTTa()
    metta.run(f"!(bind! &{space_name} (new-space))")  # Create a new space
    
    def convert_csv_to_nested_format(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)

            def convert_row(row, headers):
                result = f"({row[-1]} "  
                for i, value in enumerate(row[:-1]):
                    result += f" ({headers[i]} {value})"
                result += ")"  
                return result

            return [convert_row(row, headers) for row in reader]

    formatted_output = convert_csv_to_nested_format(csv_file_path)

    for expr in formatted_output:
        print(f"Loading: {expr}")  
        try:
            metta.run(f"!(add-atom &{space_name} {expr})")
        except Exception as e:
            print(f"Failed to load: {expr}\nError: {e}")

    query_result = metta.run(f"!(match &{space_name} ($truth $a $b $c $d) $a)")
    print("Query Results:", query_result)

metta = MeTTa()

load_csv_atom = OperationAtom("load-csv-to-space", load_csv_to_space)

metta.register_atom("load-csv", load_csv_atom)

metta_code = '''
(load-csv "truth.csv" "newspace")
! (match &{space_name} ($truth $a $b $c $d) $a)
'''
result = metta.run(metta_code)
print("Result from MeTTa query:", result)
