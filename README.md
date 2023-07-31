# MUT4SLX

MUT4SLX tool focuses on performing mutation testing on a model implemented in MATLAB/Simulink. It applies various mutation operators to the model and generates Simulink model mutants.


## Description

The Simulink Model Mutation Testing project provides a framework for generating mutants, and CSV file as an output. It utilizes the MATLAB environment to load the model, apply mutations, and collect outputs.

# DEMO
[![DEMO](http://img.youtube.com/vi/inud_NRGutc/0.jpg)](http://www.youtube.com/watch?v=inud_NRGutc)

## Features

- Mutant generation: Apply a set of predefined mutation operators to the Simulink model.
- CVS output generation: Generate an CSV output summarizing the mutations.
- HTML Report: Please note that the code used to generate this report is not open-sourced yet. [Open Report In Browser](https://rawcdn.githack.com/haliliceylan/MUT4SLX/4d3d570a058c539d058ae933ef03fac2bd6cdd7b/HelicopterSystem.html)

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
- Python [version 3.9.16](https://www.python.org/downloads/)
- Libraries: [matlab.engine](https://www.mathworks.com/help/matlab/matlab-engine-for-python.html)

### Installation

1. Clone the repository: `git clone https://github.com/haliliceylan/MUT4SLX.git`

### Usage

1. Modify the `model_files.json` file to specify the models and their configurations.
2. Run the main script: `python MUT4SLX.py --model MODEL`
3. View the generated CSV output: `open <model_name>.CSV`


## Configuration File

The configuration file specifies various settings and parameters for using the MUT4SLX tool. It includes a list of mutant operators and configurations for different Simulink models. Let's break down each part of the configuration file:

### Mutant Operators
The `mutant_operators` section lists the available mutant operators. These operators are abbreviated with short names for convenience. Here are the mutant operators included in the configuration file:

- `ROR`: Relational Operator Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/relationaloperator.html) to the definition of the relational operators in Matlab/Simulink.
The ROR operator changes the current value of the block with other different operators, such as changing "==" with "~=, <, <=, >=, >" operators.
- `LOR`: Logical Operator Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/logicaloperator.html) to the definition of the logical operators in Matlab/Simulink.
The LOR operator changes the block's current value with other different operators, such as changing "AND" with "OR, NAND, NOR, XOR" operators.
- `ASR`: Arithmetic Sign Replacement

- `MMR`: Min-Max Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/minmax.html) to the definition of the logical operators in Matlab/Simulink.
The MMR operator changes the block's current value with other operators, such as changing "MIN" with "MAX" operators.
- `ICR`: If Condition Replacement
- `TOR`: Trigonometric Operator Replacement
- `MOR`: Math Operator Replacement
- `PMR`: Product Multiplication Replacement
- `POR`: Product Operator Replacement
- `FIR`: For Index Replacement
- `FLR`: For Limit Replacement
- `UDO`: Unit Delay Operation
- `SCR`: Switch Criteria Replacement
- `STR`: Switch Threshold Replacement
- `CR` : Constant Replacement

```json
{
  "mutant_operators": [
    "ROR",
    "LOR",
    "ASR",
    "MMR",
    "ICR",
    "TOR",
    "MOR",
    "PMR",
    "POR",
    "FIR",
    "FLR",
    "UDO",
    "SCR",
    "STR",
    "CR"
  ],
```

These operators are used during the mutation process to generate modified versions of the Simulink models for testing.

### Model Configurations
The configuration file provides settings for different Simulink models. Each model has a unique key, which is used as a reference for specifying the model when running the mutation testing tool. Here are the model configurations included in the file:

The "Heli" section represents a specific configuration for the "Helicopter Control System" Simulink model. The attributes within this section are:

```json
  "Heli": {
    "model": "HelicopterSystem",
    "cd": "matlab_workspace/heli",
    "project": "heli.prj",
    "system": "HelicopterSystem",
    "test": "HeliLoopTest"
  },
```
- `model`: Specifies the main Simulink model to start the mutation process, in this case, "HelicopterSystem."
- `cd`: Indicates the relative path of the project directory where the Simulink model is located. It is generally found under the "matlab_workspace" directory with the "heli" subdirectory.
- `project`: If the Simulink model depends on a MATLAB project, you can specify the project file using this attribute. In this case, it is "heli.prj."
- `system`: Specifies the system name of the main model. It can also accept a full path, allowing the mutation process to start from that path and explore its sub-paths.
- `test`: Currently, this attribute is not usable in the current version. However, you can refer to the demo for the full behavior. It represents the test file name for this Simulink model.

Similarly, the configuration sections for other Simulink models like "sf_aircraft," "Aircraft," and "AutotransModel" follow a similar structure, specifying their respective models, directories, systems, and test files if applicable.

**Please note that the actual values used in the configuration file, such as model names and paths, are examples provided for demonstration purposes. You should replace them with the appropriate values based on your specific Simulink projects and file structures.**

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
