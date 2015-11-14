# Currency exchange rates

This repository contains a sample solution for the problem described [here](https://github.com/haren/developer/tree/master/specification-3).

It was written in Python 2.7, using [tornado 4.2.1](http://www.tornadoweb.org/en/stable/) as a server serving the REST requests.

## Installation and Requirements
The solution was prepared using [`virtualenv`](http://docs.python-guide.org/en/latest/dev/virtualenvs/). The simplest way to install it is with [`pip`](https://pypi.python.org/pypi/pip), python's package manager.

### Installation on Mac OS
#### Using [brew](http://brew.sh/):
```
brew install pip
pip install virtualenv
```
#### Using easy_install
```
curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python # install easy_install
sudo easy_install pip
```

### Installation on Linux
Depending on your distribution, you can get `pip` using one of the following:
```
sudo apt-get install python-pip

sudo yum install python-pip
```
When `pip` is installed, virtual environment for this project needs to be created. Perform the following:
```
pip install virtualenv
cd $my_project_folder
virtualenv venv             # create virtual env. 
source venv/bin/activate    # activate virtual env., puts you inside
pip install -r requirements # installs all requirements for the project
```

After finishing the server run session, virtual environment can be deactivated by simply typing
```
deactivate
```

## Usage

### Starting the server

### Response Format

### Routing

### Configuration

### Logging

## Testing
