<a href="#">
    <img src="https://raw.githubusercontent.com/pedromxavier/flag-badges/main/badges/TR.svg" alt="made in TR">
</a>

# KDVAT
KDVAT is an advanced VAT calculation application that runs on Linux, macOS, and Windows. With its user-friendly interface, you can easily calculate VAT-inclusive or VAT-exclusive amounts, process bulk calculations, and export results to Excel. Additionally, you can view transaction history and generate detailed statistical reports.

<h1 align="center">KDVAT VAT Calculation LOGO</h1>

<p align="center">
  <img src="kdv.png" alt="KDVAT Logo" width="150" height="150">
</p>


----------------------

# Linux Screenshot
![Linux(pardus)](screenshot/kdvat_linux.gif)  

--------------------
Install Git Clone and Python3

Github Package Must Be Installed On Your Device.

git
```bash
sudo apt install git -y
```

Python3
```bash
sudo apt install python3 -y 

```

pip
```bash
sudo apt install python3-pip

```

# Required Libraries

PyQt5
```bash
pip install PyQt5
```
PyQt5-sip
```bash
pip install PyQt5 PyQt5-sip
```

PyQt5-tools
```bash
pip install PyQt5-tools
```

Required Libraries for Debian/Ubuntu
```bash
sudo apt-get install python3-pyqt5
sudo apt-get install qttools5-dev-tools
sudo apt-get install python3-pillow
sudo apt-get install python3-pypdf2
```
openpyxl
```bash
pip3 install openpyxl
```
requests
```bash
pip3 install requests
```

matplotlib
```bash
pip3 install matplotlib
```

defusedxml
```bash
pip3 install defusedxml
```

----------------------------------


# Installation
Install KDVAT

```bash
sudo git clone https://github.com/cektor/KDVAT.git
```
```bash
cd KDVAT
```

```bash
python3 kdvat.py

```

# To compile

NOTE: For Compilation Process pyinstaller must be installed. To Install If Not Installed.

pip install pyinstaller 

Linux Terminal 
```bash
pytohn3 -m pyinstaller --onefile --windowed kdvat.py
```

MacOS VSCode Terminal 
```bash
pyinstaller --onefile --noconsole kdvat.py
```

# To install directly on Linux

Linux (based debian) Terminal: Linux (debian based distributions) To install directly from Terminal.
```bash
wget -O Setup_Linux64.deb https://github.com/cektor/KDVAT/releases/download/1.00/Setup_Linux64.deb && sudo apt install ./Setup_Linux64.deb && sudo apt-get install -f -y
```

Windows Installer CMD (PowerShell): To Install from Windows CMD with Direct Connection.
```bash
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/cektor/KDVAT/releases/download/1.00/Setup_Win64.exe' -OutFile 'Setup_Win64.exe'" && start /wait Setup_Win64.exe
```

Release Page: https://github.com/cektor/KDVAT/releases/tag/1.00
----------------------------------

