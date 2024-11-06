# PY-NAC
Noughts-And-Crosses/Tic-Tac-Toe in **[Python](https://python.org)**.

<hr />

> [!CAUTION]
> The compiled versions of this all have false-flagged on at least 1 antivirus. This was checked through [virustotal](https://virustotal.com).

> [!CAUTION]
> Because of these false flags the compiled executables will not be given out on their own. You will ***have to*** compile them yourself or use the [python file](/main.py) on it's own if you want to use this.

> [!CAUTION]
> The link to the virustotal checks are [here for windows](https://www.virustotal.com/gui/file/704dfa491d7321ffa73d7fc81103d08f8f494f71110d4f28a5d77871429f74da) and non-existant for Linux.

<hr />

> [!TIP]
> You will need the [fonts folder](/fonts) for the fonts used in the project. These fonts are not made by me they are made by Google (the company) for their logos but I decided to use it still. The font used is called `Product Sans`.

## Dependencies:
- **[Python](https://python.org)** (You probably already have this installed already.)
  -  If you're not sure you have Python installed check your system packages for Linux and Mac and run the command `Python3`.
  -  Or if you're not sure on Windows, check your system PATH variables to see if you have it or run the command `py` to check.
      - To exit the **[Python](https://python.org)** shell/console that is built-in with **[Python](https://python.org)** type `exit()`.

> [!WARNING]
> **[Python](https://python.org)** is needed for even just running the pre-compiled executable from the releases.

### Python import dependencies:
- **[Tkinter](https://docs.python.org/3/library/tkinter.html)** (built in with **[Python](https://python.org)** but might need an install using `sudo apt-get install python3-tk` for Linux)
- **[Turtle](https://docs.python.org/3/library/turtle.html)** (built in with **[Python](https://python.org)**)
- **[Numpy](https://numpy.org/)** (external; download with pip: `pip install numpy`)

<br>

> [!TIP]
> You can use a different compiler like **[Pyinstaller]()** if **[Nuitka](https://nuitka.net/)** doesn't work but it is unrecommended because of the generated executables being false-flagged by antiviruses.

> [!WARNING]
> You will need a few more things for **[Nuitka](https://nuitka.net/)** to work properly. Like a C compiler. See a **[list of those things here](https://nuitka.net/user-documentation/user-manual.html#requirements)**.

### Python compiling dependencies:
- **[Nuitka](https://nuitka.net/)** (external (for compiling); download with pip: `pip install nuitka`)

<hr />

> [!WARNING]
> I will **not** be providing commands for other python compilers apart from **[Nuitka](https://nuitka.net/)**.

## Compile commands:
### Linux (not tested): `nuitka --standalone --onefile --enable-plugin=tk-inter --enable-plugin=numpy --include-data-files="fonts/ProductSans-Regular.ttf=fonts/ProductSans-Regular.ttf" --windows-icon-from-ico=favicon.ico main.py`

### Windows (tested): `nuitka --standalone --onefile --enable-plugin=tk-inter --enable-plugin=numpy --include-data-files="fonts/ProductSans-Regular.ttf=fonts/ProductSans-Regular.ttf" main.py`
