#TMI - Social Networking Platform

###To Do:
-   [ ] **~~Everything~~**
-   [x] **Connect to Database**
-   **Setup Model Classes:**
    - [x] User
    - [x] Groups
    - [x] Pages
-   **Add User Sessions:**
    -   [x] Log in
    -   [x] Log out
-   **Create dynamic pages for user interaction:**
    -   [x] Index
    -   [x] Home
    -   [x] Messages
    -   [ ] Market
    -   [ ] Profile
    -   [ ] ~~Friend List~~
-   **Handle user interactions:**
    -   [ ] ~~Add Friends~~
    -   [ ] Buy Stuff
    -   [x] Message Friends
    -   [x] Create Groups
    -   [x] Search Users
    -   [ ] List for sell
    -   [ ] like/unlike post and comments


###Setup:
1.  **Install Python 3.5:**
    *   On Windows:
        1.  Download the installer from https://www.python.org/downloads/release/python-352/
        2.  Execute installer and follow instructions on screen
    *   On Mac:
        1.  Download the mac installer from https://www.python.org/downloads/release/python-352/
        2.  Execute installer and follow instructions on screen
    *   On Mac (Using brew):
        1.  Follow instructions on http://brew.sh/ to install brew
        2.  Open a new terminal
        3.  Run the following command on the terminal
            ```brew install python3```
2.  **Clone the repo:**
    1.  Install Git if necessary, you can use brew if on mac
       ``` brew install git``` 
    2.  Use git to clone the repository:
        ```git clone https://github.com/mshankar13/tmi.git```
3.  **Start the virtual envinroment:**
    1.  Open a terminal in the project directory
    2.  Create a virtual environment:
        ```$ virtualenv venv```
        note: you may need to specify a path to your python3 binary if your default version is 2
        ``` virtualenv -p /path/to/file venv```
    3.  Activate the virtual environment:
        * On Mac/Linux:
            ```$ source venv/bin/activate```
        * On Windows:
            ``` 
                $ cd venv/Scripts
                $ activate.bat
                $ cd ../..
            ```
    4.  Install dependencies:
        ```$ pip install -r requirements.txt```
    5.  Run server:
        ```$ python tmi.py```
          
###Recommended Software:
*   Pycharm, Python IDE: https://www.jetbrains.com/pycharm/download/ 
    or just use your favorite text editor

###Resources:
- Back-end:
    -   Flask: http://flask.pocoo.org/docs/0.11/tutorial/
    -   Flask-Forms: https://flask-wtf.readthedocs.io/en/stable/quickstart.html#creating-forms
    -   SQLAlchemy: http://flask-sqlalchemy.pocoo.org/2.1/
    -   ~~~Excellent Lynda tutorial: https://www.lynda.com/Flask-tutorials/Learning-Flask/521231-2.html~~~ Outdated

- Front-end:
    -   PureCSS: http://purecss.io/
