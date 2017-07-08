#!/usr/bin/env python
# -*- coding:utf-8 -*-

class TcpStream(object):
    def __init__(self):
        self.make_conn3pkts = []
        self.tr_pkts = []
        self.disconn_pkts = []


class TcpStreamPool(object):
    def __init__(self):
        # {五元组: TcpStream}
        self.stream_pool = {}

tcp_stream_pool = TcpStreamPool()

