from cx_Freeze import Executable, setup
import sys
import os

PYTHON_INSTALL_DIR = os.path.dirname(sys.executable)
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
include_files = [(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), os.path.join('lib', 'tk86.dll')),
                 (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'), os.path.join('lib', 'tcl86.dll')),
                 ('background.jpeg'), ('logo.ico'), ('logo.jpeg')]
base = None

if sys.platform == 'win32':
    base = "Win32GUI"
directory_table=[
("DesktopShortcut","DesktopFolder",
    "Milk Rate Generater",
    "TARGETDIR",
    "[TARGETDIR]\MilkRateGenerater.exe",
    None,
    None,
    None,
    None,
    None,
    None,
    "TARGETDIR",)
]
msi_data={"Shortcut":directory_table}
bdist_msi_option={'data':msi_data}
executables = [
    Executable(script="MilkRateGenerater.py", base=base, icon="logo.ico")]

setup(
    name="Milk Rate Generater",
    version="1.0",
    author='Sakib Malik',
    description="Milk Rate Generator Software is build for Rate Generate for Everest Milk Machine",
    options={"build_exe": {"packages": ["tkinter", "os"],
                           "include_files": include_files},"bdist_msi":bdist_msi_option,},

    executables=executables
)
