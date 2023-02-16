# PlatformIO Hex2MassStorage
This Python script automatically moves a .hex file to a devboard on build. It simplifies the process of transferring the compiled code to the target device.

## Requirements
* Python 3.10 or later
* Latest PlatformIO installation

## Installation
1. Clone this repository `git clone https://github.com/Cuprum77/PlatformIO-Hex2MassStorage.git`

## Usage
1. Place the Python script in the same directory as your PlatformIO project
2. Open your projects `platformio.ini`
3. Add in 
```ini
extra_scripts = post:extra_script.py
device_label = {DEVICE LABEL}
```
4. Change the `{DEVICE LABEL}` to the name your devboard shows up as.
For example, if your board shows up as `DEVICE` you change it to `device_label = DEVICE`.

## Contributing
If you find a bug or have an idea for a feature, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information
