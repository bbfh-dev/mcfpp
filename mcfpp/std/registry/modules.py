from mcfpp.compiler.modules import Score, Entity, requires
from mcfpp.lang import Criteria


@requires(Entity)
class Var(Score):
    player_id = Criteria.dummy(), "PlayerID"
    group_id = Criteria.dummy()


__modules__ = [Var]
