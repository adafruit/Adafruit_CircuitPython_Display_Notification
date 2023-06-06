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
    # unused typing-import to prevent the other typing-only imports from being loaded at runtime
    from typing import Any  # pylint: disable=unused-import

    from adafruit_ble_apple_notification_center import Notification
except ImportError:
    pass

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Display_Notification.git"


def create_notification_widget(
    notification: Notification,
    max_width: int,
    max_height: int,
    *,
    color_count: int = 2**16
) -> PlainNotification:
    """Creates a notification widget for the given Apple notification."""
    # pylint: disable=unused-argument
    return PlainNotification(
        notification.title, notification.message, max_width, max_height
    )
