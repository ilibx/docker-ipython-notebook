#!/usr/bin/env python

import fileinput
import os
import re
from subprocess import call

from IPython.lib import passwd

def check_update_password():
    password_file = '/ipython/password'
    search_string = 'c.NotebookApp.password'
    search_regex = '^' + search_string + '.*'
    destination = os.getenv('HOME', '/home/ipython') \
            + '/.ipython/profile_default/ipython_notebook_config.py'
    replaced = False

    if os.path.isfile(password_file):
        password = passwd(open(password_file, 'r').read().strip('\n'))

        for line in fileinput.input(destination, inplace=True):
            if re.search(search_regex, line):
                print search_string + " =u'" + password + "'"
                replaced = True
            else:
                print line
        if not replaced:
            with open(destination, "a") as dst:
                dst.write(search_string + " =u'" + password + "'")

def consider_certificate_and_start():
    cert_file = '/ipython/certificate.pem'
    if os.path.isfile(cert_file):
        call(["/usr/local/bin/ipython", "notebook", \
                "--certfile=" + cert_file, "--ip=*"])
    else:
        call(["/usr/local/bin/ipython", "notebook", "--ip=*"])

if __name__ == '__main__':
    check_update_password()
    consider_certificate_and_start()
