# MUT4SLX: Fast Mutant Generation for Simulink : Replication Package

This is the replication package for the paper: MUT4SLX: Fast Mutant Generation for Simulink.

## Preparation Step

### Install MATLAB R2021b:

1. Visit the MathWorks website (https://www.mathworks.com) and download the **MATLAB R2021b** installer appropriate for your operating system.
2. Run the installer and follow the on-screen instructions to install MATLAB on your computer.
3. Activate MATLAB using your MathWorks account or the provided license key.
4. During the installation process, you will be presented with different installation options. Select the "Custom" installation option to choose specific packages to install.
    - Simulink
    - Control System Toolbox
    - Embedded Coder
    - MATLAB Coder
    - MATLAB Report Generator
    - Polyspace Bug Finder
    - Polyspace Code Prover
    - Requirements Toolbox
    - Robust Control Toolbox
    - Simscape
    - Simscape Fluids
    - Simulink Check
    - Simulink Code Inspector
    - Simulink Coder
    - Simulink Control Design
    - Simulink Coverage
    - Simulink Design Verifier
    - Simulink Report Generator
    - Simulink Test
    - System Composer

**Please note that the availability of specific packages may depend on the type of license you have or the edition of MATLAB you are installing. Ensure that you have the necessary licenses or access rights to install and use the additional packages.**

### Install Python 3.9.16:

Visit the official Python website (https://www.python.org/downloads/) and download the Python 3.9.16 installer for your operating system.
Run the installer and follow the installation wizard.
**Make sure to select the option to add Python to the system PATH during** the installation process. This will make it easier to run Python from the command line.

### Installing Python Matlab Engine API

To install the `matlab.engine` for Python, you can follow these steps:

1. Start MATLAB and obtain the MATLAB root folder path by typing `matlabroot in the MATLAB command window. Take note of the returned path.

2. Open a command prompt or terminal on your operating system.
    Navigate to the MATLAB Python engine folder corresponding to your operating system:
    
    On Windows:
    ```bash
    cd "<matlabroot>\extern\engines\python"
    ```
    Replace <matlabroot> with the MATLAB root folder path obtained in step 1.

    On Linux:
    ```bash
    cd "<matlabroot>/extern/engines/python"
    ```
    Replace <matlabroot> with the MATLAB root folder path obtained in step 1.

    On macOS:
    ```bash
    cd "<matlabroot>/extern/engines/python"
    ```
    Replace <matlabroot> with the MATLAB root folder path obtained in step 1.

3. Run the following command to install the MATLAB Engine API for Python:

    ```bash
    python setup.py install
    ```
    This command will install the matlab.engine module for Python.

Wait for the installation process to complete. Once finished, you should see a message indicating successful installation.

The `matlab.engine` module allows you to call MATLAB functions and execute MATLAB code from Python. After installing the MATLAB Engine API for Python, you can use the matlab.engine module in your Python scripts to interact with MATLAB.

Feel free to explore the documentation for further details: [Matlab Documentation](https://www.mathworks.com/help/matlab/matlab-engine-for-python.html)

**Please note that you may need administrator privileges to execute some of the commands, depending on your operating system configuration.**

  
### Cloning Project 
1. Clone the repository: Open a command prompt or terminal and run the following command:
    ```bash
    git clone https://github.com/haliliceylan/MUT4SLX.git
    ```
    This command will clone the repository and download the project files to your local machine.
## Usage
To use the project, run the following command from the project directory:

```bash
python MUT4SLX.py --model Heli
```
This command will execute the MUT4SLX.py script with the --model argument set to Heli. Adjust the value of --model to the specific model you want to use. This command will initiate the execution of the project, performing the necessary operations based on the specified model.
Other possible commands to run:
- `python MUT4SLX.py --model sf_aircraft`
- `python MUT4SLX.py --model Aircraft`
- `python MUT4SLX.py --model AutotransModel`

Make sure you have MATLAB and the MATLAB Engine API for Python properly installed, as mentioned earlier, to ensure the successful execution of the project.

Feel free to explore the cloned repository for more details on the project, including additional usage options, configuration settings.
