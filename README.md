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

- `MUT4SLX.py`: This is the main script for performing mutant generation and provides a command-line interface for the tool.
- `model_files.json`: This configuration file specifies the models and their details required to run the MUT4SLX tool.
- `matlab_workspace/`: This directory contains all MATLAB models and related files.
- `HelicopterSystem.html`: This is a detailed report on the execution of the Helicopter System mutants. Please note that the code used to generate this report is not open-sourced yet. [Open Report In Browser](https://rawcdn.githack.com/haliliceylan/MUT4SLX/4d3d570a058c539d058ae933ef03fac2bd6cdd7b/HelicopterSystem.html)
- `HelicopterSystem_mutants.csv`: This CSV file contains information about all the possible mutants generated for the Helicopter System.
- `LICENSE`: This file contains the license information for the repository.
- `MutationClasses.py`: This file contains the implementation of all mutant operators used by the tool.
- `README.md`: This file, which you are currently reading, provides detailed information about the repository.
- `Replication-Package.md`: This file contains information about the replication package for the project.
- `config_reader.py`: This file includes the implementation of the configuration reader class.
- `.gitignore`: This file specifies the files and directories that should be ignored by the Git version control system.

Other supporting files and directories may be present as well.

## Example Use Cases

### Example use case with Helicopter Control System
(https://github.com/wfpotter/DO178_Case_Study)
### Example use case with Aircraft Elevator Control System
(https://gitlab.com/DrishtiYadav/fimtool/-/tree/main/Aircraft_fault_injector/sf_aircraft_model)
### Example use case with Automatic Transmission Controller System
(https://gitlab.com/DrishtiYadav/fimtool/-/tree/main/Autotrans_fault_injector/cav_benchmark)
