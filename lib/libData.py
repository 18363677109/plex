#*********************************************************************
# content   = get and set data files for project and user
# version   = 0.0.1
# date      = 2017-01-01
#
# license   = MIT
# copyright = Copyright 2017 Filmakademie Baden-Wuerttemberg, Animationsinstitut
# author    = Alexander Richter <contact@richteralexander.com>
#*********************************************************************
# This source file has been developed within the scope of the
# Technical Director course at Filmakademie Baden-Wuerttemberg.
# http://td.animationsinstitut.de
#*********************************************************************

import os
import json
import yaml

import libLog
import libFileFolder

TITLE = os.path.splitext(os.path.basename(__file__))[0]
LOG   = libLog.init(script=TITLE)

DATA_FORMAT = '.yml'
IMG_FORMAT  = '.png'

# TODO: user_id with user class - see also below
def get_data(file_name = '', user_id = os.getenv('username')):

    def get_all_data():
        config_data        = {}
        data_user_files    = libFileFolder.getFileList(path = get_env('DATA_USER_PATH'),    file_type = '*' + DATA_FORMAT)
        data_project_files = libFileFolder.getFileList(path = get_env('DATA_PROJECT_PATH'), file_type = '*' + DATA_FORMAT)

        data_project_files = list(set(data_user_files)|set(data_project_files))
        for each_file in data_project_files: config_data.update({each_file : get_data(each_file, user_id)})
        return config_data

    if not file_name:
        return get_all_data()

    file_name = file_name.split('.')[0]
    file_path = ''

    if user_id:
        file_path = os.path.normpath(('/').join([get_env('DATA_USER_PATH'), file_name + DATA_FORMAT]))

    if not os.path.exists(file_path):
        file_path = os.path.normpath(('/').join([get_env('DATA_PROJECT_PATH'), file_name + DATA_FORMAT]))

    # OPEN data path
    if os.path.exists(file_path):
        # LOG.debug(file_path)
        return get_yml_file(file_path)
    else:
        LOG.warning('CANT find file: {}'.format(file_path))
    return ''

def set_data(file_name, var, data):
    print('set_data')
    # set_yml_file


#************************
# GET PATH
def get_pipeline_path(end_path):
    pipeline_path = os.environ.get('PIPELINE_PATH', '')
    if pipeline_path:
        pipeline_path = pipeline_path.split(';')
        # find first fitting path
        for eachPath in pipeline_path:
            path = os.path.normpath(('/').join([eachPath,end_path]))

            if os.path.exists(path):
                # LOG.debug('PATH exists: {0}'.format(path))
                return path

    LOG.warning('PATH doesnt exists: {}'.format(path))
    return ''

def get_project_path(end_path = ''):
    project_path = os.environ.get('PROJECT_PATH', '')
    project_path = os.path.normpath(('/').join([project_path, end_path]))

    if os.path.exists(project_path):
        return project_path

    LOG.critical('PATH doesnt exist: {}'.format(project_path))
    return ''

def get_project_user_path(user = os.getenv('username')):
    project_user_path = get_data('Path')['PROJECT_PATH']['user']
    return get_project_path(('/').join([project_user_path, user]))

def get_img_path(end_path = 'btn/default'):
    path = get_pipeline_path('img/' + end_path + IMG_FORMAT)
    if not path:
        path = get_img_path(('/').join([os.path.dirname(end_path), 'default']))
    return path


#************************
# YAML
def set_yml_file(path, content):
    print 'set YAML file'


def get_yml_file(path):
    with open(path, 'r') as stream:
        try:
            pipeline_path = yaml.load(stream)
            if pipeline_path:
                return pipeline_path
            else:
                LOG.warning('CANT load fiel: {}'.format(path))
        except yaml.YAMLError as exc:
            LOG.error(exc, exc_info=True)





# @BRIEF  creates or add enviroment variable
#
# @PARAM  STRING var, STRING content
def add_env(var, content):
    if os.environ.__contains__(var):
        os.environ[var] += ('').join([content, ';'])
    else:
        os.environ[var] = ('').join([content, ';'])
    return os.environ[var]

def get_env(var):
    if os.environ.__contains__(var):
        return os.environ[var].split(';')[0]
    LOG.warning('ENV doesnt exist: {}'.format(var))
    return ''




# import sys
# sys.path.append('D:/Dropbox/arPipeline/2000/data')
# import setEnv
# setEnv.SetEnv()

# print get_pipeline_path('img')
# print os.environ.get('PIPELINE_PATH', ')

# print get_img_path('btn/btnReport4')
