from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel


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
    cash: float
    dividendDetails: DividendDetails
    id: int
    progress: float
    result: Result
    status: str


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
