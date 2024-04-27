from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import List, Optional, Dict
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
    addedOn: str
    currencyCode: str
    isin: str
    maxOpenQuantity: float
    minTradeQuantity: float
    name: str
    shortname: str
    ticker: str
    type: str
    workingScheduleId: int


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
    creationTime: str
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
    blocked: float
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
    endDate: str
    goal: int
    icon: Optional[Icon]
    id: int
    initialInvestment: int
    instrumentShares: Dict[str, float]
    name: str
    pubicUrl: str


class Tax(BaseModel):
    fillId: str
    name: str
    quantity: float
    timeCharged: datetime


class HistoryItem(BaseModel):
    dateCreated: datetime
    dateExecuted: datetime
    dateModified: datetime
    executor: str
    fillCost: float
    fillId: int
    fillPrice: float
    fillResult: float
    fillType: str
    filledQuantity: float
    filledValue: float
    id: int
    limitPrice: float
    orderedQuantity: float
    orderedValue: float
    parentOrder: int
    status: str
    stopPrice: float
    taxes: List[Tax]
    ticker: str
    timeValidity: str
    type: str


class HistoricalOrderData(BaseModel):
    items: List[HistoryItem]
    nextPagePath: str


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


class FilledOrder(BaseModel):
    creationTime: str
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
