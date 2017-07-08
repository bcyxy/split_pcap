#!/usr/bin/env python
# -*- coding:utf-8 -*-
import commands
import dpkt
import hashlib
import logging
import os
import socket
import re

from kernel.protocol_analyzer import pro_analyzer


l5_dict = {}

# 处理pcap文件中的单个报文
http_cache_control_reg = re.compile(r'Cache-Control:([^\n]+)\n')
def handle_pkt(pkt_data, timestamp, **kwargs):
    try:
        ana_rst = pro_analyzer.analyze_pkt(pkt_data)
    except:
        return
    (src_ip, src_port, dst_ip, dst_port, tr_pro) = ana_rst
    if (
        src_ip == None or src_port == None 
        or dst_ip == None or dst_port == None 
        or tr_pro == None
    ):
        return
    src_ip_str = socket.inet_ntoa(src_ip)
    dst_ip_str = socket.inet_ntoa(dst_ip)
    
    if src_ip > dst_ip:
        l5_str = (
            "%s_%s_%s_%s_%s" 
            %(src_ip_str, src_port, dst_ip_str, dst_port, tr_pro)
        )
    else:
        l5_str = (
            "%s_%s_%s_%s_%s" 
            %(dst_ip_str, dst_port, src_ip_str, src_port, tr_pro)
        )
    
    pkt_list = l5_dict.get(l5_str, None)
    if pkt_list == None:
        l5_dict[l5_str] = [(timestamp, pkt_data)]
    else:
        l5_dict[l5_str].append((timestamp, pkt_data))
    

# 判断是否是pcapng文件
def judge_pcapng(pcap_fpath):
    f_ih = open(pcap_fpath, 'rb')
    first_line = ""
    for line in f_ih:
        first_line = line.strip()
        break
    f_ih.close()
    if first_line == "":
        return True
    else:
        return False
    
    
# 处理pcap文件
def handle_pcap(pcap_fpath):
    f_rh = open(pcap_fpath, 'rb')

    # 初始化Reader
    if judge_pcapng(pcap_fpath):
        pcap_rh = dpkt.pcapng.Reader(f_rh)
    else:
        pcap_rh = dpkt.pcap.Reader(f_rh)

    # 遍历单个报文
    for (timestamp, pkt_data) in pcap_rh:
        handle_pkt(timestamp=timestamp, pkt_data=pkt_data)
    f_rh.close()
    
    # 输出结果
    for (l5_str, pkt_list) in l5_dict.items():
        output_path = "data/%s.pcap" %(l5_str)
        f_oh = open(output_path, "w")
        dpkt_oh = dpkt.pcap.Writer(f_oh)
        for pkt_data in pkt_list:
            dpkt_oh.writepkt(pkt=pkt_data[1], ts=pkt_data[0])
        dpkt_oh.close()
        f_oh.close()

