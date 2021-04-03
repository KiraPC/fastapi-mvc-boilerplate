# 🧰 fastapi-mvc-boilerplate

A sample FastAPI project implemented using the MVC Pattern.

## 💡 Features

-   [✔️] MIT License
-   [✔️] FastApi + SQLAlchemy
-   [✔️] Class Based Controller with fastapi-router-controller
-   [✔️] Tests with unittest
-   [✔️] Dockerfile with tiangolo/uvicorn-gunicorn-fastapi:python3.8
-   [✔️] Configuration management with Environment Variables Interpolation
-   [✔️] Centralized logging management
-   [✔️] Log requests end-time
-   [✔️] Formatted Exception Handler
-   [✔️] Validation Exception Handler
-   [✔️] Vscode dotfiles preconfigured
-   [✔️] GitHub action for unit tests on PR
-   [✔️] Sample Gunicorn Configuration


## 🔨 How to use

- Clone this repository or download it. Customize!
- Just click on 'Use this template' button on GitHub page

## 🌞 How to start app
First install the dependencies
```bash
pip install -r requirements.txt
```

### 📘 If you are using VSCode
I included in the repository the VSCode configuration for tasks and debugging.

So, you can just use the VSCode shortcut to start the application:
- Start FastApi
- Start FastApi with Gunicorn

There are also two debug configurations:
- Debug FastApi
- Debug Python Current File

See more about VScode [Tasks](https://code.visualstudio.com/docs/editor/tasks) and [Debug](https://code.visualstudio.com/docs/python/debugging).

### ✋ Manually
- Start with unicorn
```bash
pip install unicorn
uvicorn server/main:app --reload
```

- Start with gunicorn
```bash
pip install gunicorn
gunicorn server/main:app --config gunicorn_conf.py
```

## 🔨 How to run tests
Install tests requirements
```bash
pip install -r tests/requirements.txt
```

Run
```bash
python3 -m unittest discover -s tests -p '*_test.py'
```

### 📔 Notes
I am open to suggestions and criticisms, please, if something seems wrong or can be improved, tell it through an issue on the project

