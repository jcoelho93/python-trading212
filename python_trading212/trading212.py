import os
import requests
from typing import List
from requests.exceptions import HTTPError
from python_trading212.models import (
    Position, Exchange, Instrument,
    Pie, Order, AccountCash, AccountMetadata
)


class Trading212:
    def __init__(self):
        self.session = requests.Session()
        self.url = "https://live.trading212.com/api/v0/"

    def _authenticate(self):
        try:
            api_key = os.environ['TRADING212_API_KEY']
        except KeyError:
            raise Exception(
                "Please set the TRADING212_API_KEY environment variable")
        return {
            "Authorization": api_key
        }

    def exchange_list(self) -> List[Exchange]:
        """Fetch all exchanges and their corresponding working schedules that your account has access to

        https://t212public-api-docs.redoc.ly/#operation/exchanges

        Raises:
            Exception: _description_

        Returns:
            List[Exchange]: a list of exchanges
        """
        headers = self._authenticate()
        endpoint = self.url + "equity/metadata/exchanges"
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise Exception(f"Error: {e}")

        exchanges = []
        for exchange in response.json():
            exchanges.append(Exchange(**exchange))
        return exchanges

    def instrument_list(self) -> List[Instrument]:
        """Fetch all instruments that your account has access to

        https://t212public-api-docs.redoc.ly/#operation/instruments

        Raises:
            Exception: _description_

        Returns:
            List[Instrument]: a list of instruments
        """
        headers = self._authenticate()
        endpoint = self.url + "equity/metadata/instruments"
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise Exception(f"Error: {e}")

        instruments = []
        for instrument in response.json():
            instruments.append(Exchange(**instrument))
        return instruments

    def fetch_all_pies(self) -> List[Pie]:
        """Fetches all pies for the account

        https://t212public-api-docs.redoc.ly/#operation/getAll

        Returns:
            List[Pie]: a list of pies
        """
        headers = self._authenticate()
        endpoint = self.url + "equity/pies"
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise Exception(f"Error: {e}")

        pies = []
        for pie in response.json():
            pies.append(Pie(**pie))
        return pies

    def fetch_pie(self, id: int) -> Pie:
        """Fetches a pies for the account with detailed information

        https://t212public-api-docs.redoc.ly/#operation/getDetailed

        Args:
            id (int): the ID of the pie

        Returns:
            Pie: the pie
        """
        headers = self._authenticate()
        endpoint = self.url + f"equity/pie/{id}"
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise Exception(f"Error: {e}")

        return Pie(**response.json())

    def fetch_all_orders(self) -> List[Order]:
        """ Fetches all orders

        https://t212public-api-docs.redoc.ly/#operation/orders

        Returns:
            List[Order]: _description_
        """
        headers = self._authenticate()
        endpoint = self.url + "equity/orders"
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise Exception(f"Error: {e}")

        orders = []
        for order in response.json():
            orders.append(Order(**order))
        return orders

    def fetch_order(self, id: int) -> Order:
        """Fetches an order by ID

        https://t212public-api-docs.redoc.ly/#operation/orderById

        Args:
            id (int): the ID of the order

        Returns:
            Order: the order
        """
        headers = self._authenticate()
        endpoint = self.url + f"equity/orders/{id}"
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise Exception(f"Error: {e}")

        return Order(**response.json())

    def fetch_account_cash(self) -> AccountCash:
        """Fetches account cash information

        https://t212public-api-docs.redoc.ly/#operation/accountCash

        Returns:
            AccountCash: _description_
        """
        headers = self._authenticate()
        endpoint = self.url + "equity/account/cash"
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise Exception(f"Error: {e}")

        return AccountCash(**response.json())

    def fetch_account_metadata(self) -> AccountMetadata:
        """ Fetches account metadata

        https://t212public-api-docs.redoc.ly/#operation/account

        Returns:
            AccountMetadata: _description_
        """
        headers = self._authenticate()
        endpoint = self.url + "equity/account/info"
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise Exception(f"Error: {e}")

        return AccountMetadata(**response.json())

    def fetch_all_open_positions(self) -> List[Position]:
        """Fetch an open positions for your account

        https://t212public-api-docs.redoc.ly/#operation/portfolio

        Raises:
            Exception: _description_

        Returns:
            List[Position]: _description_
        """
        headers = self._authenticate()
        endpoint = self.url + "equity/portfolio"
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise Exception(f"Error: {e}")

        positions = []
        for position in response.json():
            positions.append(Position(**position))
        return positions

    def fetch_specific_position(self, ticker: str) -> Position:
        """Fetch an open position by ticker

        https://t212public-api-docs.redoc.ly/#operation/positionByTicker

        Args:
            ticker (str): the ticker of the position you want to fetch

        Raises:
            Exception: _description_

        Returns:
            Position: _description_
        """
        headers = self._authenticate()
        endpoint = self.url + f"equity/portfolio/{ticker}"
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
        except HTTPError as e:
            raise Exception(f"Error: {e}")

        return Position(**response.json())
