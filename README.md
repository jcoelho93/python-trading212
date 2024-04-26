# python-trading212

A client for the [Trading212 API](https://t212public-api-docs.redoc.ly/)

## Installation

```bash
pip install python-trading212
```

## Usage

Set your API key in the environment variable:
```bash
export TRADING_212_KEY=<your-api-key>
```

```python
from python_trading212 import Trading212, Pie

trading212 = Trading212()
pie: Pie = trading212.fetch_pie(123)
positions: List[Position] = trading212.fetch_all_open_positions()

trading212.create_pie(
    NewPieIn(
        name='My Pie',
        ...
    )
)

```
