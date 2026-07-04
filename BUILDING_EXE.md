# Building ThePancakeMEsiropi.exe

## Quick Start

### Prerequisites
- Windows 7 or newer
- Python 3.8+ installed and added to PATH
- Internet connection for downloading dependencies

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- PySimpleGUI (GUI library)
- requests (HTTP library)
- PyInstaller (EXE builder)

### Step 2: Build the EXE

```bash
python build_exe.py
```

The script will:
1. Run PyInstaller with optimized settings
2. Create the executable in `dist/ThePancakeMEsiropi.exe`
3. Show success/error messages

### Step 3: Test the EXE

```bash
.\dist\ThePancakeMEsiropi.exe
```

Or double-click `ThePancakeMEsiropi.exe` in the `dist` folder.

---

## Manual Build (Advanced)

If `build_exe.py` doesn't work, run PyInstaller directly:

```bash
pyinstaller --onefile --windowed --name=ThePancakeMEsiropi main.py
```

---

## Distributing the EXE

### Create a ZIP Distribution

1. Navigate to the `dist` folder
2. Create a new folder: `ThePancakeMEsiropi_v1.0`
3. Copy into it:
   - `ThePancakeMEsiropi.exe`
   - `README.md`
   - `apps_database.json` (optional - EXE creates its own)

4. Zip the folder:
   ```bash
   # Windows
   Compress-Archive -Path ThePancakeMEsiropi_v1.0 -DestinationPath ThePancakeMEsiropi_v1.0.zip
   
   # Linux/Mac
   zip -r ThePancakeMEsiropi_v1.0.zip ThePancakeMEsiropi_v1.0
   ```

5. Share the ZIP file!

---

## Troubleshooting

### "PyInstaller not found"
```bash
pip install pyinstaller --upgrade
```

### "Python command not found"
Add Python to your PATH:
- Windows: Search "Edit the system environment variables"
- Add your Python installation folder (e.g., `C:\Python312`)
- Restart your terminal

### EXE is too large (>100MB)
This is normal for PyInstaller bundles. You can reduce size by:
1. Using `--strip` flag
2. Using UPX (advanced)
3. Using auto-py-to-exe GUI tool

### EXE won't run on other computers
- Make sure the EXE is 64-bit (default)
- Test on multiple Windows versions
- Check Windows Defender isn't blocking it

### Building from clean state
```bash
rm -r build dist __pycache__  # Clean old builds
python build_exe.py            # Build fresh
```

---

## Advanced: Adding an Icon

1. Create or find a `.ico` file (e.g., `icon.ico`)
2. Place it in the same directory as `main.py`
3. The build script automatically detects and uses it

---

## Build Output

After a successful build:

```
dist/
└── ThePancakeMEsiropi.exe     # The main executable (~50-100MB)
```

The EXE is self-contained and doesn't require Python to be installed on the target computer.

---

## Next Steps

✓ **Share the EXE** in a ZIP file with the README

✓ **Create an installer** (optional) using NSIS or Inno Setup

✓ **Add auto-updates** (advanced) by checking a remote version file

✓ **Sign the EXE** for Windows SmartScreen trust (advanced)
