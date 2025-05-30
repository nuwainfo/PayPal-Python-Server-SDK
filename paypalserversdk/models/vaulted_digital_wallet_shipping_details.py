# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.address import Address
from paypalserversdk.models.phone_number_with_country_code import PhoneNumberWithCountryCode
from paypalserversdk.models.shipping_name import ShippingName


class VaultedDigitalWalletShippingDetails(object):

    """Implementation of the 'Vaulted Digital Wallet Shipping Details' model.

    The shipping details.

    Attributes:
        name (ShippingName): The name of the party.
        phone_number (PhoneNumberWithCountryCode): The phone number, in its
            canonical international [E.164 numbering plan
            format](https://www.itu.int/rec/T-REC-E.164/en).
        mtype (FulfillmentType): A classification for the method of purchase
            fulfillment (e.g shipping, in-store pickup, etc). Either `type` or
            `options` may be present, but not both.
        address (Address): The portable international postal address. Maps to
            [AddressValidationMetadata](https://github.com/googlei18n/libaddres
            sinput/wiki/AddressValidationMetadata) and HTML 5.1 [Autofilling
            form controls: the autocomplete
            attribute](https://www.w3.org/TR/html51/sec-forms.html#autofilling-
            form-controls-the-autocomplete-attribute).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "phone_number": 'phone_number',
        "mtype": 'type',
        "address": 'address'
    }

    _optionals = [
        'name',
        'phone_number',
        'mtype',
        'address',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 phone_number=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 address=APIHelper.SKIP):
        """Constructor for the VaultedDigitalWalletShippingDetails class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if phone_number is not APIHelper.SKIP:
            self.phone_number = phone_number 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if address is not APIHelper.SKIP:
            self.address = address 

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
        name = ShippingName.from_dictionary(dictionary.get('name')) if 'name' in dictionary.keys() else APIHelper.SKIP
        phone_number = PhoneNumberWithCountryCode.from_dictionary(dictionary.get('phone_number')) if 'phone_number' in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        address = Address.from_dictionary(dictionary.get('address')) if 'address' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   phone_number,
                   mtype,
                   address)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'phone_number={(self.phone_number if hasattr(self, "phone_number") else None)!r}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!r}, '
                f'address={(self.address if hasattr(self, "address") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'phone_number={(self.phone_number if hasattr(self, "phone_number") else None)!s}, '
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!s}, '
                f'address={(self.address if hasattr(self, "address") else None)!s})')
