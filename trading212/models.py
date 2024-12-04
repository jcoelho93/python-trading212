from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel


class Icon(Enum):
    HOME = "Home"
    PIGGY_BANK = "PiggyBank"
    ICEBERG = "Iceberg"
    AIRPLANE = "Airplane"
    RV = "RV"
    UNICORN = "Unicorn"
    WHALE = "Whale"
    CONVERTABLE = "Convertable"
    FAMILY = "Family"
    Coins = "Coins"
    EDUCATION = "Education"
    BILLS_AND_COINS = "BillsAndCoins"
    BILLS = "Bills"
    WATER = "Water"
    WIND = "Wind"
    CAR = "Car"
    BRIEFCASE = "Briefcase"
    MEDICAL = "Medical"
    LANDSCAPE = "Landscape"
    CHILD = "Child"
    VAULT = "Vault"
    TRAVEL = "Travel"
    CABIN = "Cabin"
    APPARTMENTS = "Appartments"
    BURGER = "Burger"
    BUS = "Bus"
    ENERGY = "Energy"
    FACTORY = "Factory"
    GLOBAL = "Global"
    LEAF = "Leaf"
    MATERIALS = "Materials"
    PILL = "Pill"
    RING = "Ring"
    SHIPPING = "Shipping"
    STORE_FRONT = "StoreFront"
    TECH = "Tech"
    UMBRELLA = "Umbrella"


class Position(BaseModel):
    averagePrice: float
    currentPrice: float
    frontend: str
    fxPpl: Optional[float]
    initialFillDate: str
    maxBuy: float
    maxSell: float
    pieQuantity: float
    ppl: float
    quantity: float
    ticker: str


class TimeEvent(BaseModel):
    date: str
    type: str


class WorkingSchedule(BaseModel):
    id: int
    timeEvents: List[TimeEvent]


class Exchange(BaseModel):
    id: int
    name: str
    workingSchedules: Optional[List[WorkingSchedule]]


class Instrument(BaseModel):
    ticker: str
    name: Optional[str] = None
    type: Optional[str] = None
    isin: Optional[str] = None
    addedOn: Optional[str] = None
    shortname: Optional[str] = None
    result: Optional[Result] = None
    currencyCode: Optional[str] = None
    currentShare: Optional[float] = None
    issues: Optional[List[Issue]] = None
    ownedQuantity: Optional[float] = None
    expectedShare: Optional[float] = None
    workingScheduleId: Optional[int] = None
    maxOpenQuantity: Optional[float] = None
    minTradeQuantity: Optional[float] = None


class DividendDetails(BaseModel):
    gained: float
    inCash: float
    reinvested: float


class Result(BaseModel):
    investedValue: float
    result: float
    resultCoef: float
    value: float


class Pie(BaseModel):
    # Pie Out
    cash: Optional[float] = None
    dividendDetails: Optional[DividendDetails] = None
    id: Optional[int] = None
    progress: Optional[float] = None
    result: Optional[Result] = None
    status: Optional[str] = None
    # New Pie Input
    name: Optional[str] = None
    dividendCashAction: Optional[str] = None
    endDate: Optional[datetime] = None
    goal: Optional[float] = None
    icon: Optional[Icon] = None
    instrumentShares: Optional[Dict[str, float]] = None
    # New Pie Output
    instruments: Optional[List[Instrument]] = None
    settings: Optional[Settings] = None


class Order(BaseModel):
    creationTime: datetime
    filledQuantity: float
    filledValue: float
    id: int
    limitPrice: float
    quantity: float
    status: str
    stopPrice: float
    strategy: str
    ticker: str
    type: str
    value: float


class AccountCash(BaseModel):
    blocked: Optional[float]
    free: float
    invested: float
    pieCash: float
    ppl: float
    result: float
    total: float


class AccountMetadata(BaseModel):
    currencyCode: str
    id: int


class Issue(BaseModel):
    name: str
    severity: str


class Settings(BaseModel):
    creationDate: str
    dividendCashAction: str
    endDate: Optional[str] = None
    goal: int
    icon: Optional[Icon]
    id: int
    initialInvestment: Optional[float] = None
    instrumentShares: Optional[Dict[str, float]] = None
    name: str
    pubicUrl: str


class Tax(BaseModel):
    fillId: str
    name: str
    quantity: float
    timeCharged: datetime


class HistoryItem(BaseModel):
    dateCreated: datetime
    dateExecuted: Optional[datetime]
    dateModified: datetime
    executor: str
    fillCost: Optional[float]
    fillId: Optional[int]
    fillPrice: Optional[float]
    fillResult: Optional[float]
    fillType: Optional[str]
    filledQuantity: Optional[float]
    filledValue: Optional[float]
    id: int
    limitPrice: Optional[float]
    orderedQuantity: Optional[float]
    orderedValue: Optional[float]
    parentOrder: int
    status: str
    stopPrice: Optional[float]
    taxes: List[Tax]
    ticker: str
    timeValidity: Optional[str]
    type: str


class HistoricalOrderData(BaseModel):
    items: List[HistoryItem]
    nextPagePath: Optional[str]


class LimitOrder(BaseModel):
    limitPrice: float
    quantity: float
    ticker: str
    timeValidity: str


class MarketOrder(BaseModel):
    quantity: float
    ticker: str


class StopOrder(BaseModel):
    ticker: str
    quantity: float
    stopPrice: float
    timeValidity: str


class StopLimitOrder(BaseModel):
    ticker: str
    quantity: float
    stopPrice: float
    limitPrice: float
    timeValidity: str


class Dividend(BaseModel):
    amount: float
    amountInEuro: float
    grossAmountPerShare: float
    paidOn: datetime
    quantity: float
    reference: str
    ticker: str
    type: str


class PaidOutDividends(BaseModel):
    items: List[Dividend]
    nextPagePath: str


class DataIncluded(BaseModel):
    includeDividends: bool
    includeInterest: bool
    includeOrders: bool
    includeTransactions: bool


class Export(BaseModel):
    dataIncluded: DataIncluded
    downloadLink: str
    reportId: int
    status: str
    timeFrom: datetime
    timeTo: datetime


class Report(BaseModel):
    reportId: int


class Transaction(BaseModel):
    amount: float
    dateTime: datetime
    reference: str
    type: str


class TransactionList(BaseModel):
    items: List[Transaction]
    nextPagePath: str
