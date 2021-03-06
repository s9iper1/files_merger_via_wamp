from os import environ
import txaio
import aioconsole

from helper import constants

txaio.use_asyncio()
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


class Component(ApplicationSession):
    async def onJoin(self, details):
        # listening for the corresponding message from the "backend"
        # (any session that .publish()es to this topic).
        def onevent(msg):
            print("Got event: {}".format(msg))
        while True:
            command = await aioconsole.ainput(">>> ")
            if command.lower() == "start":
                res = await self.call(constants.file_transfer)
            else:
                print("command not found")
            # call a remote procedure.
            print("Result: {}".format(res))


if __name__ == '__main__':
    runner = ApplicationRunner(
        environ.get("AUTOBAHN_DEMO_ROUTER", "ws://localhost:8080/ws"),
        "realm1",
    )
    runner.run(Component)
