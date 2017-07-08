#! /usr/bin/python
# -*- coding:utf-8 -*-

import ConfigParser

class CfgManager(object):
    def __init__(self):
        self.cfg_parser = ConfigParser.ConfigParser()
        self.cfg_parser.read("./glb.cfg")

    def get_cfg_by_key(self, cfg_key):
        return self.cfg_parser.get("glb", cfg_key)


cfg_manager = CfgManager()

