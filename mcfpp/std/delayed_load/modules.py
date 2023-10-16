from mcfpp.compiler.modules import Server
from mcfpp.lang import Event


class DelayedLoad(Server):
    dir = "minecraft:(namespace)"

    @Event.function("minecraft:load")
    def load(self, src: Server.Source):
        src.run("if entity @p", "schedule function (this) 2t replace")
        src.run("if !entity @p", "function (namespace):load")


__modules__ = [DelayedLoad]
