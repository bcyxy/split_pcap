#! /usr/bin/python
# -*- coding:utf-8 -*-

################################################################################
# auto: yuxiaoyang
################################################################################

import os
import sys

def get_file_list(dir_name):
    file_list = []
    if os.path.isfile(dir_name):
        file_list.append(dir_name)
        return file_list

    for f_d in os.listdir(dir_name):
        new_dir=os.path.join(dir_name,f_d)
        file_list += get_file_list(new_dir)

    return file_list


