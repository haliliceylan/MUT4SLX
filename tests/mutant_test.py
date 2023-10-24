import json
import subprocess
import os
import sys

current_folder = os.path.dirname(__file__)
parent_folder = os.path.join(current_folder, '../')

def run_mut4slx(model, csv_file):
    # run "../MUT4SLX.py --model $model" as a subprocess
    # check that the output file exists
    r = subprocess.run([sys.executable, "./MUT4SLX.py", "--model", model], cwd=parent_folder)
    assert r.returncode == 0
    # check if $csv_file and ../$csv_file same
    # if not, print the diff
    mutant_file = os.path.join(parent_folder, csv_file)
    mutant_file_expected = os.path.join(current_folder, csv_file)
    with open(mutant_file, "r") as f:
        mutant_file_lines = f.readlines()
    with open(mutant_file_expected, "r") as f:
        mutant_file_expected_lines = f.readlines()
    assert mutant_file_lines == mutant_file_expected_lines

def test_helicopter_model():
    run_mut4slx("Heli", "HelicopterSystem_mutants.csv")

def test_sf_aircraft_model():
    run_mut4slx("sf_aircraft", "sf_aircraft_mutants.csv")

def test_Aircraft_model():
    run_mut4slx("Aircraft", "Aircraft_mutants.csv")

def test_AutotransModel_model():
    run_mut4slx("AutotransModel", "HelicopterSystem_mutants.csv")