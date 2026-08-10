# Russound KeyPress

A Home Assistant custom integration that adds direct keypress services to the Russound RIO integration.

## What it does

The Russound RIO integration provides control of Russound zones, but does not expose every physical keypad button as a Home Assistant service.

Russound KeyPress adds these services:

* `russound_keypress.previous`
* `russound_keypress.next`
* `russound_keypress.channel_up`
* `russound_keypress.channel_down`

These send the corresponding Russound keypad events directly to the selected zone.

## Requirements

This integration requires the Home Assistant Russound RIO integration to already be installed and configured.

## Installation

Copy the `custom_components/russound_keypress` directory into the `custom_components` directory of your Home Assistant configuration.

The resulting directory should be:

```text
/config/custom_components/russound_keypress/
```

It should contain:

```text
__init__.py
manifest.json
```

Restart Home Assistant after installation.

## Usage

The services accept a Russound zone name.

### Previous

```yaml
action: russound_keypress.previous
data:
  zone: Rec Room
```

### Next

```yaml
action: russound_keypress.next
data:
  zone: Rec Room
```

### Channel Up

```yaml
action: russound_keypress.channel_up
data:
  zone: Rec Room
```

### Channel Down

```yaml
action: russound_keypress.channel_down
data:
  zone: Rec Room
```

## Supported Buttons

| Service        | Russound Button |
| -------------- | --------------- |
| `previous`     | Previous        |
| `next`         | Next            |
| `channel_up`   | Channel Up      |
| `channel_down` | Channel Down    |

## Notes

The zone name must match the zone name reported by the Russound RIO integration.

This is an independent community-developed custom integration and is not affiliated with Russound.
