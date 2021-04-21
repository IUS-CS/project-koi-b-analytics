	User Guide
Building from CMD – 

We will be using a virutal environment to build this program.

You will need Python version 3.8.8 - 3.9


In CMD navigate to a folder of your choice.

git clone https://github.com/IUS-CS/project-koi-b-analytics.git

python -m pip install --upgrade pip setuptools virtualenv

python -m virtualenv kivy_venv

windows: kivy_venv\Scripts\activate

macos/linux: source kivy_venv/bin/activate


navigate to  \kivy_venv\Lib\site-packages\kivy\uix\popup.py -comment out lines 215-217 -

cd project-koi-b-analytics/doc

pip install -r requirements.md

cd..

cd /src

python koib_build.py
