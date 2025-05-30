# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class SellerProtectionStatus(object):

    """Implementation of the 'Seller Protection Status' enum.

    Indicates whether the transaction is eligible for seller protection. For
    information, see [PayPal Seller Protection for
    Merchants](https://www.paypal.com/us/webapps/mpp/security/seller-protection
    ).

    Attributes:
        ELIGIBLE: Your PayPal balance remains intact if the customer claims
            that they did not receive an item or the account holder claims
            that they did not authorize the payment.
        PARTIALLY_ELIGIBLE: Your PayPal balance remains intact if the customer
            claims that they did not receive an item.
        NOT_ELIGIBLE: This transaction is not eligible for seller protection.

    """
    ELIGIBLE = 'ELIGIBLE'

    PARTIALLY_ELIGIBLE = 'PARTIALLY_ELIGIBLE'

    NOT_ELIGIBLE = 'NOT_ELIGIBLE'

