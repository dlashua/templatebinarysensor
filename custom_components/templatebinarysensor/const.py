"""Constants for templatebinarysensor."""
# Base component constants
DOMAIN = "templatebinarysensor"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
PLATFORMS = ["binary_sensor"]
REQUIRED_FILES = [
    ".translations/en.json",
    "const.py",
    "config_flow.py",
    "manifest.json",
    "binary_sensor.py",
]
ISSUE_URL = "https://github.com/dlashua/templatebinarysensor/issues"
