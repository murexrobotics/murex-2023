<p align="center">
    <img src="https://github.com/murexrobotics/murex-2023/blob/Restructured-Repository/logo.png?raw=true" width="300">
</p>

# MUREX ROV 2022-2023

Codebase for the MUREX 2023 ROV for the MATE Underwater Robotics Competition.

## Table of Contents
- [Setup](Setup)
- [Usage](Usage)
- [License](License)

## Setup
To use propperly use the Murex codebase the user must have some software installed in addition to the MUREX codebase.

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

## License

Licensed under the [MIT](LICENSE) License

Copyright (c) 2023 MUREX Robotics

