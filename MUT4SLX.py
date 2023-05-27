import csv
import io
import json
import argparse
import matlab.engine
from time import perf_counter, sleep
from MutationClasses import (
    MutationApplier
)
from config_reader import get_available_mutant_operators
import logging
import re
import io
out = io.StringIO()
err = io.StringIO()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

                
# Create an argument parser
parser = argparse.ArgumentParser(description='Simulink model mutation tool.')

# Add the --model parameter to specify the model name
parser.add_argument('--model', type=str, help='Name of the Simulink model in config file.', required=True)

# Add the --matlab-gui parameter to specify whether to show the MATLAB GUI
parser.add_argument('--matlab-gui', action='store_true', help='Show the MATLAB GUI.')


# Parse the command line arguments
args = parser.parse_args()

# Access the value of the --model parameter
model_name = args.model

# Access the value of the --matlab-gui parameter
matlab_gui = args.matlab_gui

# Use the model_name variable in your code to mutate the Simulink model
logging.info(f"Mutating Simulink model: {model_name}")

logging.info("Launching/Attaching MATLAB engine...")
eng = matlab.engine.connect_matlab()
logging.info("Succesfully connected with MATLAB engine.")

if matlab_gui:
    logging.info("Enabling MATLAB GUI...")
    eng.desktop(nargout=0)
    logging.info("MATLAB GUI enabled.")
    

logging.info("Loading model file configurations...")
with open("model_files.json", "r") as f:
    model_files = json.load(f)
logging.info("Model file configurations loaded.")


current_model_config = model_files[model_name]

logging.info(f"Changing MATLAB working directory to {current_model_config['cd']}...")
eng.cd(current_model_config["cd"], nargout=0)
logging.info("MATLAB working directory changed.")

logging.info(f"Loading mutation operators from configuration file...")
avaliable_mutant_operators, short_list = get_available_mutant_operators(model_files)
logging.info(f"Enabled mutation operators: {', '.join(short_list)}")

if "project" in current_model_config:
    eng.openProject(current_model_config["project"])


logging.info(f"Loading Model...")
eng.close_system(current_model_config["model"], 0.0, nargout=0)
eng.load_system(current_model_config["model"])
logging.info(f"Loaded model '{current_model_config['model']}'")


def findAllSubModels(start_model_name):
    all_systems = [start_model_name]
    all_systems_x = {start_model_name: 1}
    for model in all_systems:
        for x in eng.find_system(model, 'BlockType', 'ModelReference'):
            model_name = eng.get_param(x, 'ModelName')
            if model_name not in all_systems:
                all_systems.append(model_name)
                all_systems_x[model_name] = 1
                eng.close_system(model_name, 0.0, nargout=0)
                eng.load_system(model_name)
                logging.info(f"{model_name} is loaded")
            else:
                all_systems_x[model_name] += 1
    return all_systems_x


def getTotalBlockCount(model_name):
    return len(eng.find_system(model_name))

logging.info(f"Finding all submodels...")
all_systems = findAllSubModels(current_model_config["model"])
all_systems_keys = list(all_systems.keys())

total_block_count = 0
for x in all_systems:
    block_count = getTotalBlockCount(x)
    multiplied_count = block_count * all_systems[x]
    total_block_count += multiplied_count
    #logging.info(f"{x}: Block Count - {block_count}, Multiplied Count - {multiplied_count}")

logging.info(f"Total Block Count: {total_block_count}")
logging.info(f"Found all submodels.")


dict_data = []

def add_new_block_to_dict(mutation, mutator, BlockPath):
    global dict_data
    data = {
            "ModelName": current_model_config["model"],
            "SubSystem": BlockPath.rsplit("/", 1)[0],
            "BlockName": BlockPath.rsplit("/", 1)[1],
            "BlockType": mutator.block_type,
            "MutationClass": mutator.__class__.__name__,
            "Parameter": mutator.param_name,
            "OriginalValue": mutator.original_function,
            "MutationValue": mutation[1],
            "FullPath":BlockPath
        }
    dict_data.append(data)

def csv_generator():
    global dict_data
    csv_columns = ['ModelName','SubSystem','BlockName','BlockType','MutationClass','Parameter','OriginalValue','MutationValue','FullPath']
    with open('{}_mutants.csv'.format(current_model_config["model"]), 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
        
logging.info("Mutant Generating is starting...")
for mutator_class in avaliable_mutant_operators:
    for system in all_systems_keys:
        eng.load_system(system)
        blockType = mutator_class.block_type
        blocks = eng.find_system(system,'BlockType',blockType)
        for block in blocks:
            mutator = mutator_class()
            if not mutator.load(block, eng):
                continue
            for mutation in mutator:
                add_new_block_to_dict(mutation, mutator, block)
logging.info("Mutant Generating is finished.")

logging.info(f"Mutant Count: {len(dict_data)}")
logging.info("CSV Generating is starting...")
csv_generator()
logging.info("CSV Generating is finished.")
logging.info(f"{current_model_config['model']}_mutants.csv")