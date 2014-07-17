# ipython notebook

This is the build I use to study for the "Machine Learning" course of Andrew Ng at Coursera.
It basically covers everything you need, since it is possible to use octave code in the notebooks via the "octavemagic" extension and the magic function "%%octave".
It's sometimes a bit hard to debug in ipython notebook, because all the code in a cell is basically an argument for the octave function but it's nice to save progress, write some notes and plot some data.

This installation is a bit bloated (no --no-install-recommends for apt-get) but covers numpy, scipy, matplotlib, octave and ipython-notebook for a prompt start.

## Installation

```
docker pull temal/ipython-notebook:latest
```

There are two ways to run the container. 


## Usage

### Data consistent

**RECOMMENDED WAY**

Data is saved in a directory specified by you. Before you start the container you have the possibility to set a password and a SSL certificate.

Lets say, for example, you have a directory on you host at /exported/ipython which you want to use in the container.

To use a password [optional]:

```
echo "YOURPASSWORDHERE" > /exported/ipython/password
```

To use a SSL certificate (self signed) [optional]:

```
openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 -subj "/C=0O/ST=CHANGEME/L=CHANGEME/O=CHANGEME/CN=CHANGEME" -keyout /exported/ipython/certificate.pem -out /exported/ipython/certificate.pem
```


After the above steps, you can start the container with:

```
docker run -dp 8000:8888 -v /exported/ipython:/ipython temal/ipython-notebook
```

### Data-inconsistent

**UNSAFE**

No data is saved, no password is set and no SSL certificate is provided!
For quick fun:

```
docker run -dp 8000:8888 temal/ipython-notebook
```
