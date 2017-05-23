# uncompyle6 version 2.9.11
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Apr  4 2017, 08:46:44) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad/SpecialSessionComponent.py
# Compiled at: 2016-09-30 03:13:24
from _Framework.SessionComponent import SessionComponent

class SpecialSessionComponent(SessionComponent):
    """ Special session subclass that handles ConfigurableButtons """

    def _update_stop_clips_led(self, index):
        if self.is_enabled() and self._stop_track_clip_buttons != None and index < len(self._stop_track_clip_buttons):
            button = self._stop_track_clip_buttons[index]
            tracks_to_use = self.tracks_to_use()
            track_index = index + self.track_offset()
            if 0 <= track_index < len(tracks_to_use):
                track = tracks_to_use[track_index]
                if track.fired_slot_index == -2:
                    button.send_value(self._stop_clip_triggered_value)
                elif track.playing_slot_index >= 0:
                    button.send_value(self._stop_clip_value)
                else:
                    button.turn_off()
            else:
                button.send_value(4)
        return
# okay decompiling SpecialSessionComponent.pyc
