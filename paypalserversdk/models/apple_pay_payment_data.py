# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper


class ApplePayPaymentData(object):

    """Implementation of the 'Apple Pay Payment Data' model.

    Information about the decrypted apple pay payment data for the token like
    cryptogram, eci indicator.

    Attributes:
        cryptogram (str): Online payment cryptogram, as defined by 3D Secure.
            The pattern is defined by an external party and supports Unicode.
        eci_indicator (str): ECI indicator, as defined by 3- Secure. The
            pattern is defined by an external party and supports Unicode.
        emv_data (str): Encoded Apple Pay EMV Payment Structure used for
            payments in China. The pattern is defined by an external party and
            supports Unicode.
        pin (str): Bank Key encrypted Apple Pay PIN. The pattern is defined by
            an external party and supports Unicode.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cryptogram": 'cryptogram',
        "eci_indicator": 'eci_indicator',
        "emv_data": 'emv_data',
        "pin": 'pin'
    }

    _optionals = [
        'cryptogram',
        'eci_indicator',
        'emv_data',
        'pin',
    ]

    def __init__(self,
                 cryptogram=APIHelper.SKIP,
                 eci_indicator=APIHelper.SKIP,
                 emv_data=APIHelper.SKIP,
                 pin=APIHelper.SKIP):
        """Constructor for the ApplePayPaymentData class"""

        # Initialize members of the class
        if cryptogram is not APIHelper.SKIP:
            self.cryptogram = cryptogram 
        if eci_indicator is not APIHelper.SKIP:
            self.eci_indicator = eci_indicator 
        if emv_data is not APIHelper.SKIP:
            self.emv_data = emv_data 
        if pin is not APIHelper.SKIP:
            self.pin = pin 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        cryptogram = dictionary.get("cryptogram") if dictionary.get("cryptogram") else APIHelper.SKIP
        eci_indicator = dictionary.get("eci_indicator") if dictionary.get("eci_indicator") else APIHelper.SKIP
        emv_data = dictionary.get("emv_data") if dictionary.get("emv_data") else APIHelper.SKIP
        pin = dictionary.get("pin") if dictionary.get("pin") else APIHelper.SKIP
        # Return an object of this model
        return cls(cryptogram,
                   eci_indicator,
                   emv_data,
                   pin)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'cryptogram={(self.cryptogram if hasattr(self, "cryptogram") else None)!r}, '
                f'eci_indicator={(self.eci_indicator if hasattr(self, "eci_indicator") else None)!r}, '
                f'emv_data={(self.emv_data if hasattr(self, "emv_data") else None)!r}, '
                f'pin={(self.pin if hasattr(self, "pin") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'cryptogram={(self.cryptogram if hasattr(self, "cryptogram") else None)!s}, '
                f'eci_indicator={(self.eci_indicator if hasattr(self, "eci_indicator") else None)!s}, '
                f'emv_data={(self.emv_data if hasattr(self, "emv_data") else None)!s}, '
                f'pin={(self.pin if hasattr(self, "pin") else None)!s})')
