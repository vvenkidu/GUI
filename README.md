# Graphical User Interface: GUI
## Measurement
Here are codes to create a desktop GUI for devices typically used in RF labs. AWGs, VNAs and Oscilloscopes typically require user's change measurement or signal-generator settings manually, using keypads on the device.
We hope to create a direct link between user's desktop computers and the measurment device to fascillitate quick and easy settings' change. These codes are used primarily for measurement and simulation purposes.
We will use the python libraries **tk** and **pyvisa** to establish connection with the device and create the GUI respectively.
We use SCPI commands (standard commands) to change the device settings: each device has its own set of commands that follow the SCPI structure. Documentation for SCPI commands, including notes about their structure and implementation, are linked bellow.
- VNA :
- AFG : [AFG 3000](https://www.tek.com/en/function-generator/afg3000-function-generator-manual/afg3000-series)
- OSC :
> Both python libraries are open-source. We include links to the [tk](https://docs.python.org/3/library/tk.html) and [pyvisa](https://pyvisa.readthedocs.io/en/latest/) documentation.
``` python
import pyvisa
import tk
```

To install pyvisa
``` shell
pip install pyvisa
```

### Establishing VISA connection
Before we can send commands to these devices, we need to establish either a USB or network connection with the device. We also need to install the proper drivers and packages onto our desktop computer.
- IO libraries suite
- Python packages

We then need to establish a VISA connection with the device.
- ping device
- *IDN?

The drivers required depend on the device manufactoror.
- Keysight/Agilent [Connection Expert](https://www.keysight.com/us/en/lib/software-detail/computer-software/io-libraries-suite-downloads-2175637.html)
- Tektronix: [TekVISA](https://www.tek.com/en/support/software/driver/tekvisa-connectivity-software-v411)

  
## Simulation
We hope to extend scripted GUI develop additional-features for our full-wave solver simulation tools. Tools such as Sim4Life have a built-in-GUI for basic to advanced manipulation of model geometires and solution settings. Features that are unavailable in this built-in-GUI have to implemented in user-coded jupyter-notebook python scripts. Handling of these python-scripts can be improved by a simple GUI interface for these additional-features. User's that are unfamiliar with the python-code will be able to use these additional-features in short-period of time.
