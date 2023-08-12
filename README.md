## Graphical User Interface: GUI

Here are codes used to create a GUI for measurement and simulation purposes for typical devices in RF labs. AWGs, VNAs and Oscilloscopes typically require user's change measurement or signal-generator settings manually, using keypads on the device.
We hope to create a direct link between user's desktop computers and the measurment device to fascillitate quick and easy settings' change
We will use the python libraries **tk** and **pyvisa** to establish connection with the device and create the GUI respectively.
We use SCPI commands (standard commands) to change the device settings: each device has its own set of commands that follow the SCPI structure.
- VNA :
- AFG :
- OSC :
> Both python libraries are open-source. We include links to the [tk](https://docs.python.org/3/library/tk.html) and [pyvisa](https://pyvisa.readthedocs.io/en/latest/) documentation.
``` python
import pyvisa
import tikzpicture
```
