# coding: utf-8
# Remove a specific judge entry from database
# Created by James Raphael Tiovalen (2021)

import slack
import ast
import settings
import config

from slackers.hooks import commands

conv_db = config.conv_handler


@commands.on("deletejudge")
def deletejudge(payload):

    return
