# MUT4SLX

This project focuses on performing mutation testing on a model implemented in MATLAB/Simulink. It applies various mutation operators to the model and evaluates the effectiveness of the test suite by measuring how many mutants are killed.

## Description

The Simulink Model Mutation Testing project provides a framework for generating mutants, executing tests, and analyzing the results. It utilizes the MATLAB environment to load the model, apply mutations, run tests, and collect metrics.

## Features

- Mutation generation: Apply a set of predefined mutation operators to the model.
- Test execution: Run test cases against both the original model and the generated mutants.
- Mutation analysis: Calculate mutation scores, count killed mutants, and identify survived mutants.
- HTML report generation: Generate an HTML report summarizing the mutation analysis results.
- Visualization: Visualize the mutation analysis results using bar charts.

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

- MATLAB [version R2019a](https://nl.mathworks.com/products/matlab.html)
- Python [version 3.7.8](https://www.python.org/downloads/release/python-378/)
- Libraries: [matlab.engine](https://www.mathworks.com/help/matlab/matlab-engine-for-python.html), [jinja2](https://jinja.palletsprojects.com/)

### Installation

For windows you can follow this https://github.com/haliliceylan/MUT4SLX-Duco/blob/main/INSTALL-WINDOWS.md
1. Clone the repository: `git clone https://github.com/haliliceylan/MUT4SLX-Duco.git`
2. Install the required libraries: `pip install -r requirements.txt`

### Usage

1. Modify the `model_files.json` file to specify the models and their configurations.
2. Run the main script: `python MUT4SLX.py --model MODEL`
3. View the generated HTML report: `open <model_name>.html`

## File Structure

- `MUT4SLX.py`: Main script for performing mutation testing.
- `model_files.json`: Configuration file specifying the models and their details.
- `index.html.j2`: Jinja2 template for generating the HTML report.
- Other supporting files and directories.

## Example Use Cases


### Example use case with TestLibStdPidCtrlShared_Sum_S32_S32_to_lim_S32
[![asciicast](https://asciinema.org/a/B0fasAEl1l7zfKLe119TqfpFe.svg)](https://asciinema.org/a/B0fasAEl1l7zfKLe119TqfpFe)
### Example use case with TestLibStdPidCtrlShared_PidCtrl_RsltU16Mult255
[![asciicast](https://asciinema.org/a/Z6VAbWctcYOrxkg0D5kGuw74H.svg)](https://asciinema.org/a/Z6VAbWctcYOrxkg0D5kGuw74H)
