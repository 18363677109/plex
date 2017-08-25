#*********************************************************************
# content   = create, search etc in/for file and folders
# version   = 0.1.0
# date      = 2017-07-30
#
# license   = MIT
# copyright = Copyright 2017 Animationsinstitut
# author    = Alexander Richter <pipeline@richteralexander.com>
#*********************************************************************
# This source file has been developed within the scope of the
# Technical Director course at Filmakademie Baden-Wuerttemberg.
# http://td.animationsinstitut.de
#*********************************************************************

import os
import glob
import logging
import webbrowser

import libLog

TITLE = os.path.splitext(os.path.basename(__file__))[0]
LOG   = libLog.init(script=TITLE)

#************************
# FOLDER
# @BRIEF  creates a folder, checks if it already exists,
#         creates the folder above if the path is a file
def create_folder(path):
    if len(path.split('.')) > 1: path = os.path.dirname(path)
    if not os.path.exists(path):
        try:    os.makedirs(path)
        except: LOG.warning('CANT create folder: {}'.format(path))

# @BRIEF  opens folder even if file is given
def open_folder(path):
    path = os.path.normpath(path)
    if os.path.exists(path):
        if len(path.split('.')) > 1: path = os.path.dirname(path)
        webbrowser.open(path)
    else: LOG.warning('UNVALID path: {}'.format(path))
    return path


#************************
# FILES
# @BRIEF  get a file/folder list with specifics
#
# @PARAM  path string.
#         file_type string/string[]. '*.py'
#         extension bool. True:[name.py] False:[name]
#         exclude string /string[]. '__init__.py' | '__init__' | ['btnReport48', 'btnHelp48']
#
# @RETURN strint[].
def get_file_list(path, file_type='*', extension=False, exclude='*', add_path = False):
    if(os.path.exists(path)):
        getFile = []
        os.chdir(path)
        for file_name in glob.glob(file_type):
            if exclude in file_name: continue
            if add_path:  file_name = os.path.normpath(('/').join([path,file_name]))
            if extension: getFile.append(file_name)
            else:         getFile.append((file_name.split('.')[0]))
        return getFile

##
# @BRIEF  GET ALL subfolders in the path
def get_deep_folder_list(path, add_path=False):
    if add_path: getFile = map(lambda x: x[0], os.walk(path))
    else:        getFile = map(lambda x: os.path.basename(x[0]), os.walk(path))

    try:    getFile.pop(0)
    except: LOG.error('CANT pop file. Path: {}'.format(path), exc_info=True)

    return getFile


#************************
# TEMP IMAGE
def rm_tmp_img():
    tmpImgPath = 'C:/temp/tmp.png'  #temp user place (os independent)
    if os.path.exists(tmpImgPath):
        try:    os.remove(tmpImgPath)
        except: LOG.error('FAIL : cant delete tmpFile : ' + tmpImgPath, exc_info=True)
    return tmpImgPath
