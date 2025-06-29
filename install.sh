#!/bin/bash
pkg update && pkg upgrade -y
pkg install python git -y
pip install -r requirements.txt
echo "Installation done!"