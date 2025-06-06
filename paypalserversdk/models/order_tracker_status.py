# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class OrderTrackerStatus(object):

    """Implementation of the 'Order Tracker Status' enum.

    The status of the item shipment.

    Attributes:
        CANCELLED: The shipment was cancelled and the tracking number no
            longer applies.
        SHIPPED: The merchant has assigned a tracking number to the items
            being shipped from the Order. This does not correspond to the
            carrier's actual status for the shipment. The latest status of the
            parcel must be retrieved from the carrier.

    """
    CANCELLED = 'CANCELLED'

    SHIPPED = 'SHIPPED'

