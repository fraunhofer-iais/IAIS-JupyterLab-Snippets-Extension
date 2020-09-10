

"""
Standard Library
https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
https://wiki.python.org/moin/TkInter
"""

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
