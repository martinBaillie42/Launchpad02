# uncompyle6 version 2.9.11
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Apr  4 2017, 08:46:44) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad/__init__.py
# Compiled at: 2016-09-30 03:13:24
from Launchpad import Launchpad

def create_instance(c_instance):
    """ Creates and returns the Launchpad script """
    return Launchpad(c_instance)


from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[
                         14], model_name='Launchpad'),
       PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE, SCRIPT]),
                 outport(props=[NOTES_CC, REMOTE, SCRIPT])]
       }
# okay decompiling __init__.pyc
