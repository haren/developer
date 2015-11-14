# Currency exchange rates

This repository contains a sample solution for the problem described [here](https://github.com/haren/developer/tree/master/specification-3).

It was written in Python 2.7, using [tornado 4.2.1](http://www.tornadoweb.org/en/stable/) as a server serving the REST requests.

## Installation and Requirements
The environment can be setup in 2 ways:

1. Using [`docker-compose`](https://docs.docker.com/compose/)
2. Using [`virtualenv`](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

Both setups are described below.

### Docker-compose

To run the app using `docker` and `docker-compose` you need them installed. Installation instructions for `docker` can be found [here](http://docs.docker.com/engine/installation/), and for `docker-compose` [here](https://docs.docker.com/compose/install/).

When both are installed, the docker image needs to be built from the defined `Dockerfile` with the following:
```
docker build .
```

The environment is now ready to run the app.

### Virtualenv

The simplest way to install `virtualenv` is with [`pip`](https://pypi.python.org/pypi/pip), python's package manager.

#### Installing `pip` on Mac OS
Using [brew](http://brew.sh/):
```
brew install pip
pip install virtualenv
```
#### Using easy_install
```
curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python # install easy_install
sudo easy_install pip
```

#### Installation on Linux
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

The app does not have much configuration, yet if any values or paths (e.g. for CSV files) need to be changed, it can be done in `config.py`.

### Logging

The application logs all important events into a time-rotating log file. The log file is structured as follows:
```
/logs/main.log/main.log
```
And is created automatically upon server start.

## Testing

Test suite has been prepared for the app. To run the test suite, make sure the test is running and perform the following:

```
cd test
python run_tests.py
```

The test process exists with an appropriate exit code so that it can be directly plugged into an e.g. continuous integration solutoin.
