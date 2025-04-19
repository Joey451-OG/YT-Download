# Contributing

Make sure your python virtual environment folder is name `venv` in order to be ignored by `.gitignore`.


## Dependencies
YT-DLP
```bash
pip install yt-dlp
```

FreeSimpleGUI
```bash
pip install FreeSimpleGUI
```

PyYaml
```bash
pip install PyYaml
```


## Notes for Windows Developers
To allow Powershell to run the active script for the python virtual env. Use:
```powershell
PS:\> Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope Process
```