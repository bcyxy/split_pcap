#!/usr/bin/env python
# -*- coding:utf-8 -*-

import dpkt


class ProtocolAnalyzer(object):
    def __init__(self):
        self.initial()

    def initial(self):
        self.src_ip = None
        self.src_port = None
        self.dst_ip = None
        self.dst_port = None
        self.tr_pro = None

    def analyze_pkt(self, pkt_data):
        self.initial()

        eth_data = dpkt.ethernet.Ethernet(pkt_data) 
        self.ethernet2(eth_data)
        
        return (self.src_ip, self.src_port, self.dst_ip, self.dst_port, self.tr_pro)

    def ethernet2(self, eth_data):
        nl_type = eth_data.type
        nl_data = eth_data.data

        if nl_type == 2048:
            self.ipv4(nl_data)
        elif nl_type == 34525:
            #self.ipv6(nl_data)
            pass
        elif nl_type == 2054:
            self.arp(nl_data)
        else:
            pass

    def ipv4(self, ipv4_data):
        src_ip = ipv4_data.src
        dst_ip = ipv4_data.dst
        nl_type = ipv4_data.p
        nl_data = ipv4_data.data
        
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        
        if nl_type == 6:
            self.tcp(nl_data)
        elif nl_type == 17:
            self.udp(nl_data)
        elif nl_type == 47:
            self.gre(nl_data)
        else:
            pass

    def ipv6(self, ipv6_data):
        src_ip = ipv6_data.src
        dst_ip = ipv6_data.dst
        nl_type = ipv6_data.p
        nl_data = ipv6_data.data

        if nl_type == 6:
            self.tcp(nl_data)
        elif nl_type == 17:
            self.udp(nl_data)
        else:
            pass

    def arp(self, arp_data):
        pass

    def tcp(self, tcp_data):
        src_port = tcp_data.sport
        dst_port = tcp_data.dport
        flags = tcp_data.flags
        nl_data = tcp_data.data

        self.tr_pro = "tcp"
        self.dst_port = dst_port
        self.src_port = src_port

    def udp(self, udp_data):
        src_port = udp_data.sport
        dst_port = udp_data.dport
        nl_data = udp_data.data
        
        self.tr_pro = "udp"
        self.dst_port = dst_port
        self.src_port = src_port
        
    def gre(self, gre_data):
        nl_type = gre_data.p
        nl_data = gre_data.data
        
        if nl_type == 2048:
            self.ipv4(nl_data)

pro_analyzer = ProtocolAnalyzer()

