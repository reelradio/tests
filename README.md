# Reel Radio tests

Selenium tests to test all site functionality.

## First time setup

Create a new Python 3 virtual environment so we can install dependencies, and activate it:

```
python3 -m env venv
. venv/bin/activate
```

Then install the requirements:

```
pip install -r requirements.txt
```

Then install a browser driver:
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
and add the driver file to the `venv/bin` directory.

I've used the `geckodriver` for Firefox in the python scripts.


## When returning after closing terminal

Ensure your venv is activated

```
. venv/bin/activate
```

## Running the tests

Either run the tests individually, ie:

```
python 01-get.py
```

Or run all of the tests:

```
for f in *.py; do python "$f"; done
```

