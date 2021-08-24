import os
import PyInstaller.__main__


# delete old spec files
spec_files = [file for file in os.listdir(".") if file.endswith(".spec")]
for file in spec_files:
    os.remove(file)

PyInstaller.__main__.run(
    ['main.py', '--onefile', '--noconfirm', '--name', f'splitmap', '--icon', 'zusor_logo.ico'])

