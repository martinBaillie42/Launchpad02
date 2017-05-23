# uncompyle6 version 2.9.11
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Apr  4 2017, 08:46:44) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad/SpecialMixerComponent.py
# Compiled at: 2016-09-30 03:13:24
import Live
from _Framework.MixerComponent import MixerComponent
from DefChannelStripComponent import DefChannelStripComponent
from _Framework.ButtonElement import ButtonElement

class SpecialMixerComponent(MixerComponent):
    """ Class encompassing several defaultable channel strips to form a mixer """

    def __init__(self, num_tracks, num_returns=0):
        MixerComponent.__init__(self, num_tracks, num_returns)
        self._unarm_all_button = None
        self._unsolo_all_button = None
        self._unmute_all_button = None
        return

    def disconnect(self):
        if self._unarm_all_button != None:
            self._unarm_all_button.remove_value_listener(self._unarm_all_value)
            self._unarm_all_button = None
        if self._unsolo_all_button != None:
            self._unsolo_all_button.remove_value_listener(self._unsolo_all_value)
            self._unsolo_all_button = None
        if self._unmute_all_button != None:
            self._unmute_all_button.remove_value_listener(self._unmute_all_value)
            self._unmute_all_button = None
        MixerComponent.disconnect(self)
        return

    def set_global_buttons(self, unarm_all, unsolo_all, unmute_all):
        assert isinstance(unarm_all, (ButtonElement, type(None)))
        assert isinstance(unsolo_all, (ButtonElement, type(None)))
        assert isinstance(unmute_all, (ButtonElement, type(None)))
        if self._unarm_all_button != None:
            self._unarm_all_button.remove_value_listener(self._unarm_all_value)
        self._unarm_all_button = unarm_all
        if self._unarm_all_button != None:
            self._unarm_all_button.add_value_listener(self._unarm_all_value)
            self._unarm_all_button.turn_off()
        if self._unsolo_all_button != None:
            self._unsolo_all_button.remove_value_listener(self._unsolo_all_value)
        self._unsolo_all_button = unsolo_all
        if self._unsolo_all_button != None:
            self._unsolo_all_button.add_value_listener(self._unsolo_all_value)
            self._unsolo_all_button.turn_off()
        if self._unmute_all_button != None:
            self._unmute_all_button.remove_value_listener(self._unmute_all_value)
        self._unmute_all_button = unmute_all
        if self._unmute_all_button != None:
            self._unmute_all_button.add_value_listener(self._unmute_all_value)
            self._unmute_all_button.turn_off()
        return

    def _create_strip(self):
        return DefChannelStripComponent()

    def _unarm_all_value(self, value):
        assert self.is_enabled()
        assert self._unarm_all_button != None
        assert value in range(128)
        if value != 0 or not self._unarm_all_button.is_momentary():
            for track in self.song().tracks:
                if track.can_be_armed and track.arm:
                    track.arm = False

        return

    def _unsolo_all_value(self, value):
        assert self.is_enabled()
        assert self._unsolo_all_button != None
        assert value in range(128)
        if value != 0 or not self._unsolo_all_button.is_momentary():
            for track in tuple(self.song().tracks) + tuple(self.song().return_tracks):
                if track.solo:
                    track.solo = False

        return

    def _unmute_all_value(self, value):
        assert self.is_enabled()
        assert self._unmute_all_button != None
        assert value in range(128)
        if value != 0 or not self._unmute_all_button.is_momentary():
            for track in tuple(self.song().tracks) + tuple(self.song().return_tracks):
                if track.mute:
                    track.mute = False

        return
# okay decompiling SpecialMixerComponent.pyc
