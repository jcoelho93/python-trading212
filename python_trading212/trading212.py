import os
import requests
from typing import List, Dict
from requests.exceptions import HTTPError
from python_trading212.models import (
    Position, Exchange, Instrument,
    Pie, Order, AccountCash, AccountMetadata,
    NewPieIn, NewPieOut, HistoricalOrderData
)


class Trading212:
    def __init__(self, host='live.trading212.com'):
        self.session = requests.Session()
        self.session.headers = self._authenticate()
        host = os.getenv('TRADING212_HOST', host)
        self.url = f"https://{host}/api/v0/"

    def _authenticate(self) -> Dict[str, str]:
        try:
            api_key = os.environ['TRADING212_API_KEY']
        except KeyError:
            raise Exception(
                "Please set the TRADING212_API_KEY environment variable")
        return {
            "Authorization": api_key
        }

    def _get(self, endpoint: str, params=None):
        try:
            response = self.session.get(endpoint, params=params)
            response.raise_for_status()
        except HTTPError as e:
            raise Exception(f"Error: {e}")
        return response.json()

    def _post(self, endpoint: str, json: Dict):
        try:
            response = self.session.post(endpoint, json=json)
            response.raise_for_status()
        except HTTPError as e:
            raise Exception(f"Error: {e}")
        return response.json()

    def _delete(self, endpoint: str):
        try:
            response = self.session.delete(endpoint)
            response.raise_for_status()
        except HTTPError as e:
            raise Exception(f"Error: {e}")
        return response.json()

    def exchange_list(self) -> List[Exchange]:
        """Fetch all exchanges and their corresponding working schedules that your account has access to

        https://t212public-api-docs.redoc.ly/#operation/exchanges

        Raises:
            Exception: _description_

        Returns:
            List[Exchange]: a list of exchanges
        """
        endpoint = self.url + "equity/metadata/exchanges"
        response = self._get(endpoint)

        exchanges = []
        for exchange in response:
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
        endpoint = self.url + "equity/metadata/instruments"
        response = self._get(endpoint)

        instruments = []
        for instrument in response:
            instruments.append(Instrument(**instrument))
        return instruments

    def fetch_all_pies(self) -> List[Pie]:
        """Fetches all pies for the account

        https://t212public-api-docs.redoc.ly/#operation/getAll

        Returns:
            List[Pie]: a list of pies
        """
        endpoint = self.url + "equity/pies"
        response = self._get(endpoint)

        pies = []
        for pie in response:
            pies.append(Pie(**pie))
        return pies

    def create_pie(self, new_pie: NewPieIn) -> NewPieOut:
        """Creates a new pie

        https://t212public-api-docs.redoc.ly/#operation/create

        Args:
            new_pie (NewPieIn): the new pie to create

        Returns:
            NewPieOut: the new pie
        """
        endpoint = self.url + "equity/pie"
        response = self._post(endpoint, new_pie.model_dump())

        return NewPieOut(**response)

    def delete_pie(self, id: int) -> None:
        """Deletes a pie by ID

        https://t212public-api-docs.redoc.ly/#operation/delete

        Args:
            id (int): the ID of the pie
        """
        endpoint = self.url + f"equity/pie/{id}"
        return self._delete(endpoint)

    def fetch_pie(self, id: int) -> Pie:
        """Fetches a pies for the account with detailed information

        https://t212public-api-docs.redoc.ly/#operation/getDetailed

        Args:
            id (int): the ID of the pie

        Returns:
            Pie: the pie
        """
        endpoint = self.url + f"equity/pie/{id}"
        response = self._get(endpoint)

        return Pie(**response)

    def update_pie(self, id: int, new_pie: NewPieIn) -> NewPieOut:
        """Updates a pie by ID

        https://t212public-api-docs.redoc.ly/#operation/update

        Args:
            id (int): the ID of the pie
            new_pie (NewPieIn): the new pie

        Returns:
            NewPieOut: the new pie
        """
        endpoint = self.url + f"equity/pie/{id}"
        response = self._post(endpoint, new_pie.model_dump())

        return NewPieOut(**response)

    def fetch_all_orders(self) -> List[Order]:
        """ Fetches all orders

        https://t212public-api-docs.redoc.ly/#operation/orders

        Returns:
            List[Order]: _description_
        """
        endpoint = self.url + "equity/orders"
        response = self._get(endpoint)

        orders = []
        for order in response:
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
        endpoint = self.url + f"equity/orders/{id}"
        response = self._get(endpoint)

        return Order(**response)

    def fetch_account_cash(self) -> AccountCash:
        """Fetches account cash information

        https://t212public-api-docs.redoc.ly/#operation/accountCash

        Returns:
            AccountCash: _description_
        """
        endpoint = self.url + "equity/account/cash"
        response = self._get(endpoint)

        return AccountCash(**response)

    def fetch_account_metadata(self) -> AccountMetadata:
        """ Fetches account metadata

        https://t212public-api-docs.redoc.ly/#operation/account

        Returns:
            AccountMetadata: _description_
        """
        endpoint = self.url + "equity/account/info"
        response = self._get(endpoint)

        return AccountMetadata(**response)

    def fetch_all_open_positions(self) -> List[Position]:
        """Fetch an open positions for your account

        https://t212public-api-docs.redoc.ly/#operation/portfolio

        Raises:
            Exception: _description_

        Returns:
            List[Position]: _description_
        """
        endpoint = self.url + "equity/portfolio"
        response = self._get(endpoint)

        positions = []
        for position in response:
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
        endpoint = self.url + f"equity/portfolio/{ticker}"
        response = self._get(endpoint)

        return Position(**response)

    def historical_order_data(self, cursor: int, ticker: str, limit: int) -> HistoricalOrderData:
        """Fetch historical order data

        https://t212public-api-docs.redoc.ly/#operation/orders_1

        Args:
            cursor (int): the cursor
            ticker (str): the ticker
            limit (int): the limit

        Returns:
            HistoricalOrderData: _description_
        """
        endpoint = self.url + "equity/history/orders"
        params = None
        if cursor or ticker or limit:
            params = {
                "cursor": cursor,
                "ticker": ticker,
                "limit": limit
            }
        response = self._get(endpoint, params)

        return HistoricalOrderData(**response)
