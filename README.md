# MUT4SLX
The MUT4SLX tool focuses on performing mutation testing on a model implemented in MATLAB/Simulink. It applies various mutation operators to the model and generates Simulink model mutants.


## Description

The MUT4SLX tool provides a structured framework for systematically generating mutants and producing corresponding output files in CSV format. It leverages the MATLAB environment to load Simulink models, apply predefined mutation operators, and record the resulting outputs.

# DEMO
[![DEMO](http://img.youtube.com/vi/inud_NRGutc/0.jpg)](http://www.youtube.com/watch?v=inud_NRGutc)

## Features

- Mutant generation: Apply a set of predefined mutation operators to the Simulink model.
- CVS output generation: Generate an CSV output summarizing the mutations.
- HTML Report: Please note that the code used to generate this report is not open-sourced yet. [Open Report In Browser](https://rawcdn.githack.com/haliliceylan/MUT4SLX/4d3d570a058c539d058ae933ef03fac2bd6cdd7b/HelicopterSystem.html)

## Licensing Information

This repository contains code and assets under different licenses:
Make sure to review the specific license for each part of the code. Additionally, check out the example use cases with different licenses:

- [Helicopter Control System (BSD 3-Clause "New" or "Revised" License)](https://github.com/wfpotter/DO178_Case_Study/blob/master/license.txt) 
- [Aircraft Elevator Control System (MIT License)](https://gitlab.com/DrishtiYadav/fimtool/-/blob/main/LICENSE)
- [Automatic Transmission Controller System (MIT License)](https://gitlab.com/DrishtiYadav/fimtool/-/blob/main/LICENSE)

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

### Mutant Operators For Simulink
The `mutant_operators` section lists the available mutant operators. These operators are abbreviated with short names for convenience. Here are the mutant operators included in the configuration file:

- `ROR`: Relational Operator Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/relationaloperator.html) to the definition of the relational operators in Matlab/Simulink.
The ROR operator changes the current value of the block with other different operators, such as changing "==" with "~=, <, <=, >=, >" operators.
- `LOR`: Logical Operator Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/logicaloperator.html) to the definition of the logical operators in Matlab/Simulink.
The LOR operator changes the block's current value with other different operators, such as changing "AND" with "OR, NAND, NOR, XOR" operators.
- `ASR`: Arithmetic Sign Replacement
Please refer (https://nl.mathworks.com/help/matlab/relational-operators.html) to the definition of the relational operators in Matlab/Simulink.
The ASR operator changes the block's current value with other different operators, such as changing "==" with "~=, <, <=, >=, >" operators.
- `MMR`: Min-Max Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/minmax.html) to the definition of the logical operators in Matlab/Simulink.
The MMR operator changes the block's current value with other operators, such as changing "MIN" with "MAX" operators.
- `ICR`: If Condition Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/if.html) to the definition of the If condition operators in Matlab/Simulink.
The ICR operator changes the block's current value with other operators, such as changing an if condition with "1 == 1 (true), 1 == 0 (false)" conditions.
- `TOR`: Trigonometric Operator Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/trigonometricfunction.html) to the definition of the trigonometric operators in Matlab/Simulink.
The TOR operator changes the block's current value with other operators, such as changing "sin" operator with "cos, tan, asin, acos , atan, sinh, 
 cosh, tanh, asinh, acosh, atanh, cos + jsin" operators.
- `MOR`: Math Operator Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/mathfunction.html) to the definition of the Math operators in Matlab/Simulink.
The MOR operator changes the block's current value with other operators, such as changing "exp" operator with "log, 10^u, log10, magnitude^2, square, conj, reciprocal, transpose, hermitian" operators.
- `PMR`: Product Multiplication Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/product.html) to the definition of the product multiplication types in Matlab/Simulink.
The PMR operator changes the block's current value with other operators, such as changing "Element-wise(.*)" type with "Matrix(*)" type.
- `POR`: Product Operator Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/product.html) to the definition of the product block in Matlab/Simulink.
The POR operator changes the block's current value with other operators, such as changing "2" input types with "* /, / *, //" types.
- `FIR`: For Index Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/foriterator.html) to the definition of the For iterator block in Matlab/Simulink.
The FIR operator changes the block's current value with other operators, such as changing "Zero-based" type with "One-based" type.
- `FLR`: For Limit Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/foriterator.html) to the definition of the For iterator block in Matlab/Simulink.
The FLR operator changes the block's current value with other operators, such as changing the current "x" limit value with "x*2" limit value.
- `UDO`: Unit Delay Operation
Please refer (https://nl.mathworks.com/help/simulink/slref/unitdelay.html) to the definition of the unit delay block in Matlab/Simulink.
The UDO operator changes the block's current value with other operators, such as changing "Columns as channels (frame based)" value with "Elements as channels (sample based)" value.
- `SCR`: Switch Criteria Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/switch.html) to the definition of the switch block in Matlab/Simulink.
The SCR operator changes the block's current value with other operators, such as changing "u2 >= Threshold" value with "u2 ~= 0" value.
- `STR`: Switch Threshold Replacement
Please refer (https://nl.mathworks.com/help/simulink/slref/switch.html) to the definition of the switch block in Matlab/Simulink.
The STR operator changes the block's current value with other operators, such as changing the current "x" threshold value with "x+10" value.
- `CR`: Constant Replacement
  Please refer (https://nl.mathworks.com/help/simulink/slref/constant.html) to the definition of the constant block in Matlab/Simulink.
The CR operator changes the block's current value with other operators, such as changing the current "x" value with "x+1, x+10, x+100, x-1, x-10, x-100" values.

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

### Mutant Operators For Stateflow
Note: The Stateflow extension has not yet been included in the current version of MUT4SLX. We will release this version soon.
- `LOM`: Logical Operation Mutation
Please refer (https://nl.mathworks.com/help/stateflow/ug/operations-for-stateflow-data.html) to the definition of the logical operators in Matlab/Stateflow.
The LOI operator changes the current value of the logical operator with another different operator, such as changing the "&&" with the "||" operator.
- `ROM`: Relational Operation Mutation
Please refer (https://nl.mathworks.com/help/stateflow/ug/operations-for-stateflow-data.html) to the definition of the relational operators in Matlab/Stateflow.
The ROI operator changes the current value of the relational operator with other different operators, such as changing ">" with "<, >=, <=, ==, ~=" operators.
- `BOM`: Bitwise Operation Mutation
Please refer (https://nl.mathworks.com/help/stateflow/ug/operations-for-stateflow-data.html) to the definition of the relational operators in Matlab/Stateflow.
The BOI operator changes the current value of the bitwise operator with other different operators, such as changing "&" with "|, ^, ~" operators.
- `MOM`: Math Operation Mutation
Please refer (https://nl.mathworks.com/help/stateflow/ug/operations-for-stateflow-data.html) to the definition of the relational operators in Matlab/Stateflow.
The MOI operator changes the current value of the math operator with other different operators, such as changing "+" with "-, *, /" operators.
- `NOM`: Non-bitwise Operation Mutation
Please refer (https://nl.mathworks.com/help/stateflow/ug/operations-for-stateflow-data.html) to the definition of the relational operators in Matlab/Stateflow.
The NOI operator changes the current value of the non-bitwise operator with an empty character, such as deleting "!" operator.
- `CCM`: Control Chart Mutation
Please refer (https://nl.mathworks.com/help/stateflow/ug/using-temporal-logic-in-state-actions-and-transitions.html) to the definition of the control charts in Matlab/Stateflow.
The CCI operator changes the current value of the after operator in a control chart with other possible values, such as changing the current "x" value with "x+1, x+10, x+100, x-1, x-10, x-100" values.
- `CDM`: Control chart Duration Mutation
Please refer (https://nl.mathworks.com/help/stateflow/ug/using-temporal-logic-in-state-actions-and-transitions.html) to the definition of the control charts in Matlab/Stateflow.
The CDI operator changes the current value of the duration operator in a control chart with other possible values, such as changing the current "x" value with "x+1, x+10, x+100, x-1, x-10, x-100" values.
- `TOM`: Transition Order Mutation
Please refer (https://nl.mathworks.com/help/stateflow/ug/execution-order-for-parallel-states.html) to the definition of the execution order in Matlab/Stateflow.
The TOI operator changes the execution in a model with other possible orders, such as changing the current "1-2-3" value with "1-3-2, 2-3-1, 2-1-3, 3-1-2, 3-2-1" orders.

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
- `tests/`: This directory contains the smoke tests for the tool.
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

## Testing

To run the tests for this project, you can use the following command:

```
make test # or pytest
```

### Cite This

1. Ceylan, H. I., Kilincceker, O., Beyazit, M., & Demeyer, S. (2023, September). MUT4SLX: Fast Mutant Generation for Simulink. In 2023 38th IEEE/ACM International Conference on Automated Software Engineering (ASE) (pp. 2086-2089). IEEE.
2. Nuyens, S., Ceylan, H. I., Kilincceker, O., Beyazit, M., & Demeyer, S. (2024, March). MUT4SLX: Extensions for Mutation Testing of Stateflow Models. In 2024 IEEE International Conference on Software Analysis, Evolution and Reengineering-Companion (SANER-C) (pp. 215-218). IEEE.

