# Russound KeyPress

A Home Assistant custom integration that adds direct keypress services to the Russound RIO integration.

## What it does

The Russound RIO integration provides control of Russound zones, but does not expose every physical keypad button as a Home Assistant service.

Russound KeyPress adds the following services:

- `russound_keypress.previous`
- `russound_keypress.next`
- `russound_keypress.channel_up`
- `russound_keypress.channel_down`

These send the corresponding Russound keypad events directly to the selected zone.

## Requirements

This integration requires the Home Assistant Russound RIO integration to already be installed and configured.

## Installation

Copy the `custom_components/russound_keypress` directory into the `custom_components` directory of your Home Assistant configuration:

```text
/config/custom_components/russound_keypress/
