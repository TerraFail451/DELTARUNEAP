from BaseClasses import Location
from typing import TYPE_CHECKING

from worlds.deltarune.Locations import LocationData, LocationGroups, LocationIDs
from worlds.deltarune.Regions import Regions

if TYPE_CHECKING:
    from .. import DeltaruneWorld

chapter5_locations = {
    Regions.ch5_mew_mew_shop: [
        LocationData(
            id=LocationIDs.ch5_mew_mew_shop_1,
            group=LocationGroups.chapter5,
        ),
        LocationData(
            id=LocationIDs.ch5_mew_mew_shop_2,
            group=LocationGroups.chapter5,
        ),
        LocationData(
            id=LocationIDs.ch5_mew_mew_shop_3,
            group=LocationGroups.chapter5,
        ),
        LocationData(
            id=LocationIDs.ch5_mew_mew_shop_4,
            group=LocationGroups.chapter5,
        ),
    ],
    Regions.ch5_flower_rewards: [
        LocationData(
            id=LocationIDs.ch5_flower_reward_aqua_item,
            group=LocationGroups.chapter5,
        ),
        LocationData(
            id=LocationIDs.ch5_flower_reward_blue_item,
            group=LocationGroups.chapter5,
        ),
        LocationData(
            id=LocationIDs.ch5_flower_reward_green_item,
            group=LocationGroups.chapter5,
        ),
        LocationData(
            id=LocationIDs.ch5_flower_reward_yellow_item,
            group=LocationGroups.chapter5,
        ),
        LocationData(
            id=LocationIDs.ch5_flower_reward_orange_item,
            group=LocationGroups.chapter5,
        ),
        LocationData(
            id=LocationIDs.ch5_flower_reward_seth_item,
            group=LocationGroups.chapter5,
        ),
        LocationData(
            id=LocationIDs.ch5_flower_reward_flowery_item,
            group=LocationGroups.chapter5,
        ),
    ],
}
