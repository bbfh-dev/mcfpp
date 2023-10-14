from mcfpp.compiler.modules import Score
from mcfpp.lang import Criteria


class Var(Score):
    player_id = Criteria.dummy(), "PlayerID"
    group_id = Criteria.dummy()


__modules__ = [Var]
