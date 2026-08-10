from homeassistant.core import HomeAssistant, ServiceCall

DOMAIN = "russound_keypress"
RUSSOUND_DOMAIN = "russound_rio"


async def async_setup(hass: HomeAssistant, config: dict) -> bool:

    def get_zone(zone_name: str):
        entries = hass.config_entries.async_entries(RUSSOUND_DOMAIN)

        if not entries:
            raise RuntimeError("No Russound RIO config entry found")

        client = entries[0].runtime_data

        for controller in client.controllers.values():
            for zone in controller.zones.values():
                if zone.name == zone_name:
                    return zone

        raise RuntimeError(f"Russound zone not found: {zone_name}")

    async def previous(call: ServiceCall) -> None:
        zone = get_zone(call.data["zone"])
        await zone.send_event("KeyRelease", "Previous")

    async def next_(call: ServiceCall) -> None:
        zone = get_zone(call.data["zone"])
        await zone.send_event("KeyRelease", "Next")

    async def channel_up(call: ServiceCall) -> None:
        zone = get_zone(call.data["zone"])
        await zone.send_event("KeyRelease", "ChannelUp")

    async def channel_down(call: ServiceCall) -> None:
        zone = get_zone(call.data["zone"])
        await zone.send_event("KeyRelease", "ChannelDown")

    hass.services.async_register(DOMAIN, "previous", previous)
    hass.services.async_register(DOMAIN, "next", next_)
    hass.services.async_register(DOMAIN, "channel_up", channel_up)
    hass.services.async_register(DOMAIN, "channel_down", channel_down)

    return True
