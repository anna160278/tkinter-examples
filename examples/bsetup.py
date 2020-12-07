import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os"],
    "excludes": ["tkinter"],
    'initScript': 'Console'
}

setup(name="名称",
      version="版本",
      description="描述",
      options={"build_exe": build_exe_options},
      executables=[Executable("b.py", targetName='bbbbb')])
