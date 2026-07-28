from enum import StrEnum
from typing import TYPE_CHECKING

from worlds.deltarune.Locations import LocationData, LocationGroups, LocationIDs
from worlds.deltarune.LogicHelper import (
    should_include_spike_band_fusion,
    should_include_tensionbow_fusion,
    should_include_truetie_fusion,
    should_include_twin_ribbon_fusion,
    should_include_twistedsword_fusion,
)
from worlds.deltarune.Regions import Regions

if TYPE_CHECKING:
    from .. import DeltaruneWorld


cross_chapter_locations: dict = {
    Regions.fusion: [
        LocationData(
            LocationIDs.cc_castle_town_dd_burger_fusion,
            should_be_included=lambda world: world.can_access_fusion(),
            group=LocationGroups.castle_town,
        ),
        LocationData(
            LocationIDs.cc_castle_town_silver_card_fusion,
            should_be_included=lambda world: world.can_access_fusion(),
            group=LocationGroups.castle_town,
        ),
        LocationData(
            LocationIDs.cc_castle_town_twin_ribbon_fusion,
            should_be_included=lambda world: should_include_twin_ribbon_fusion(world),
            group=LocationGroups.castle_town,
        ),
        LocationData(
            LocationIDs.cc_castle_town_spike_band_fusion,
            should_be_included=lambda world: should_include_spike_band_fusion(world),
            group=LocationGroups.castle_town,
        ),
        LocationData(
            LocationIDs.cc_castle_town_tensionbow_fusion,
            should_be_included=lambda world: should_include_tensionbow_fusion(world),
            group=LocationGroups.castle_town,
        ),
        LocationData(
            LocationIDs.cc_castle_town_twistedsword_fusion,
            should_be_included=lambda world: should_include_twistedsword_fusion(world),
            group=LocationGroups.castle_town,
        ),
    ],
    Regions.lost_rabbick: [
        LocationData(
            LocationIDs.cc_lost_rabbick,
            should_be_included=lambda world: (world.include_chapter(3) and world.is_all_routes())
            or (world.include_chapter(1) and world.is_weird_route() and world.is_chapter_1_recruit_system_enabled()),
            group=LocationGroups.cross_chapter,
        ),
    ],
    Regions.ch5_fusion: [
        LocationData(
            LocationIDs.cc_castle_town_monarchrbn_fusion,
            should_be_included=lambda world: world.can_access_ch5_fusion()
            # scarfmark & princessRBN
            and world.include_chapter(4),
            group=LocationGroups.castle_town,
        ),
        LocationData(
            LocationIDs.cc_castle_town_truetie_fusion,
            should_be_included=lambda world: should_include_truetie_fusion(world),
            group=LocationGroups.castle_town,
        ),
        LocationData(
            LocationIDs.cc_castle_town_tvdinner_fusion,
            should_be_included=lambda world: world.can_access_ch5_fusion()
            # tvslop
            and world.include_chapter(3),
            group=LocationGroups.castle_town,
        ),
        LocationData(
            LocationIDs.cc_castle_town_deluxedinner_fusion,
            should_be_included=lambda world: world.can_access_ch5_fusion()
            # tvdinner
            and world.include_chapter(3),
            group=LocationGroups.castle_town,
        ),
        LocationData(
            LocationIDs.cc_castle_town_punchbowl_fusion,
            should_be_included=lambda world: world.can_access_ch5_fusion()
            # Scarlixir & powerband
            and world.include_chapter(4),
            group=LocationGroups.castle_town,
        ),
        LocationData(
            LocationIDs.cc_castle_town_tensionmax_fusion,
            should_be_included=lambda world: world.can_access_ch5_fusion()
            # Scarlixir & mysticband
            and world.include_chapter(4),
            group=LocationGroups.castle_town,
        ),
        LocationData(
            LocationIDs.cc_castle_town_dogwidow_fusion,
            should_be_included=lambda world: world.can_access_ch5_fusion()
            # Goldwidow and dogdollar (no need to check for any more chapters since dogdollar is already in ch4)
            and world.include_chapter(4),
            group=LocationGroups.castle_town,
        ),
    ],
}
