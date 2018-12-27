# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Security(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'company_id': 'str',
        'name': 'str',
        'type': 'str',
        'code': 'str',
        'share_class': 'str',
        'currency': 'str',
        'round_lot_size': 'float',
        'ticker': 'str',
        'exchange_ticker': 'str',
        'composite_ticker': 'str',
        'alternate_tickers': 'list[str]',
        'figi': 'str',
        'cik': 'str',
        'composite_figi': 'str',
        'share_class_figi': 'str',
        'figi_uniqueid': 'str',
        'active': 'bool',
        'etf': 'bool',
        'delisted': 'bool',
        'primary_listing': 'bool',
        'primary_security': 'bool',
        'first_stock_price': 'date',
        'last_stock_price': 'date',
        'last_stock_price_adjustment': 'date',
        'last_corporate_action': 'date',
        'previous_tickers': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'company_id': 'company_id',
        'name': 'name',
        'type': 'type',
        'code': 'code',
        'share_class': 'share_class',
        'currency': 'currency',
        'round_lot_size': 'round_lot_size',
        'ticker': 'ticker',
        'exchange_ticker': 'exchange_ticker',
        'composite_ticker': 'composite_ticker',
        'alternate_tickers': 'alternate_tickers',
        'figi': 'figi',
        'cik': 'cik',
        'composite_figi': 'composite_figi',
        'share_class_figi': 'share_class_figi',
        'figi_uniqueid': 'figi_uniqueid',
        'active': 'active',
        'etf': 'etf',
        'delisted': 'delisted',
        'primary_listing': 'primary_listing',
        'primary_security': 'primary_security',
        'first_stock_price': 'first_stock_price',
        'last_stock_price': 'last_stock_price',
        'last_stock_price_adjustment': 'last_stock_price_adjustment',
        'last_corporate_action': 'last_corporate_action',
        'previous_tickers': 'previous_tickers'
    }

    def __init__(self, id=None, company_id=None, name=None, type=None, code=None, share_class=None, currency=None, round_lot_size=None, ticker=None, exchange_ticker=None, composite_ticker=None, alternate_tickers=None, figi=None, cik=None, composite_figi=None, share_class_figi=None, figi_uniqueid=None, active=None, etf=None, delisted=None, primary_listing=None, primary_security=None, first_stock_price=None, last_stock_price=None, last_stock_price_adjustment=None, last_corporate_action=None, previous_tickers=None):  # noqa: E501
        """Security - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._company_id = None
        self._name = None
        self._type = None
        self._code = None
        self._share_class = None
        self._currency = None
        self._round_lot_size = None
        self._ticker = None
        self._exchange_ticker = None
        self._composite_ticker = None
        self._alternate_tickers = None
        self._figi = None
        self._cik = None
        self._composite_figi = None
        self._share_class_figi = None
        self._figi_uniqueid = None
        self._active = None
        self._etf = None
        self._delisted = None
        self._primary_listing = None
        self._primary_security = None
        self._first_stock_price = None
        self._last_stock_price = None
        self._last_stock_price_adjustment = None
        self._last_corporate_action = None
        self._previous_tickers = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if company_id is not None:
            self.company_id = company_id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if code is not None:
            self.code = code
        if share_class is not None:
            self.share_class = share_class
        if currency is not None:
            self.currency = currency
        if round_lot_size is not None:
            self.round_lot_size = round_lot_size
        if ticker is not None:
            self.ticker = ticker
        if exchange_ticker is not None:
            self.exchange_ticker = exchange_ticker
        if composite_ticker is not None:
            self.composite_ticker = composite_ticker
        if alternate_tickers is not None:
            self.alternate_tickers = alternate_tickers
        if figi is not None:
            self.figi = figi
        if cik is not None:
            self.cik = cik
        if composite_figi is not None:
            self.composite_figi = composite_figi
        if share_class_figi is not None:
            self.share_class_figi = share_class_figi
        if figi_uniqueid is not None:
            self.figi_uniqueid = figi_uniqueid
        if active is not None:
            self.active = active
        if etf is not None:
            self.etf = etf
        if delisted is not None:
            self.delisted = delisted
        if primary_listing is not None:
            self.primary_listing = primary_listing
        if primary_security is not None:
            self.primary_security = primary_security
        if first_stock_price is not None:
            self.first_stock_price = first_stock_price
        if last_stock_price is not None:
            self.last_stock_price = last_stock_price
        if last_stock_price_adjustment is not None:
            self.last_stock_price_adjustment = last_stock_price_adjustment
        if last_corporate_action is not None:
            self.last_corporate_action = last_corporate_action
        if previous_tickers is not None:
            self.previous_tickers = previous_tickers

    @property
    def id(self):
        """Gets the id of this Security.  # noqa: E501

        The Intrinio ID for the Security  # noqa: E501

        :return: The id of this Security.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Security.

        The Intrinio ID for the Security  # noqa: E501

        :param id: The id of this Security.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def company_id(self):
        """Gets the company_id of this Security.  # noqa: E501

        The Intrinio ID for the company for which the Security is issued  # noqa: E501

        :return: The company_id of this Security.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this Security.

        The Intrinio ID for the company for which the Security is issued  # noqa: E501

        :param company_id: The company_id of this Security.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def name(self):
        """Gets the name of this Security.  # noqa: E501

        The name of the Security  # noqa: E501

        :return: The name of this Security.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Security.

        The name of the Security  # noqa: E501

        :param name: The name of this Security.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Security.  # noqa: E501

        The Security's type  # noqa: E501

        :return: The type of this Security.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Security.

        The Security's type  # noqa: E501

        :param type: The type of this Security.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def code(self):
        """Gets the code of this Security.  # noqa: E501

        A 2-3 digit code classifying the Security  # noqa: E501

        :return: The code of this Security.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Security.

        A 2-3 digit code classifying the Security  # noqa: E501

        :param code: The code of this Security.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def share_class(self):
        """Gets the share_class of this Security.  # noqa: E501

        The Security's share class (if applicable)  # noqa: E501

        :return: The share_class of this Security.  # noqa: E501
        :rtype: str
        """
        return self._share_class

    @share_class.setter
    def share_class(self, share_class):
        """Sets the share_class of this Security.

        The Security's share class (if applicable)  # noqa: E501

        :param share_class: The share_class of this Security.  # noqa: E501
        :type: str
        """

        self._share_class = share_class

    @property
    def currency(self):
        """Gets the currency of this Security.  # noqa: E501

        The currency in which the Security is traded on the exchange  # noqa: E501

        :return: The currency of this Security.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Security.

        The currency in which the Security is traded on the exchange  # noqa: E501

        :param currency: The currency of this Security.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def round_lot_size(self):
        """Gets the round_lot_size of this Security.  # noqa: E501

        The normal unit of trading  # noqa: E501

        :return: The round_lot_size of this Security.  # noqa: E501
        :rtype: float
        """
        return self._round_lot_size

    @round_lot_size.setter
    def round_lot_size(self, round_lot_size):
        """Sets the round_lot_size of this Security.

        The normal unit of trading  # noqa: E501

        :param round_lot_size: The round_lot_size of this Security.  # noqa: E501
        :type: float
        """

        self._round_lot_size = round_lot_size

    @property
    def ticker(self):
        """Gets the ticker of this Security.  # noqa: E501

        The common ticker  # noqa: E501

        :return: The ticker of this Security.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this Security.

        The common ticker  # noqa: E501

        :param ticker: The ticker of this Security.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def exchange_ticker(self):
        """Gets the exchange_ticker of this Security.  # noqa: E501

        The exchange-level ticker  # noqa: E501

        :return: The exchange_ticker of this Security.  # noqa: E501
        :rtype: str
        """
        return self._exchange_ticker

    @exchange_ticker.setter
    def exchange_ticker(self, exchange_ticker):
        """Sets the exchange_ticker of this Security.

        The exchange-level ticker  # noqa: E501

        :param exchange_ticker: The exchange_ticker of this Security.  # noqa: E501
        :type: str
        """

        self._exchange_ticker = exchange_ticker

    @property
    def composite_ticker(self):
        """Gets the composite_ticker of this Security.  # noqa: E501

        The country-composite ticker  # noqa: E501

        :return: The composite_ticker of this Security.  # noqa: E501
        :rtype: str
        """
        return self._composite_ticker

    @composite_ticker.setter
    def composite_ticker(self, composite_ticker):
        """Sets the composite_ticker of this Security.

        The country-composite ticker  # noqa: E501

        :param composite_ticker: The composite_ticker of this Security.  # noqa: E501
        :type: str
        """

        self._composite_ticker = composite_ticker

    @property
    def alternate_tickers(self):
        """Gets the alternate_tickers of this Security.  # noqa: E501

        Alternate formats of the common ticker  # noqa: E501

        :return: The alternate_tickers of this Security.  # noqa: E501
        :rtype: list[str]
        """
        return self._alternate_tickers

    @alternate_tickers.setter
    def alternate_tickers(self, alternate_tickers):
        """Sets the alternate_tickers of this Security.

        Alternate formats of the common ticker  # noqa: E501

        :param alternate_tickers: The alternate_tickers of this Security.  # noqa: E501
        :type: list[str]
        """

        self._alternate_tickers = alternate_tickers

    @property
    def figi(self):
        """Gets the figi of this Security.  # noqa: E501

        The exchange-level OpenFIGI identifier  # noqa: E501

        :return: The figi of this Security.  # noqa: E501
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """Sets the figi of this Security.

        The exchange-level OpenFIGI identifier  # noqa: E501

        :param figi: The figi of this Security.  # noqa: E501
        :type: str
        """

        self._figi = figi

    @property
    def cik(self):
        """Gets the cik of this Security.  # noqa: E501

        Central Index Key issued by the SEC, which is the unique identifier for all owner filings  # noqa: E501

        :return: The cik of this Security.  # noqa: E501
        :rtype: str
        """
        return self._cik

    @cik.setter
    def cik(self, cik):
        """Sets the cik of this Security.

        Central Index Key issued by the SEC, which is the unique identifier for all owner filings  # noqa: E501

        :param cik: The cik of this Security.  # noqa: E501
        :type: str
        """

        self._cik = cik

    @property
    def composite_figi(self):
        """Gets the composite_figi of this Security.  # noqa: E501

        The country-composite OpenFIGI identifier  # noqa: E501

        :return: The composite_figi of this Security.  # noqa: E501
        :rtype: str
        """
        return self._composite_figi

    @composite_figi.setter
    def composite_figi(self, composite_figi):
        """Sets the composite_figi of this Security.

        The country-composite OpenFIGI identifier  # noqa: E501

        :param composite_figi: The composite_figi of this Security.  # noqa: E501
        :type: str
        """

        self._composite_figi = composite_figi

    @property
    def share_class_figi(self):
        """Gets the share_class_figi of this Security.  # noqa: E501

        The global-composite OpenFIGI identifier  # noqa: E501

        :return: The share_class_figi of this Security.  # noqa: E501
        :rtype: str
        """
        return self._share_class_figi

    @share_class_figi.setter
    def share_class_figi(self, share_class_figi):
        """Sets the share_class_figi of this Security.

        The global-composite OpenFIGI identifier  # noqa: E501

        :param share_class_figi: The share_class_figi of this Security.  # noqa: E501
        :type: str
        """

        self._share_class_figi = share_class_figi

    @property
    def figi_uniqueid(self):
        """Gets the figi_uniqueid of this Security.  # noqa: E501

        The OpenFIGI unique ID  # noqa: E501

        :return: The figi_uniqueid of this Security.  # noqa: E501
        :rtype: str
        """
        return self._figi_uniqueid

    @figi_uniqueid.setter
    def figi_uniqueid(self, figi_uniqueid):
        """Sets the figi_uniqueid of this Security.

        The OpenFIGI unique ID  # noqa: E501

        :param figi_uniqueid: The figi_uniqueid of this Security.  # noqa: E501
        :type: str
        """

        self._figi_uniqueid = figi_uniqueid

    @property
    def active(self):
        """Gets the active of this Security.  # noqa: E501

        If true, the Security is active and has been recently traded  # noqa: E501

        :return: The active of this Security.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Security.

        If true, the Security is active and has been recently traded  # noqa: E501

        :param active: The active of this Security.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def etf(self):
        """Gets the etf of this Security.  # noqa: E501

        If true, this Security is an ETF  # noqa: E501

        :return: The etf of this Security.  # noqa: E501
        :rtype: bool
        """
        return self._etf

    @etf.setter
    def etf(self, etf):
        """Sets the etf of this Security.

        If true, this Security is an ETF  # noqa: E501

        :param etf: The etf of this Security.  # noqa: E501
        :type: bool
        """

        self._etf = etf

    @property
    def delisted(self):
        """Gets the delisted of this Security.  # noqa: E501

        If true, the Security is no longer traded on the exchange  # noqa: E501

        :return: The delisted of this Security.  # noqa: E501
        :rtype: bool
        """
        return self._delisted

    @delisted.setter
    def delisted(self, delisted):
        """Sets the delisted of this Security.

        If true, the Security is no longer traded on the exchange  # noqa: E501

        :param delisted: The delisted of this Security.  # noqa: E501
        :type: bool
        """

        self._delisted = delisted

    @property
    def primary_listing(self):
        """Gets the primary_listing of this Security.  # noqa: E501

        If true, the Security is the primary issue for the company, otherwise it is a secondary issue on a secondary stock exchange  # noqa: E501

        :return: The primary_listing of this Security.  # noqa: E501
        :rtype: bool
        """
        return self._primary_listing

    @primary_listing.setter
    def primary_listing(self, primary_listing):
        """Sets the primary_listing of this Security.

        If true, the Security is the primary issue for the company, otherwise it is a secondary issue on a secondary stock exchange  # noqa: E501

        :param primary_listing: The primary_listing of this Security.  # noqa: E501
        :type: bool
        """

        self._primary_listing = primary_listing

    @property
    def primary_security(self):
        """Gets the primary_security of this Security.  # noqa: E501

        If true, the Security is considered by Intrinio to be the primary Security for its company  # noqa: E501

        :return: The primary_security of this Security.  # noqa: E501
        :rtype: bool
        """
        return self._primary_security

    @primary_security.setter
    def primary_security(self, primary_security):
        """Sets the primary_security of this Security.

        If true, the Security is considered by Intrinio to be the primary Security for its company  # noqa: E501

        :param primary_security: The primary_security of this Security.  # noqa: E501
        :type: bool
        """

        self._primary_security = primary_security

    @property
    def first_stock_price(self):
        """Gets the first_stock_price of this Security.  # noqa: E501

        The date of the first recorded stock price  # noqa: E501

        :return: The first_stock_price of this Security.  # noqa: E501
        :rtype: date
        """
        return self._first_stock_price

    @first_stock_price.setter
    def first_stock_price(self, first_stock_price):
        """Sets the first_stock_price of this Security.

        The date of the first recorded stock price  # noqa: E501

        :param first_stock_price: The first_stock_price of this Security.  # noqa: E501
        :type: date
        """

        self._first_stock_price = first_stock_price

    @property
    def last_stock_price(self):
        """Gets the last_stock_price of this Security.  # noqa: E501

        The date of the last recorded stock price (or the most recent trading day)  # noqa: E501

        :return: The last_stock_price of this Security.  # noqa: E501
        :rtype: date
        """
        return self._last_stock_price

    @last_stock_price.setter
    def last_stock_price(self, last_stock_price):
        """Sets the last_stock_price of this Security.

        The date of the last recorded stock price (or the most recent trading day)  # noqa: E501

        :param last_stock_price: The last_stock_price of this Security.  # noqa: E501
        :type: date
        """

        self._last_stock_price = last_stock_price

    @property
    def last_stock_price_adjustment(self):
        """Gets the last_stock_price_adjustment of this Security.  # noqa: E501

        The date of the last stock price adjustment (dividend, split, etc)  # noqa: E501

        :return: The last_stock_price_adjustment of this Security.  # noqa: E501
        :rtype: date
        """
        return self._last_stock_price_adjustment

    @last_stock_price_adjustment.setter
    def last_stock_price_adjustment(self, last_stock_price_adjustment):
        """Sets the last_stock_price_adjustment of this Security.

        The date of the last stock price adjustment (dividend, split, etc)  # noqa: E501

        :param last_stock_price_adjustment: The last_stock_price_adjustment of this Security.  # noqa: E501
        :type: date
        """

        self._last_stock_price_adjustment = last_stock_price_adjustment

    @property
    def last_corporate_action(self):
        """Gets the last_corporate_action of this Security.  # noqa: E501

        The date of the last corporate action  # noqa: E501

        :return: The last_corporate_action of this Security.  # noqa: E501
        :rtype: date
        """
        return self._last_corporate_action

    @last_corporate_action.setter
    def last_corporate_action(self, last_corporate_action):
        """Sets the last_corporate_action of this Security.

        The date of the last corporate action  # noqa: E501

        :param last_corporate_action: The last_corporate_action of this Security.  # noqa: E501
        :type: date
        """

        self._last_corporate_action = last_corporate_action

    @property
    def previous_tickers(self):
        """Gets the previous_tickers of this Security.  # noqa: E501

        Previous tickers used by this security  # noqa: E501

        :return: The previous_tickers of this Security.  # noqa: E501
        :rtype: list[str]
        """
        return self._previous_tickers

    @previous_tickers.setter
    def previous_tickers(self, previous_tickers):
        """Sets the previous_tickers of this Security.

        Previous tickers used by this security  # noqa: E501

        :param previous_tickers: The previous_tickers of this Security.  # noqa: E501
        :type: list[str]
        """

        self._previous_tickers = previous_tickers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Security):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
