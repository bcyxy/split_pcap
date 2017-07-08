#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import sys

import split_pcap
from util import get_fpaths
from util.cfg_manage import cfg_manager


def initial():
    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s [%(levelname)s] %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S',
        filename = cfg_manager.get_cfg_by_key("log_path"),
        filemode = 'w'
    )
initial()


def main(args):
    pcap_dir = args[1]
    pcap_fpath_list = get_fpaths.get_file_list(pcap_dir)
    for pcap_fpath in pcap_fpath_list:
        if not ( 
            pcap_fpath.endswith(".pcap") 
            or pcap_fpath.endswith(".pcapng") 
            or pcap_fpath.endswith(".cap")
        ):
            continue
        logging.info("[main::main] handle pcap file: '%s'" %pcap_fpath)
        if True:#try:
            split_pcap.handle_pcap(pcap_fpath)
        #except Exception, e:
        #    logging.warning("[main::main] handle pcap file error. fpath='%s', error='%s'" %(pcap_fpath, str(e)))



if __name__ == '__main__':
    main(sys.argv)

