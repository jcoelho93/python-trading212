# pytrading212

A client for the [Trading212 API](https://t212public-api-docs.redoc.ly/)

## Installation

```bash
pip install pytrading212
```

## Usage

Set your **read-only** API key in the environment variable:
```bash
export TRADING_212_KEY=<your-api-key>
```

```python
from pytrading212 import Trading212, Pie

trading212 = Trading212()
pie: Pie = trading212.fetch_pie(123)

```
