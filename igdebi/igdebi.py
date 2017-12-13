#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import requests
import sys
from tqdm import tqdm
from urllib.parse import urlparse
import validators

def main():
    if len(sys.argv) < 2:
        print ('Usage: igdebi < url or path to packgage>')
        print 
    else:
        argument = sys.argv[1]
        if validators.url(argument):
            a = urlparse(argument)
            debfile = os.path.basename(a.path)
            r = requests.get(argument, stream=True)
            total_size = int(r.headers.get('content-length', 0)); 
            with open(debfile, 'wb') as f:
                for data in tqdm(r.iter_content(32 * 1024), total=total_size, unit='B', unit_scale=True):
                    f.write(data)
        else:
            if(os.path.isfile(argument)):
                debfile = argument
            else:
                print ("Not such file " + argument)
                debfile = ""
        if(len(debfile)):
            os.system('gdebi ' + debfile)
            os.remove(debfile)
        