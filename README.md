To install the Python dependencies run:
pip install -r requirements.txt

The Server and slave are in their own dedicated folders.
To compile the client.py run
pyinstaller client.py --onefile

A file called client.exe will appear in dist/

When you open the client.exe on the target machine it will try to connect to the server given by the IP address in the Python script.

When it connects you will have a nice looking "Linux" command line with access to every tool you need. 
