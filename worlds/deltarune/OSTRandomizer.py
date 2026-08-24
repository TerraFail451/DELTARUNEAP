from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import DeltaruneWorld

ost_name = [""]


def randomizeOST(world: "DeltaruneWorld"):
    randomized = {}

    left_to_pick = ost_name

    for ost in ost_name:
        chosen = world.random.choice(left_to_pick)
        randomized[ost] = chosen
        left_to_pick.remove(chosen)

    return randomized
