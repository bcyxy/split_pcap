# 功能
- 将抓包得到的报文文件按照<源IP, 源端口, 目的IP, 目的端口, TCP/UDP>拆分成多个文件。

# 使用:
1. 运行：sh run.sh your_pcaps_dir (例: sh run.sh /pcap/xxx/xxx/)
1. 拆分后的pcap文件放置在 “data/”目录下。
