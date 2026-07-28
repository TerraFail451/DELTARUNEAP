from typing import TYPE_CHECKING

from BaseClasses import LocationProgressType
from rule_builder.rules import Has

from worlds.deltarune.Locations import locations, LocationIDs
from worlds.deltarune.Items import items, ItemIDs, glitched_item_name
from worlds.deltarune.LogicHelper import (
    include_hidden_items,
    include_secret_bosses_items_requirement,
    include_secret_bosses_items_reward,
    mysterykey_from_pink_coins,
)
from worlds.deltarune.Rules import have_susie, have_kris_susie_or_ralsei, have_kris

if TYPE_CHECKING:
    from .. import DeltaruneWorld


def set_rules(world: "DeltaruneWorld"):
    if world.is_secret_bosses_items_requirement_randomized():
        world.set_rule(
            world.get_location(locations[LocationIDs.ch5_pinks_shop_4]), Has(items[ItemIDs.pinkcoin], 10)
        )

def handle_locked_items(world: "DeltaruneWorld"):
    if not include_secret_bosses_items_reward(world):
        world.get_location(locations[LocationIDs.ch5_castle_top_pink_defeat]).place_locked_item(
            world.create_item(items[ItemIDs.shadowcrystal])
        )
        world.get_location(locations[LocationIDs.ch5_castle_top_flower_gift_aqua]).place_locked_item(
            world.create_item(items[ItemIDs.aquaknife])
        )
        world.get_location(locations[LocationIDs.ch5_castle_top_flower_gift_blue]).place_locked_item(
            world.create_item(items[ItemIDs.blueshoes])
        )
        world.get_location(locations[LocationIDs.ch5_castle_top_flower_gift_green]).place_locked_item(
            world.create_item(items[ItemIDs.greenapron])
        )
        world.get_location(locations[LocationIDs.ch5_castle_top_flower_gift_yellow]).place_locked_item(
            world.create_item(items[ItemIDs.yellowhat])
        )
        world.get_location(locations[LocationIDs.ch5_castle_top_flower_gift_orange]).place_locked_item(
            world.create_item(items[ItemIDs.ogloves])
        )
        world.get_location(locations[LocationIDs.ch5_castle_top_flower_gift_seth]).place_locked_item(
            world.create_item(items[ItemIDs.sethspecs])
        )
        world.get_location(locations[LocationIDs.ch5_castle_top_flowerys_gift]).place_locked_item(
            world.create_item(items[ItemIDs.floweryscarf])
        )

    if not include_secret_bosses_items_requirement(world):
        world.get_location(locations[LocationIDs.ch5_pinks_shop_4]).place_locked_item(
            world.create_item(items[ItemIDs.pinkkey])
        )
        # pink coins :(
        world.get_location(locations[LocationIDs.ch5_garden_water_can_pink_coin]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_garden_pink_coin_near_tropical_starwalker]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_dark_garden_pink_coin_above_shrine]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_dark_garden_pink_coin_left_of_running_area]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_cliffs_pink_coin_by_rising_vine]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_cliffs_pink_coin_under_falling_water]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_cliffs_wind_platforming_pink_coin]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_cliffs_running_challenge_pink_coin]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_castle_west_shinobeetle_shuriken_pink_coin]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_castle_west_yellow_flower_platforming_pink_coin]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_castle_east_pink_coin_behind_paper_wall]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_castle_east_pink_lantern_pink_coin]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_castle_east_fox_race_pink_coin]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_castle_east_fox_collecting_pink_coin]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_castle_east_terakota_buttons_pink_coin]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_castle_east_mysterious_puzzle_pink_coin]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_castle_east_difficult_shadow_puzzle_pink_coin]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_castle_top_yellow_flower_platforming_pink_coin]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
        world.get_location(locations[LocationIDs.ch5_castle_top_pink_door_pink_coin]).place_locked_item(
            world.create_item(items[ItemIDs.pinkcoin])
        )
    else: 
        if mysterykey_from_pink_coins(world):
            world.get_location(locations[LocationIDs.ch5_pinks_shop_4]).place_locked_item(
                world.create_item(items[ItemIDs.pinkkey])
            )

    # Hidden Items
    if not include_hidden_items(world):
        world.get_location(locations[LocationIDs.ch5_castle_moss]).place_locked_item(
            world.create_item(items[ItemIDs.castle_moss])
        )
        world.get_location(locations[LocationIDs.ch5_cliffs_man]).place_locked_item(
            world.create_item(items[ItemIDs.chapter_5_egg])
        )
        world.get_location(locations[LocationIDs.ch5_castle_top_painting_room_item]).place_locked_item(
            world.create_item(items[ItemIDs.bromidef])
        )
        world.get_location(locations[LocationIDs.ch5_castle_top_annoying_dog]).place_locked_item(
            world.create_item(items[ItemIDs.dogdollar])
        )
