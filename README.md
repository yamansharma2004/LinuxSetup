# LinuxSetup

### System Update and Program Installation Script

This script automates the process of updating your system packages and installing commonly used programs and libraries. It also provides an option to clone repositories from GitHub.

### Prerequisites

- Python 3.x
- `subprocess`, `os`, and `optparse` modules

### Usage

Ensure that you have Python installed on your system. Run the script with elevated privileges (sudo).

```bash
sudo python main.py
```

#### Options

- `-a, --argument`: Specify the mode of operation. Default is `None`.
  - `None`: Performs basic system update and installs programs.
  - `with github`: Clones repositories from GitHub in addition to basic operations.

### Note

- Running the script without any arguments will perform a basic system update and install listed programs.
- Ensure to review and customize the `list_` and `github` variables to suit your requirements.

### Disclaimer

This script is provided as-is and without warranty. Use it at your own risk.

### Author

Yaman sharma
