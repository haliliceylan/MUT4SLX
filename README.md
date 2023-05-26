# MUT4SLX

MUT4SLX tool focuses on performing mutation testing on a model implemented in MATLAB/Simulink. It applies various mutation operators to the model and generates Simulink model mutants.


## Description

The Simulink Model Mutation Testing project provides a framework for generating mutants, and CSV file as an output. It utilizes the MATLAB environment to load the model, apply mutations, and collect outputs.

# DEMO
[![DEMO](http://img.youtube.com/vi/inud_NRGutc/0.jpg)](http://www.youtube.com/watch?v=inud_NRGutc)

## Features

- Mutant generation: Apply a set of predefined mutation operators to the Simulink model.
- CVS output generation: Generate an CSV output summarizing the mutations.

## Getting Started

```
usage: MUT4SLX.py [-h] --model MODEL [--matlab-gui]

Simulink model mutation tool.

optional arguments:
  -h, --help     show this help message and exit
  --model MODEL  Name of the Simulink model in config file.
  --matlab-gui   Show the MATLAB GUI.
```

### Prerequisites

- MATLAB [version R2021b](https://nl.mathworks.com/products/matlab.html)
- Python [version 3.7.8](https://www.python.org/downloads/)
- Libraries: [matlab.engine](https://www.mathworks.com/help/matlab/matlab-engine-for-python.html)

### Installation

1. Clone the repository: `git clone https://github.com/haliliceylan/MUT4SLX.git`
2. Install the required libraries: `pip install -r requirements.txt`

### Usage

1. Modify the `model_files.json` file to specify the models and their configurations.
2. Run the main script: `python MUT4SLX.py --model MODEL`
3. View the generated CSV output: `open <model_name>.CSV`

## File Structure

- `MUT4SLX.py`: Main script for performing mutant generation.
- `model_files.json`: Configuration file specifying the models and their details.
- Other supporting files and directories.

## Example Use Cases

### Example use case with Helicopter Control System
(https://github.com/wfpotter/DO178_Case_Study)
### Example use case with Aircraft Elevator Control System
(https://gitlab.com/DrishtiYadav/fimtool/-/tree/main/Aircraft_fault_injector/sf_aircraft_model)
### Example use case with Automatic Transmission Controller System
(https://gitlab.com/DrishtiYadav/fimtool/-/tree/main/Autotrans_fault_injector/cav_benchmark)
