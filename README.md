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

## Usage

### Starting the server

To start the server, perform the following:
```
source venv/bin/activate    # activate virtual env. if you are not currently in it
cd solution/
python rest.py
```

The server is up and running and by default listening on `127.0.0.1:8888`. The `PORT` value van be changed in the file `config.py`.

### Shutting down the server

After finishing the server run session (`ctrl/cmd + c`), virtual environment can be deactivated by simply typing
```
deactivate
```

### Response Format

All the responses are returned in `JSON` format. Sample response is presented below. Response always returns HTML code `200` and the status indicates request handling effect.

 - `status` is an integer number,
 - `rate` is a stringified decimal number with 6 precision digits.
```
{"status": 200, "rate": "4.229459"}
```

### Routing

Server handles only one url:
```
/rate/CURRENCY_FROM/CURRENCY_TO/
```
e.g.:
```
/rate/EUR/PLN/
```

All other requests will results in the following response

```
{"status": 404, "msg": "Incorrect request url."}
```

### Configuration

### Logging

## Testing
