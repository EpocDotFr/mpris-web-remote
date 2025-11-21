from dbus_next.aio import MessageBus, ProxyInterface
from dbus_next import Message
from typing import Optional
import abc


class Dbus(metaclass=abc.ABCMeta):
    bus: MessageBus
    interface: ProxyInterface

    @abc.abstractmethod
    async def get_interface(self) -> ProxyInterface:
        raise NotImplementedError()

    async def __aenter__(self) -> 'Dbus':
        self.bus = await MessageBus().connect()
        self.interface = await self.get_interface()

        return self

    async def __aexit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.bus.disconnect()


class Mpris(Dbus):
    async def get_current_state(self) -> Optional[str]:
        ret = await self.interface.get_playback_status()

        return ret.lower() if ret else None

    async def change_state(self, action: str) -> Optional[str]:
        if action == 'play':
            await self.interface.call_play()
        elif action == 'pause':
            await self.interface.call_pause()

        return 'playing' if action == 'play' else 'paused'

    async def get_interface(self) -> ProxyInterface:
        reply = await self.bus.call(Message(
            destination='org.freedesktop.DBus',
            path='/org/freedesktop/DBus',
            interface='org.freedesktop.DBus',
            member='ListNames'
        ))

        first_mpris_bus = None

        for name in reply.body[0]:
            if name.startswith('org.mpris.MediaPlayer2'):
                first_mpris_bus = name

                break

        if not first_mpris_bus:
            raise RuntimeError('No MPRIS2 bus found')

        return self.bus.get_proxy_object(
            first_mpris_bus,
            '/org/mpris/MediaPlayer2',
            await self.bus.introspect(first_mpris_bus, '/org/mpris/MediaPlayer2')
        ).get_interface('org.mpris.MediaPlayer2.Player')


class Properties(Dbus):
    async def get_interface(self) -> ProxyInterface:
        return self.bus.get_proxy_object(
            'org.freedesktop.DBus',
            '/org/freedesktop/DBus',
            await self.bus.introspect('org.freedesktop.DBus', '/org/freedesktop/DBus')
        ).get_interface('org.freedesktop.DBus.Properties')
