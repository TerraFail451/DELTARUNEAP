from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import DeltaruneWorld


def should_include_recruits_chapter1(world: "DeltaruneWorld"):
    return world.is_chapter_1_recruit_system_enabled() and world.recruit_sanity_enabled()


def should_include_lose_recruits_chapter1(world: "DeltaruneWorld"):
    return world.is_chapter_1_recruit_system_enabled() and world.lose_recruit_sanity_enabled()


def should_include_twin_ribbon_fusion(world: "DeltaruneWorld"):
    return (
        world.can_access_fusion()
        and world.has_at_least_one_chapter_included([2, 3])
        and (
            (world.is_starting_equipment_removed() and world.has_at_least_one_chapter_included([1, 3]))
            or (not world.is_starting_equipment_removed() and world.has_at_least_one_chapter_included([1, 2, 3]))
        )
    )


def should_include_spike_band_fusion(world: "DeltaruneWorld"):
    return (
        world.can_access_fusion()
        and world.include_chapter(1)
        and (
            world.include_chapter(2)
            or (
                not world.is_starting_equipment_removed()
                and (world.include_chapter(4) or world.have_all_chapters_included([3, 4]))
            )
        )
    )


def should_include_tensionbow_fusion(world: "DeltaruneWorld"):
    return (
        world.can_access_fusion() and world.include_chapter(2) and (not world.is_weird_route() or world.is_all_routes())
    )


def should_include_twistedsword_fusion(world: "DeltaruneWorld"):
    return (
        world.can_access_fusion()
        and world.include_chapter(2)
        and world.is_unused_items_included()
        and world.is_weird_route()
    )


def should_include_truetie_fusion(world: "DeltaruneWorld"):
    return (
        world.can_access_ch5_fusion()
        # frayed bowtie
        and world.include_chapter(2)
        and world.is_not_weird_route_only()
        # tennatie
        and world.include_chapter(3)
    )
