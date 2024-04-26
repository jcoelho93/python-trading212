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

## Disclaimer

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
