from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.deltarune.Locations import LocationIDs, locations

if TYPE_CHECKING:
    from . import DeltaruneWorld

def set_completion_goal(world: "DeltaruneWorld"):
    locations_goal = []

    if included_chapter(world, 1):
        locations_goal.append(locations[LocationIDs.ch1_fountain_sealed])
    if included_chapter(world, 2):
        locations_goal.append(locations[LocationIDs.ch2_fountain_sealed])
    if included_chapter(world, 3):
        locations_goal.append(locations[LocationIDs.ch3_fountain_sealed])
    if included_chapter(world, 4):
        locations_goal.append(locations[LocationIDs.ch4_third_sanctuary_fountain_sealed])
    if included_chapter(world, 5):
        if world.is_weird_route():
            locations_goal.append(locations[LocationIDs.ch5_weird_route_sinking])
        else:
            locations_goal.append(locations[LocationIDs.ch5_fountain_sealed_2])

    def complete_chapters_goal(state: CollectionState):
        for location in locations_goal:
            if not state.can_reach(location, "Location", world.player):
                return False
        return True

    world.multiworld.completion_condition[world.player] = complete_chapters_goal
