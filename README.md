Install the required packages to be able to run the evaluation locally.

You need to have Python 3 on your system (a Python version lower than 3.10). Then you can clone this repo and being at the repo's root :: repository_name> ... follow the steps below:
``````
Windows:

  python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt 
`````` 
Linux & MacOs:
``````
  python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  
``````
The both long command-lines have a same structure, they pipe multiple commands using the symbol ; but you may manually execute them one after another.

* Create the Python's virtual environment that isolates the required libraries of the project to avoid conflicts;
* Activate the Python's virtual environment so that the Python kernel & libraries will be those of the isolated environment;
* Upgrade Pip, the installed libraries/packages manager to have the up-to-date version that will work correctly;
* Install the required libraries/packages listed in the requirements.txt file so that it will be allow to import them into the python's scripts and notebooks without any issue.
NB: For MacOs users, please install Xcode if you have an issue.

Run FastAPI
Run the demo apps (being at the repository root):

FastAPI:

Demo

uvicorn src.demo_01.api:app --reload 
Go to your browser at the following address, to explore the api's documentation :

http://127.0.0.1:8000/docs
