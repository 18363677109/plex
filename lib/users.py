#*********************************************************************
# content   = set und get user data
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

# why users? because user is already taken by python

import os
import sys

import libLog
import libData

TITLE = os.path.splitext(os.path.basename(__file__))[0]
LOG   = libLog.init(script=TITLE)

class User:
    def __init__(self, user_id, name = '', birth = '', task = {}, position = '', settings = {}, rights = 'artist'):
        self.id       = user_id         # arichter
        self.initial  = self.id[0:2]    #  ar
        self.name     = name            # Alexander Richter

        self.birth    = birth           # 06.10.1986
        self.task     = task            # {'LIGHT': [110, 120]}

        self.position = position        # Pipeline
        self.settings = settings        # {'arLoad': []}

        self.rights   = rights          # admin, artist

    def __call__(self):
        return (self.id, ': ',  self.name,
                '\nBirth: ',    self.birth,
                '\nTask: ',     self.task,
                '\nPosition: ', self.position,
                '\nSettings: ', self.settings)


    #************************
    # VARIABLES
    @property
    def id(self):
        return self.id

    @property
    def initial(self):
        return self.initial

    @property
    def name(self):
        return self.name

    @property
    def rights(self):
        return self.rights


    #************************
    # EXTRAS
    @property
    def data_path(self):
        return "data_path"

    @property
    def user_path(self):
        return "user_path"

    @property
    def local_path(self):
        return "local_path"

    @property
    def is_admin(self):
        return True if self.rights == 'admin' else False


    #************************
    # FUNCTIONS
    def read_data(self):
        libData.setData()

    def write_data(self, scriptSettings):
        currentChange = self.read_user()
        currentChange.__dict__["settings"].update(scriptSettings)
        setUser(currentChange)

    def delete_data(self):
        deletePath = os.path.join(DATA.PATH['data_user'], self.id)
        if os.path.exists(deletePath):
            LOG.info("DONE : " + self.id + " removed")
            os.remove(deletePath)
        else:
            LOG.info("FAIL : " + self.id + " - user doesnt exists")

