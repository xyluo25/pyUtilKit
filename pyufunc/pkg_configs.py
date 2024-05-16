# -*- coding:utf-8 -*-
##############################################################
# Created Date: Sunday, July 9th 2023
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################
from __future__ import absolute_import
import os
from pyufunc.util_pathio._path import path2linux

__all__ = [
    "pkg_version",
    "pkg_name",
    "pkg_author",
    "pkg_email",
    "config_FUNC_KEYWORD",
    "config_logging",
    "config_datetime_fmt",
    "config_email",
    "config_gmns",
]

# ############## Package Configurations ############## #
pkg_version = "0.2.6"
pkg_name = "pyufunc"
pkg_author = "Mr. Xiangyong Luo, Dr. Xuesong Simon Zhou"
pkg_email = "luoxiangyong01@gmail.com, xzhou74@asu.edu"

# ############### Function Keywords Configuration ############### #
config_FUNC_KEYWORD = {
    "non-keywords": [],
    "show"        : [],
    "get"         : [],
    "generate"    : [],
    "create"      : [],
    "find"        : [],
    "calc"        : [],
    "run"         : [],
    "group"       : [],
    "check"       : [],
    "validate"    : [],
    "list"        : [],
    "img"         : [],
    "split"       : [],
    "fmt"         : [],
    "cvt"         : [],
    "is"          : [],
    "proj"        : [],
    "github"      : [],
    "pypi"        : [],
    "error"       : [],
    "algo"        : [],
}


# ############## Logging Configurations ############## #
config_logging = {
    # system logging
    "is_log": True,

    # logging default folder
    "log_folder": path2linux(os.path.join(os.getcwd(), "syslogs")),

    # logging
    "log_level": "DEBUG",

    # default log format
    "log_fmt": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",

    # default log date format
    "log_datefmt": "%Y-%m-%d %H:%M:%S",
}

# ############### Date Time Format Configuration ############### #
config_datetime_fmt = {

    # 0 "YYYY-MM-DD", 2023-07-09
    # 1 "YYYY-MM-DD HH:MM:SS", 2023-07-09 11:11:11
    # 2 "YYYY-MM-DD HH:MM:SS.MS", 2023-07-09 11:11:11.123456
    0 : "%Y-%m-%d",
    1 : "%Y-%m-%d %H:%M:%S",
    2 : "%Y-%m-%d %H:%M:%S.%f",

    # 3 "YYYY/MM/DD", 2023/07/09
    # 4 "YYYY/MM/DD HH:MM:SS", 2023/07/09 11:11:11
    # 5 "YYYY/MM/DD HH:MM:SS.MS", 2023/07/09 11:11:11.123456
    3: "%Y/%m/%d",
    4: "%Y/%m/%d %H:%M:%S",
    5: "%Y/%m/%d %H:%M:%S.%f",

    # 6 "MM/DD/YYYY", 07/09/2023
    # 7 "MM/DD/YYYY HH:MM:SS", 07/09/2023 11:11:11
    # 8 "MM/DD/YYYY HH:MM:SS.MS", 07/09/2023 11:11:11.123456
    6 : "%m/%d/%Y",
    7 : "%m/%d/%Y %H:%M:%S",
    8 : "%m/%d/%Y %H:%M:%S.%f",

    # 9 "DD/MM/YYYY", 09/07/2023
    # 10 "DD/MM/YYYY HH:MM:SS", 09/07/2023 11:11:11
    # 11 "DD/MM/YYYY HH:MM:SS.MS", 09/07/2023 11:11:11.123456
    9 : "%d/%m/%Y",
    10 : "%d/%m/%Y %H:%M:%S",
    11 : "%d/%m/%Y %H:%M:%S.%f",

    # 12 "HH:MM:SS", 11:11:11
    # 13 "HH:MM:SS.MS", 11:11:11.123456
    12 : "%H:%M:%S",  # "HH:MM:SS", 11:11:11
    13 : "%H:%M:%S.%f",  # "HH:MM:SS.MS", 11:11:11.123456

    14: "%m-%d-%Y",  # "MM-DD-YYYY", 07-09-2023
    15: "%m-%d-%Y %H:%M:%S",  # "MM-DD-YYYY HH:MM:SS", 07-09-2023 11:11:11
    16: "%m-%d-%Y %H:%M:%S.%f",  # "MM-DD-YYYY HH:MM:SS.MS", 07-09-2023 11:11:11.123456

    17: "%d-%m-%Y",  # "DD-MM-YYYY", 09-07-2023
    18: "%d-%m-%Y %H:%M:%S",  # "DD-MM-YYYY HH:MM:SS", 09-07-2023 11:11:11
    19: "%d-%m-%Y %H:%M:%S.%f",  # "DD-MM-YYYY HH:MM:SS.MS", 09-07-2023 11:11:11.123456

    29: "%Y-%m",  # "YYYY-MM", 2023-07
    30: "%Y/%m",  # "YYYY/MM", 2023/07
    31: "%m/%Y",  # "MM/YYYY", 07/2023
    32: "%m-%Y",  # "MM-YYYY", 07-2023

}

# ############### Email Configuration ############### #
config_email = {
    'gmail.com': {
        'smtp': ('smtp.gmail.com', 587),
        'pop3': ('pop.gmail.com', 995)},
    'office365.com': {
        'smtp': ('smtp.office365.com', 587),
        'pop3': ('outlook.office365.com', 995)},
    'outlook.com': {
        'smtp': ('smtp-mail.outlook.com', 587),
        'pop3': ('outlook.office365.com', 995)},
    'yahoo.com': {
        'smtp': ('smtp.mail.yahoo.com', 587),
        'pop3': ('pop.mail.yahoo.com', 995)},
    'hotmail.com': {
        'smtp': ('smtp-mail.outlook.com', 587),
        'pop3': ('outlook.office365.com', 995)},
    'aol.com': {
        'smtp': ('smtp.aol.com', 587),
        'pop3': ('pop.aol.com', 995)},
    'protonmail.com': {
        'smtp': ('smtp.protonmail.com', 465),
        'pop3': None},  # ProtonMail does not offer POP3 access
    'zoho.com': {
        'smtp': ('smtp.zoho.com', 587),
        'pop3': ('pop.zoho.com', 995)},
    'fastmail.com': {
        'smtp': ('smtp.fastmail.com', 587),
        'pop3': ('mail.messagingengine.com', 995)},
    'qq.com': {
        'smtp': ('smtp.qq.com', 587),
        'pop3': ('pop.qq.com', 995)},
    '163.com': {
        'smtp': ('smtp.163.com', 465),
        'pop3': ('pop.163.com', 995)},
    'asu.edu': {
        'smtp': ('smtp.gmail.edu', 587),
        'pop3': ('pop.gmail.edu', 995)},
}

# ############### GMNS: General Modeling Network Specification configuration #
config_gmns = {
    # specify required fields for node.csv and poi.csv and zone.csv (optional)
    "node_required_fields": ["node_id", "x_coord", "y_coord",
                             "activity_type", "is_boundary", "poi_id"],
    "poi_required_fields": ["poi_id", "building", "centroid", "area", "geometry"],
    "link_required_fields": ["link_id", "from_node_id", "to_node_id", "length", "lanes"],
}
