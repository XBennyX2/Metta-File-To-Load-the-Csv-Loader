# CSV_LOADER_TO_ATOMSPACE
The Atom Space Loader is a Python-based utility that reads a CSV file,
converts it into a structured MeTTa format, and loads it into a designated Atom Space for further processing.
This allows seamless integration of structured data into a MeTTa reasoning environment.

## Features
Reads CSV files and formats them into MeTTa-compatible expressions.

## PreRequsities
1. "Install Hyperon MeTTa"
   `pip install hyperon`
2. "Install CSV"
   `pip install csv`

## Expected CSV Format
The CSV you are planning to load must be in this format and it can have N number of data meaning its not limited to A B C D only
A,B,C,D,Truthvalue
True,False,True,True,True
False,True,True,True,True

This will be converted into

(True (A True) (B False) (C True) (D True))
(True (A False) (B True) (C True) (D True))

## Testing
!(unify (False (A False) (B True) (C True) (D True) (E True)) ($truth-val ($A $T1)($B $T2)($C $T3)($D $T4)($E $T5)) True False)
the above tests differs when using different formted csv file for the test the csv file contains that type of format and if it is loaded correctly it will return True

## Ensure that the python function is registered using get-type
