<p align="center">
    <img src="https://github.com/murexrobotics/murex-2023/blob/main/logo.png?raw=true" width="300">
</p>

# MUREX ROV 2022-2023

Codebase for the MUREX 2023 ROV for the MATE Underwater Robotics Competition.

## Table of Contents
- [Setup](Setup)
- [Usage](Usage)
- [Design](Design)
- [License](License)

## Setup
To use properly use the Murex codebase the user must have some software installed in addition to the MUREX codebase.

### Dev Dependencies
- [Python](https://www.python.org/downloads/) v3.9 (Or Newer)
- [NodeJS](https://nodejs.org/en/download) v18.6.1 (Or Newer)
- [FFmpeg](https://ffmpeg.org/download.html) v5.1.2 (Or Newer)

### Installation
```Bash
git clone https://github.com/murexrobotics/murex-2023.git
cd murex-2023
python3 -m pip install -r requirements.txt
cd web-interface
npm i
cd ../
```

## Usage

For optimal usage, start topside, then aquatic then web-interface.

### Topside
```Python
python3 topside
```

### Aquatic
```Bash
python3 aquatic
```

### Web Interface
```Bash
cd web-interface
npm run dev
```

## Design
This is a brief overview of how the ROV was designed.

### Mechanical
[ROV CAD](https://cad.onshape.com/documents/f2c5e508349c88b025f713bf/w/5608aa019685f90fd8c58b6c/e/0061e131f16a5293ec96639c)
### Programming
| Codebase | Role |
|----------|------|
| [Aquatic](https://github.com/murexrobotics/murex-2023/tree/main/aquatic) | Handles interfacing with sensors and thrusters. Control of ROV. |
| [Topside](https://github.com/murexrobotics/murex-2023/tree/main/topside) | Decodes control input and overall ROV control signals. |
| [Web Interface](https://github.com/murexrobotics/murex-2023/tree/main/web-interface) | Displays telemetry data from ROV for realtime monitoring and emergency control. |
### Electrical

| PCB | Role |
|-----|------|
| Integration PCB | Supply power to all components, sensors and PWM signal generator. |
| ESC Integration PCB | Connects directly to ESC's and Integration PCB to make connecting ESC's easier. **Was not used in final revision** |

## License

Licensed under the [MIT](LICENSE) License

Copyright (c) 2023 MUREX Robotics

