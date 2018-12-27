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


class StockMarketIndexSummary(object):
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
        'symbol': 'str',
        'name': 'str',
        'continent': 'str',
        'country': 'str',
        'update_frequency': 'str',
        'last_updated': 'datetime',
        'observation_start': 'date',
        'observation_end': 'date'
    }

    attribute_map = {
        'id': 'id',
        'symbol': 'symbol',
        'name': 'name',
        'continent': 'continent',
        'country': 'country',
        'update_frequency': 'update_frequency',
        'last_updated': 'last_updated',
        'observation_start': 'observation_start',
        'observation_end': 'observation_end'
    }

    def __init__(self, id=None, symbol=None, name=None, continent=None, country=None, update_frequency=None, last_updated=None, observation_start=None, observation_end=None):  # noqa: E501
        """StockMarketIndexSummary - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._symbol = None
        self._name = None
        self._continent = None
        self._country = None
        self._update_frequency = None
        self._last_updated = None
        self._observation_start = None
        self._observation_end = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if symbol is not None:
            self.symbol = symbol
        if name is not None:
            self.name = name
        if continent is not None:
            self.continent = continent
        if country is not None:
            self.country = country
        if update_frequency is not None:
            self.update_frequency = update_frequency
        if last_updated is not None:
            self.last_updated = last_updated
        if observation_start is not None:
            self.observation_start = observation_start
        if observation_end is not None:
            self.observation_end = observation_end

    @property
    def id(self):
        """Gets the id of this StockMarketIndexSummary.  # noqa: E501

        Intrinio ID for the Index  # noqa: E501

        :return: The id of this StockMarketIndexSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StockMarketIndexSummary.

        Intrinio ID for the Index  # noqa: E501

        :param id: The id of this StockMarketIndexSummary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def symbol(self):
        """Gets the symbol of this StockMarketIndexSummary.  # noqa: E501

        The symbol used to identify the Index  # noqa: E501

        :return: The symbol of this StockMarketIndexSummary.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this StockMarketIndexSummary.

        The symbol used to identify the Index  # noqa: E501

        :param symbol: The symbol of this StockMarketIndexSummary.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def name(self):
        """Gets the name of this StockMarketIndexSummary.  # noqa: E501

        The name of the Index  # noqa: E501

        :return: The name of this StockMarketIndexSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StockMarketIndexSummary.

        The name of the Index  # noqa: E501

        :param name: The name of this StockMarketIndexSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def continent(self):
        """Gets the continent of this StockMarketIndexSummary.  # noqa: E501

        The continent of the country of focus for the Index  # noqa: E501

        :return: The continent of this StockMarketIndexSummary.  # noqa: E501
        :rtype: str
        """
        return self._continent

    @continent.setter
    def continent(self, continent):
        """Sets the continent of this StockMarketIndexSummary.

        The continent of the country of focus for the Index  # noqa: E501

        :param continent: The continent of this StockMarketIndexSummary.  # noqa: E501
        :type: str
        """

        self._continent = continent

    @property
    def country(self):
        """Gets the country of this StockMarketIndexSummary.  # noqa: E501

        The country of focus for the Index  # noqa: E501

        :return: The country of this StockMarketIndexSummary.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this StockMarketIndexSummary.

        The country of focus for the Index  # noqa: E501

        :param country: The country of this StockMarketIndexSummary.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def update_frequency(self):
        """Gets the update_frequency of this StockMarketIndexSummary.  # noqa: E501

        How often the Index is updated  # noqa: E501

        :return: The update_frequency of this StockMarketIndexSummary.  # noqa: E501
        :rtype: str
        """
        return self._update_frequency

    @update_frequency.setter
    def update_frequency(self, update_frequency):
        """Sets the update_frequency of this StockMarketIndexSummary.

        How often the Index is updated  # noqa: E501

        :param update_frequency: The update_frequency of this StockMarketIndexSummary.  # noqa: E501
        :type: str
        """

        self._update_frequency = update_frequency

    @property
    def last_updated(self):
        """Gets the last_updated of this StockMarketIndexSummary.  # noqa: E501

        When the Index was updated last  # noqa: E501

        :return: The last_updated of this StockMarketIndexSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this StockMarketIndexSummary.

        When the Index was updated last  # noqa: E501

        :param last_updated: The last_updated of this StockMarketIndexSummary.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def observation_start(self):
        """Gets the observation_start of this StockMarketIndexSummary.  # noqa: E501

        The earliest date for which data is available  # noqa: E501

        :return: The observation_start of this StockMarketIndexSummary.  # noqa: E501
        :rtype: date
        """
        return self._observation_start

    @observation_start.setter
    def observation_start(self, observation_start):
        """Sets the observation_start of this StockMarketIndexSummary.

        The earliest date for which data is available  # noqa: E501

        :param observation_start: The observation_start of this StockMarketIndexSummary.  # noqa: E501
        :type: date
        """

        self._observation_start = observation_start

    @property
    def observation_end(self):
        """Gets the observation_end of this StockMarketIndexSummary.  # noqa: E501

        The latest date for which data is available  # noqa: E501

        :return: The observation_end of this StockMarketIndexSummary.  # noqa: E501
        :rtype: date
        """
        return self._observation_end

    @observation_end.setter
    def observation_end(self, observation_end):
        """Sets the observation_end of this StockMarketIndexSummary.

        The latest date for which data is available  # noqa: E501

        :param observation_end: The observation_end of this StockMarketIndexSummary.  # noqa: E501
        :type: date
        """

        self._observation_end = observation_end

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
        if not isinstance(other, StockMarketIndexSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
