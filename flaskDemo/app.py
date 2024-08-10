from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Return a friendly HTTP greeting."""
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet():
    """Display a greeting."""
    name = "John Michael Kane"
    return f"Hello {name}"


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9.0 / 5) + 32


@app.route('/f/<float:celsius>')
def convert_to_fahrenheit(celsius):
    """Convert from Celsius to Fahrenheit and display both values."""
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f"{celsius}°C is equivalent to {fahrenheit:.2f}°F"


if __name__ == '__main__':
    app.run()
