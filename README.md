# igdebi
Online package installer for Debian. 

Download package and install it using gdebi

Usage
-----

    sudo igdebi https://repo.skype.com/latest/skypeforlinux-64.deb


Installation
------------

    wget -O - http://v.s.cz/info@vitexsoftware.cz.gpg.key|sudo apt-key add -
    echo deb http://v.s.cz/ stable main > /etc/apt/sources.list.d/ease.list
    aptitude update
    aptitude install igdebi


