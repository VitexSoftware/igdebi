# ![iGdebi](https://raw.githubusercontent.com/VitexSoftware/igdebi/master/igdebi.png)  igdebi 

Online package installer for Debian. 

Download package and install it using gdebi.

Also can handle local files

Usage
-----

```shell
    sudo igdebi <URL>
```

![Screenshot](https://raw.githubusercontent.com/VitexSoftware/igdebi/master/screenshot.png)

Installation
------------

```shell
    sudo apt install lsb-release wget
    echo "deb http://repo.vitexsoftware.cz $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/vitexsoftware.list
    sudo wget -O /etc/apt/trusted.gpg.d/vitexsoftware.gpg http://repo.vitexsoftware.cz/keyring.gpg
    apt update
    apt install igdebi
```

Build
-----

we use stadard debian devscripts:

```shell
debuild -i -us -uc -b
```


Dependencies
------------

For URL recoginsation we use https://pypi.python.org/pypi/validators
debian package source is https://github.com/VitexSoftware/python-validators.deb
all other dependencies are already in debian repos.


