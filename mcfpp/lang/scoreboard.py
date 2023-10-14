from mcfpp.lib.nbt import NBT
from .units import UIColor


class Criteria:
    def __init__(self, value: str):
        self.value = value

    @classmethod
    def dummy(cls):
        return Criteria("dummy")

    @classmethod
    def trigger(cls):
        return Criteria("trigger")

    @classmethod
    def death_count(cls):
        return Criteria("deathCount")

    @classmethod
    def player_kill_count(cls):
        return Criteria("playerKillCount")

    @classmethod
    def total_kill_count(cls):
        return Criteria("totalKillCount")

    @classmethod
    def health(cls):
        return Criteria("health")

    @classmethod
    def xp(cls):
        return Criteria("xp")

    @classmethod
    def level(cls):
        return Criteria("level")

    @classmethod
    def food(cls):
        return Criteria("food")

    @classmethod
    def air(cls):
        return Criteria("air")

    @classmethod
    def armor(cls):
        return Criteria("armor")

    @classmethod
    def custom(cls, value: str):
        return Criteria(f"minecraft.custom:minecraft.{value}")

    @classmethod
    def teamkill(cls, team: UIColor):
        return Criteria(f"teamkill.{team.value}")

    @classmethod
    def killed_by_team(cls, team: UIColor):
        return Criteria(f"killedByTeam.{team.value}")

    @classmethod
    def mined(cls, block_id: str):
        return Criteria(f"minecraft.mined:minecraft.{block_id}")

    @classmethod
    def broken(cls, item_id: str):
        return Criteria(f"minecraft.broken:minecraft.{item_id}")

    @classmethod
    def crafted(cls, item_id: str):
        return Criteria(f"minecraft.crafted:minecraft.{item_id}")

    @classmethod
    def used(cls, item_id: str):
        return Criteria(f"minecraft.used:minecraft.{item_id}")

    @classmethod
    def picked_up(cls, item_id: str):
        return Criteria(f"minecraft.picked_up:minecraft.{item_id}")

    @classmethod
    def dropped(cls, item_id: str):
        return Criteria(f"minecraft.dropped:minecraft.{item_id}")

    @classmethod
    def killed(cls, entity_id: str):
        return Criteria(f"minecraft.killed:minecraft.{entity_id}")

    @classmethod
    def killed_by(cls, entity_id: str):
        return Criteria(f"minecraft.killed_by:minecraft.{entity_id}")


class Scoreboard:
    class Operation:
        def __init__(self):
            pass

    def __init__(self, criteria: Criteria, /, name: str = None, display: str = None):
        self._criteria = criteria
        self._name = name
        self._display = display
        self.target = "@s"
        self._operations: list[Scoreboard.Operation] = []

    def of(self, selector: str):
        self.target = selector
        return self

    @property
    def name(self):
        if self._name is None:
            return ""
        return NBT.string(self._name)
