# Python Shell

**_A Linux Shell in Python_**

Hey guys!
This is my attempt at a ~~great~~ not very good Python-based Linux shell.

Instructions:

`git clone https://github.com/supercoderguy/Python-Shell.git`

`chmod +x /path/to/shell.py`

`sudo ln -s /path/to/shell.py /usr/local/bin/pythonshell`

`sudo nano /etc/shells`

In that file, add this to the bottom:
`/usr/local/bin/pythonshell`

Then save the changes and execute this command:
`chsh -s /usr/local/bin/pythonshell`
