import txaio

from helper import constants

txaio.use_asyncio()
from os import environ
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

current_status = False


class Component(ApplicationSession):

    async def onJoin(self, details):
        # a remote procedure; see frontend.py for a Python front-end
        # that calls this. Any language with WAMP bindings can now call
        # this procedure if its connected to the same router and realm.

        def start_transfer():
            print('command received')
            if not current_status:
                await self.publish(constants.ready_file, constants.ready_for_file)
            return 'incoming.....'

        file_transfer = await self.register(start_transfer, constants.file_transfer)


if __name__ == '__main__':
    runner = ApplicationRunner(
        environ.get("AUTOBAHN_DEMO_ROUTER", "ws://localhost:8080/ws"),
        "realm1",
    )
    runner.run(Component)
