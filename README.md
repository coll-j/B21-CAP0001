# B21-CAP0001 (Cloud)
Hoax & hate speech game [backend]

# How to Install & Run (need to enter project first)
## 1. Install (if not exists) and Create Virtual Environment
### a. Run command bellow
```
python3 -m venv venv
```

### b. Activate the environment
```
. venv/bin/activate (macOS/linux)
venv\Scripts\activate (windwos)
```

<br/>


## 2. Install all requirements library
Using all library using :
```
pip install -r requirements.txt
```

<br/>

## 3. Run the app
### a. Export the main.py (or entry that contain run function) into system variable
```
export FLASK_APP=hello (Bash)
set FLASK_APP=hello (CMD)
$env:FLASK_APP = "hello" (Powershell)
```

### b. Run and enjoy
```
flask run (without debugging) (or)
python main.py (with debugging)
```