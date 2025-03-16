
# Class workspace

Create date-named folder and symlimk to 2 folder: Homework and Classwork

## Important note:

In current state, this script expect a filesystem with symlink support and a folder structure as:
```
/Homework

/Classwork

/Workspace
  main.py
```
Tldr: Will broken if 2 requirements aren't met

> [!CAUTION]
> There is no backup or revert, so please use this script with your own risk

## Usage

```bash
git clone https://github.com/gingercookies/silly_python.git
cd silly_python/class_workspace
python3 src/main.py
```

## To-do
- Code cleanup
- Creating folders automatically after detect the source folder isn't exist
- Change folder name with a .env file (maybe?)