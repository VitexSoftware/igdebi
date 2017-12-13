# igdebi
Online package installer for Debian. 

Download package and install it using gdebi
Also can handle local files

Usage
-----

```shell
    sudo igdebi <URL>
```

![Screenshot](https://raw.githubusercontent.com/VitexSoftware/igdebi/master/igdebi.png)

Installation
------------

    wget -O - http://v.s.cz/info@vitexsoftware.cz.gpg.key|sudo apt-key add -
    echo deb http://v.s.cz/ stable main > /etc/apt/sources.list.d/ease.list
    aptitude update
    aptitude install igdebi


