from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel


class Position(BaseModel):
    averagePrice: int
    currentPrice: int
    frontend: str
    fxPpl: Optional[int]
    initialFillDate: str
    maxBuy: int
    maxSell: int
    pieQuantity: int
    ppl: int
    quantity: int
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
    maxOpenQuantity: int
    minTradeQuantity: int
    name: str
    shortname: str
    ticker: str
    type: str
    workingScheduleId: int


class DividendDetails(BaseModel):
    gained: int
    inCash: int
    reinvested: int


class Result(BaseModel):
    investedValue: int
    result: int
    resultCoef: int
    value: int


class Pie(BaseModel):
    cash: int
    dividendDetails: DividendDetails
    id: int
    progress: float
    result: Result
    status: str


class Order(BaseModel):
    creationTime: str
    filledQuantity: int
    filledValue: int
    id: int
    limitPrice: int
    quantity: int
    status: str
    stopPrice: int
    strategy: str
    ticker: str
    type: str
    value: int


class AccountCash(BaseModel):
    blocked: int
    free: int
    invested: int
    pieCash: int
    ppl: int
    result: int
    total: int


class AccountMetadata(BaseModel):
    currencyCode: str
    id: int
