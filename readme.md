# Trilobot STEM Packup

A robot learning platrofrm using a Raspberry Pi 4B+ for STEM outreach

# Pre Requesites

You must enable:

• i2c: `sudo raspi-config` -> Interface Options -> I2C -> Enable

You must install:

• git: `sudo apt install git`
• trilobot, sshkeyboard, smb3: `pip install trilobot sshkeyboard`

# Setup

### Install the trilobot library
```Python
git clone https://github.com/pimoroni/trilobot-python
cd trilobot-python
sudo ./install.sh
```
Press N when prompted to move examples to a convenient place

### Clone this packup
`git clone https://github.com/AstraAppivate/riat-trilobot.git`

### Connect using VSCode Remote SSH
- Install VSCode Remote SSH extension
- Connect to the raspberry pi using its username@ip address
- Wait for the connection to finish
- Install the VSCode Python extension
- move into the riat_packup directory
- Run the controller using `python3 remote_control.py`
