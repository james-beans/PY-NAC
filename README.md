# pyimgui-hw
"Hello, world." in a nested Pygame and Imgui window.

<hr />

> [!WARNING]
> Binaries for windows and Linux have not been made yet I will make them soon.

<hr />

> [!TIP]
> To compile this, you will need either Pyinstaller or Nuitka. I prefer Nuitka because it doesn't give of antivirus malfunctions. Because of this I will not be giving the command to compile with Pyinstaller. If you still want to you will need to trubleshoot and make a command yourself.

## Compile command:
### Windows (tested on Windows 11):
`nuitka --standalone --enable-plugin=numpy --include-package=imgui main.py`
### Linux (tested on Debian 12):
> [!WARNING]
> I haven't changed the script so this will work on Linux yet. It will not work at the moment.
