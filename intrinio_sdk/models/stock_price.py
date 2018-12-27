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

from intrinio_sdk.models.security_summary import SecuritySummary  # noqa: F401,E501


class StockPrice(object):
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
        'date': 'date',
        'intraperiod': 'bool',
        'frequency': 'str',
        'open': 'float',
        'high': 'float',
        'low': 'float',
        'close': 'float',
        'volume': 'float',
        'adj_open': 'float',
        'adj_high': 'float',
        'adj_low': 'float',
        'adj_close': 'float',
        'adj_volume': 'float',
        'security': 'SecuritySummary'
    }

    attribute_map = {
        'date': 'date',
        'intraperiod': 'intraperiod',
        'frequency': 'frequency',
        'open': 'open',
        'high': 'high',
        'low': 'low',
        'close': 'close',
        'volume': 'volume',
        'adj_open': 'adj_open',
        'adj_high': 'adj_high',
        'adj_low': 'adj_low',
        'adj_close': 'adj_close',
        'adj_volume': 'adj_volume',
        'security': 'security'
    }

    def __init__(self, date=None, intraperiod=None, frequency=None, open=None, high=None, low=None, close=None, volume=None, adj_open=None, adj_high=None, adj_low=None, adj_close=None, adj_volume=None, security=None):  # noqa: E501
        """StockPrice - a model defined in Swagger"""  # noqa: E501

        self._date = None
        self._intraperiod = None
        self._frequency = None
        self._open = None
        self._high = None
        self._low = None
        self._close = None
        self._volume = None
        self._adj_open = None
        self._adj_high = None
        self._adj_low = None
        self._adj_close = None
        self._adj_volume = None
        self._security = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if intraperiod is not None:
            self.intraperiod = intraperiod
        if frequency is not None:
            self.frequency = frequency
        if open is not None:
            self.open = open
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if close is not None:
            self.close = close
        if volume is not None:
            self.volume = volume
        if adj_open is not None:
            self.adj_open = adj_open
        if adj_high is not None:
            self.adj_high = adj_high
        if adj_low is not None:
            self.adj_low = adj_low
        if adj_close is not None:
            self.adj_close = adj_close
        if adj_volume is not None:
            self.adj_volume = adj_volume
        if security is not None:
            self.security = security

    @property
    def date(self):
        """Gets the date of this StockPrice.  # noqa: E501

        The calendar date that the stock price represents. For non-daily stock prices, this represents the last day in the period (end of the week, month, quarter, year, etc)  # noqa: E501

        :return: The date of this StockPrice.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this StockPrice.

        The calendar date that the stock price represents. For non-daily stock prices, this represents the last day in the period (end of the week, month, quarter, year, etc)  # noqa: E501

        :param date: The date of this StockPrice.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def intraperiod(self):
        """Gets the intraperiod of this StockPrice.  # noqa: E501

        If true, the stock price represents an unfinished period (be it day, week, quarter, month, or year), meaning that the close price is the latest price available, not the official close price for the period  # noqa: E501

        :return: The intraperiod of this StockPrice.  # noqa: E501
        :rtype: bool
        """
        return self._intraperiod

    @intraperiod.setter
    def intraperiod(self, intraperiod):
        """Sets the intraperiod of this StockPrice.

        If true, the stock price represents an unfinished period (be it day, week, quarter, month, or year), meaning that the close price is the latest price available, not the official close price for the period  # noqa: E501

        :param intraperiod: The intraperiod of this StockPrice.  # noqa: E501
        :type: bool
        """

        self._intraperiod = intraperiod

    @property
    def frequency(self):
        """Gets the frequency of this StockPrice.  # noqa: E501

        The type of period that the stock price represents  # noqa: E501

        :return: The frequency of this StockPrice.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this StockPrice.

        The type of period that the stock price represents  # noqa: E501

        :param frequency: The frequency of this StockPrice.  # noqa: E501
        :type: str
        """
        allowed_values = ["daily", "weekly", "monthly", "quarterly", "yearly"]  # noqa: E501
        if frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency, allowed_values)
            )

        self._frequency = frequency

    @property
    def open(self):
        """Gets the open of this StockPrice.  # noqa: E501

        The price at the beginning of the period  # noqa: E501

        :return: The open of this StockPrice.  # noqa: E501
        :rtype: float
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this StockPrice.

        The price at the beginning of the period  # noqa: E501

        :param open: The open of this StockPrice.  # noqa: E501
        :type: float
        """

        self._open = open

    @property
    def high(self):
        """Gets the high of this StockPrice.  # noqa: E501

        The highest price over the span of the period  # noqa: E501

        :return: The high of this StockPrice.  # noqa: E501
        :rtype: float
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this StockPrice.

        The highest price over the span of the period  # noqa: E501

        :param high: The high of this StockPrice.  # noqa: E501
        :type: float
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this StockPrice.  # noqa: E501

        The lowest price over the span of the period  # noqa: E501

        :return: The low of this StockPrice.  # noqa: E501
        :rtype: float
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this StockPrice.

        The lowest price over the span of the period  # noqa: E501

        :param low: The low of this StockPrice.  # noqa: E501
        :type: float
        """

        self._low = low

    @property
    def close(self):
        """Gets the close of this StockPrice.  # noqa: E501

        The price at the end of the period  # noqa: E501

        :return: The close of this StockPrice.  # noqa: E501
        :rtype: float
        """
        return self._close

    @close.setter
    def close(self, close):
        """Sets the close of this StockPrice.

        The price at the end of the period  # noqa: E501

        :param close: The close of this StockPrice.  # noqa: E501
        :type: float
        """

        self._close = close

    @property
    def volume(self):
        """Gets the volume of this StockPrice.  # noqa: E501

        The number of shares exchanged during the period  # noqa: E501

        :return: The volume of this StockPrice.  # noqa: E501
        :rtype: float
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this StockPrice.

        The number of shares exchanged during the period  # noqa: E501

        :param volume: The volume of this StockPrice.  # noqa: E501
        :type: float
        """

        self._volume = volume

    @property
    def adj_open(self):
        """Gets the adj_open of this StockPrice.  # noqa: E501

        The price at the beginning of the period, adjusted for splits and dividends  # noqa: E501

        :return: The adj_open of this StockPrice.  # noqa: E501
        :rtype: float
        """
        return self._adj_open

    @adj_open.setter
    def adj_open(self, adj_open):
        """Sets the adj_open of this StockPrice.

        The price at the beginning of the period, adjusted for splits and dividends  # noqa: E501

        :param adj_open: The adj_open of this StockPrice.  # noqa: E501
        :type: float
        """

        self._adj_open = adj_open

    @property
    def adj_high(self):
        """Gets the adj_high of this StockPrice.  # noqa: E501

        The highest price over the span of the period, adjusted for splits and dividends  # noqa: E501

        :return: The adj_high of this StockPrice.  # noqa: E501
        :rtype: float
        """
        return self._adj_high

    @adj_high.setter
    def adj_high(self, adj_high):
        """Sets the adj_high of this StockPrice.

        The highest price over the span of the period, adjusted for splits and dividends  # noqa: E501

        :param adj_high: The adj_high of this StockPrice.  # noqa: E501
        :type: float
        """

        self._adj_high = adj_high

    @property
    def adj_low(self):
        """Gets the adj_low of this StockPrice.  # noqa: E501

        The lowest price over the span of the period, adjusted for splits and dividends  # noqa: E501

        :return: The adj_low of this StockPrice.  # noqa: E501
        :rtype: float
        """
        return self._adj_low

    @adj_low.setter
    def adj_low(self, adj_low):
        """Sets the adj_low of this StockPrice.

        The lowest price over the span of the period, adjusted for splits and dividends  # noqa: E501

        :param adj_low: The adj_low of this StockPrice.  # noqa: E501
        :type: float
        """

        self._adj_low = adj_low

    @property
    def adj_close(self):
        """Gets the adj_close of this StockPrice.  # noqa: E501

        The price at the end of the period, adjusted for splits and dividends  # noqa: E501

        :return: The adj_close of this StockPrice.  # noqa: E501
        :rtype: float
        """
        return self._adj_close

    @adj_close.setter
    def adj_close(self, adj_close):
        """Sets the adj_close of this StockPrice.

        The price at the end of the period, adjusted for splits and dividends  # noqa: E501

        :param adj_close: The adj_close of this StockPrice.  # noqa: E501
        :type: float
        """

        self._adj_close = adj_close

    @property
    def adj_volume(self):
        """Gets the adj_volume of this StockPrice.  # noqa: E501

        The number of shares exchanged during the period, adjusted for splits and dividends  # noqa: E501

        :return: The adj_volume of this StockPrice.  # noqa: E501
        :rtype: float
        """
        return self._adj_volume

    @adj_volume.setter
    def adj_volume(self, adj_volume):
        """Sets the adj_volume of this StockPrice.

        The number of shares exchanged during the period, adjusted for splits and dividends  # noqa: E501

        :param adj_volume: The adj_volume of this StockPrice.  # noqa: E501
        :type: float
        """

        self._adj_volume = adj_volume

    @property
    def security(self):
        """Gets the security of this StockPrice.  # noqa: E501

        The Security of the stock price  # noqa: E501

        :return: The security of this StockPrice.  # noqa: E501
        :rtype: SecuritySummary
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this StockPrice.

        The Security of the stock price  # noqa: E501

        :param security: The security of this StockPrice.  # noqa: E501
        :type: SecuritySummary
        """

        self._security = security

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
        if not isinstance(other, StockPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
