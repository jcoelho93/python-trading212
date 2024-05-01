# python-trading212

![CICD Status](https://img.shields.io/github/actions/workflow/status/jcoelho93/python-trading212/ci.yml?label=cicd)
![PyPI - Downloads](https://img.shields.io/pypi/dm/python-trading212)
![GitHub License](https://img.shields.io/github/license/jcoelho93/python-trading212)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-trading212)
![PyPI - Version](https://img.shields.io/pypi/v/python-trading212)


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
from trading212 import Trading212, Pie

trading212 = Trading212()
pie: Pie = trading212.fetch_pie(123)
positions: List[Position] = trading212.fetch_all_open_positions()

trading212.create_pie(
    Pie(
        name='My Pie',
        ...
    )
)

```

## Supported Endpoints

### Instruments Metadata

- [x] Exchange List
- [x] Instrument List

## Pies

- [x] Fetch all pies
- [x] Create Pie
- [x] Delete Pie
- [x] Fetch a Pie
- [x] Update pie

## Equity Orders

- [x] Fetch all
- [x] Place Limit order
- [x] Place Market order
- [x] Place Stop order
- [x] Place StopLimit order
- [x] Cancel by ID
- [x] Fetch by ID

## Account Data

- [x] Fetch account cash
- [x] Fetch account metadata

## Personal Portfolio

- [x] Fetch all open positions
- [x] Fetch a specific position

## Historical Items

- [x] Historical order data
- [x] Paid out dividens
- [x] Exports List
- [x] Export csv
- [x] Transaction list

## Disclaimer

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
