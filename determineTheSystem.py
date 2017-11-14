#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:06:31 2017

@author: ilkay.isik
small script to determine the system/user and the directory to work on
"""

import sys
import os

myhost = os.uname()[1]

if myhost == 'nro-mac-d-016': #ilkay's
    #os.chdir('') # can add a specific directory
    os.chdir = os.getcwd() #get current directory of this python script

elif myhost == 'nro-mac-d-014': #ed's
    #os.chdir('/Users/ilkay.isik/Desktop/fmri_Localizer01')
    os.chdir= os.getcwd()  # get current directory of this python script





