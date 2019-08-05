# templatebinarysensor

<!-- [![GitHub Release][releases-shield]][releases] -->
<!-- [![GitHub Activity][commits-shield]][commits] -->
[![License][license-shield]](LICENSE.md)

<!-- [![hacs][hacsbadge]](hacs) -->
![Project Maintenance][maintenance-shield]

[![Community Forum][forum-shield]][forum]

_Add template binary_sensors from the UI._

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `templatebinarysensor`.
4. Download _all_ the files from the `custom_components/templatebinarysensor/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Custom Template Binary Sensor"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/templatebinarysensor/.translations/en.json
custom_components/templatebinarysensor/__init__.py
custom_components/templatebinarysensor/config_flow.py
custom_components/templatebinarysensor/const.py
custom_components/templatebinarysensor/manifest.json
custom_components/templatebinarysensor/sensor.py
```

## Configuration

Configuration are done through the UI.

"Configuration" --> "Integrations" --> "+" --> "Custom Template Binary Sensor"

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[templatebinarysensor]: https://github.com/dlashua/templatebinarysensor
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/

[commits-shield]: https://img.shields.io/github/commit-activity/y/dlashua/templatebinarysensor.svg?style=for-the-badge
[commits]: https://github.com/dlashua/templatebinarysensor/commits/master
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/dlashua/templatebinarysensor.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Daniel%20Lashua%20%40dlashua-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/dlashua/templatebinarysensor.svg?style=for-the-badge
[releases]: https://github.com/dlashua/templatebinarysensor/releases
