#!/usr/bin/env python
#_*_coding:utf-8 _*_
import subprocess
def func_uname():
    uname = "uname"
    uname_arg = "-a"
    print "Gathering system information with %s command \n" % uname
    subprocess.call([uname,uname_arg])
def func_disk_info():
    disk_info = "df"
    disk_info_arg = "-h"
    print "Gathering disk information with %s command \n" % disk_info
    subprocess.call([disk_info,disk_info_arg])
def main():
    func_uname()
    func_disk_info()
main()