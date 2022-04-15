# links_parser
Allows analyzing web-page links.

## Start project

### Initialization
Install all dependencies (need only for GUI mode)
```shell
cd links_parser            # Go to the folder
python3 -m venv venv       # Create venv
source venv/bin/activate   # Activate venv
# Install dependencies
pip install -r read pip install -r requirements.txt
```
Compile QT resources (need only for GUI mode)
```shell
pyrcc5 ./gui/resources.qrc -o ./gui/resources.py
```

### Running
CMD mode: 
```shell
python links_parser.py 'https://www.python.org/'
```

GUI mode:
```
python links_parser.gui.py
```
