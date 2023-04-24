# SPDX-FileCopyrightText: 2019 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_display_notification.apple`
================================================================================

Maps Apple Notification Center Notification objects to the notification widgets
in this library.

"""

from . import PlainNotification

try:
    from typing import Union
except ImportError:
    pass

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Display_Notification.git"


def create_notification_widget(
    notification: object, max_width: Union[int, float], max_height: Union[int, float], 
    *, color_count: int=2**16):
    """
        Creates a notification widget for the given Apple notification.
        :param notification object: Object with attributes title and message
        :param max_width int: Max Width of the notification
        :param max_height int: Max Height of the Notication 
        :param color_count int: Number of colors, default is 2**16
    
    """
    # pylint: disable=unused-argument
    return PlainNotification(
        notification.title, notification.message, max_width, max_height
    )
