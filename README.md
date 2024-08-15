
# Web AI interface (WAII) 

A simple user interface for interacting with AI technologies using Python and Flask

## Project setup

These instructions walk you through getting the WAII project set up for
development and testing. The general steps are installing some prerequisite
software, cloning the project from the code repository, setting a few environment 
variables, and running the configuration installation. The code project uses
[Python Poetry](https://python-poetry.org/) to manage packages and
the Python runtime environment.

Note: You need a Google Gemini API Key to be able to run the project, which you
can obtain from the 
[Google Gemini API](https://ai.google.dev/gemini-api/docs/api-key) page.

### Install the prerequisites

The WAII project uses Python 3 and Python Poetry to manage packages and
run the application. The following installation instructions are for a Linux
host machine.

To install the required software:

1.  Install Python 3 and the `venv` virtual environment package for Python.\
<pre>
sudo apt update
sudo apt install git pip python3-venv
</pre>
1.  Install Python Poetry to manage dependencies and packaging for the
    project.\
<pre>
curl -sSL https://install.python-poetry.org | python3 -
</pre>

You can use Python Poetry to add more Python libraries if you extend the
project. For more information about Python Poetry, see the
[Python Poetry](https://python-poetry.org/docs/) documentation.

### Clone and configure the project

Download the project code and use the Poetry installation command to download
the required dependencies and configure the project. You need
[git](https://git-scm.com/) source control software to retrieve the
project source code.

To download and configure the project code:

1.  Clone the git repository using the following command.\
<pre>
git clone https://github.com/joefernandez/waii.git
</pre>
1.  Move to the `waii` project root directory.\
<pre>
cd waii/
</pre>
1.  Run the Poetry install command to download dependencies and configure
    the project:\
<pre>
poetry install
</pre>

### Set environment variables

Set a few environment variables that are required to allow the WAII code
project to run, including a
[Google Gemini API Key](https://ai.google.dev/gemini-api/docs/api-key). 
You add these variable settings to a `.env` file, which is read by the 
web application.

Caution: Treat your API Key like a password and protect it appropriately. Don't
embed your key in publicly published code.

To set the environment variables:

1.  Get a [Google Gemini API Key](https://ai.google.dev/gemini-api/docs/api-key) 
    and copy the key string.
1.  Set the API Key as an environment variable for the project, by creating
    `.env` text file at this location in your clone of the project:\ 
    `<waii-project>/web_ai_interface_app/.env`
1.  After creating the `.env` text file, add the following settings and save it:
<pre>
API_KEY=&lt;YOUR_API_KEY_HERE&gt;
</pre>

### Run and test the application

1.  In a terminal window, navigate to the `waii/web_ai_interface_app/`
    directory.\
<pre>
cd web_ai_interface_app/
</pre>
1.  Run the application:\
<pre>
poetry run flask run
</pre>
