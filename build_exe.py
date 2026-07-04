#!/usr/bin/env python
"""
Build script to create ThePancakeMEsiropi.exe using PyInstaller
Run this script: python build_exe.py
"""

import subprocess
import sys
import os

def build_exe():
    print("Building ThePancakeMEsiropi.exe...")
    print("="*50)
    
    # PyInstaller command
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--windowed",
        "--icon=icon.ico" if os.path.exists('icon.ico') else "",
        "--name=ThePancakeMEsiropi",
        "--distpath=./dist",
        "--buildpath=./build",
        "--specpath=./build",
        "main.py"
    ]
    
    # Remove empty strings
    cmd = [c for c in cmd if c]
    
    try:
        result = subprocess.run(cmd, check=True)
        print("="*50)
        print("✓ SUCCESS! EXE created at: dist/ThePancakeMEsiropi.exe")
        print("="*50)
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    build_exe()
