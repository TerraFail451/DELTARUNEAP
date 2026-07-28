from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import DeltaruneWorld


def include_mike_battle(world: "DeltaruneWorld") -> bool:
    return world.options.include_mike.value in [
        world.options.include_mike.option_battle_only,
        world.options.include_mike.option_battle_and_games,
    ]


def include_hidden_items_chapter2_weird_route_exclusion(world: "DeltaruneWorld") -> bool:
    return include_hidden_items(world) and not weird_route(world)


def include_secret_bosses_items_requirement_chapter2_weird_route_exclusion(world: "DeltaruneWorld") -> bool:
    return include_secret_bosses_items_requirement(world) and not weird_route(world)


def include_chapter1_door_key(world: "DeltaruneWorld") -> bool:
    return include_secret_bosses_items_requirement(world) and world.is_door_key_from_broken_keys()


def include_secret_bosses_items_reward(world: "DeltaruneWorld") -> bool:
    return (
        world.options.randomize_secret_bosses.value == world.options.randomize_secret_bosses.option_true
        or are_secret_bosses_mandatory(world)
    )


def include_secret_bosses_items_reward_chapter2_weird_route_exclusion(world: "DeltaruneWorld") -> bool:
    return include_secret_bosses_items_reward(world) and not weird_route(world)


def include_recruits_chapter1(world: "DeltaruneWorld") -> bool:
    return include_recruits(world) and world.options.chapter_1_recruit.value == 1


def include_lose_recruits_chapter1(world: "DeltaruneWorld") -> bool:
    return include_lose_recruits(world) and world.options.chapter_1_recruit.value == 1


def not_include_lose_recruits(world: "DeltaruneWorld") -> bool:
    return not include_lose_recruits(world)


def include_recruits(world: "DeltaruneWorld") -> bool:
    return world.options.recruits_sanity == True


def include_lose_recruits(world: "DeltaruneWorld"):
    return world.options.lose_recruits_sanity == True


def include_recruits_chapter2_weird_route_exclusion(world: "DeltaruneWorld"):
    return include_recruits(world) and not weird_route(world)


def include_recruit_swatchlings_weird_route(world: "DeltaruneWorld"):
    return include_recruits(world) and (
        world.options.include_swatchling_during_weird_route == True or not weird_route(world)
    )


def should_include_lose_swatchlings_weird_route(world: "DeltaruneWorld"):
    return include_lose_recruits(world) and (
        world.options.include_swatchling_during_weird_route == True or not weird_route(world)
    )


def should_include_twin_ribbon_fusion(world: "DeltaruneWorld"):
    return (
        can_access_fusion(world)
        and any_included_chapter(world, [2, 3])
        and (
            (starting_equipment_removed(world) and world.has_at_least_one_chapter_included([1, 3]))
            or (not starting_equipment_removed(world) and world.has_at_least_one_chapter_included([1, 2, 3]))
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


def include_tensionbow_fusion(world: "DeltaruneWorld"):
    return (
        can_access_fusion(world)
        and included_chapter(world, 2)
        and (not world.is_weird_route() or world.is_all_routes())
    )


def include_twistedsword_fusion(world: "DeltaruneWorld"):
    return (
        can_access_fusion(world) and included_chapter(world, 2) and include_unused_items(world) and weird_route(world)
    )


def include_truetie_fusion(world: "DeltaruneWorld"):
    return (
        can_access_fusion_post_chapter_5(world)
        # frayed bowtie
        and included_chapter(world, 2)
        and not_weird_route(world)
        # tennatie
        and included_chapter(world, 3)
    )


# region Direct Option Read


def weird_route(world: "DeltaruneWorld") -> bool:
    return world.options.chosen_route.value in [
        world.options.chosen_route.option_weird_route,
        world.options.chosen_route.option_both_all_recruits_and_weird_route,
    ]


def not_weird_route(world: "DeltaruneWorld") -> bool:
    return world.options.chosen_route.value != world.options.chosen_route.option_weird_route


def all_recruits_route(world: "DeltaruneWorld") -> bool:
    return world.options.chosen_route.value in [
        world.options.chosen_route.option_all_recruits,
        world.options.chosen_route.option_both_all_recruits_and_weird_route,
    ]


def both_routes(world: "DeltaruneWorld") -> bool:
    return world.options.chosen_route == world.options.chosen_route.option_both_all_recruits_and_weird_route


def include_mike_games(world: "DeltaruneWorld") -> bool:
    return world.options.include_mike.value == world.options.include_mike.option_battle_and_games


def include_mantle(world: "DeltaruneWorld") -> bool:
    return world.options.randomize_mantle.value != world.options.randomize_mantle.option_mantleless


def randomized_mantle(world: "DeltaruneWorld") -> bool:
    return world.options.randomize_mantle.value == world.options.randomize_mantle.option_true


def include_shadow_mantle(world: "DeltaruneWorld") -> bool:
    return world.options.include_shadow_mantle.value == 1


def mysterykey_from_pink_coins(world: "DeltaruneWorld") -> bool:
    return world.options.mysterykey_from_pink_coins.value == 1


def doorkey_from_broken_keys(world: "DeltaruneWorld") -> bool:
    return world.options.door_key_from_broken_keys.value == 1


def include_hidden_items(world: "DeltaruneWorld") -> bool:
    return world.options.include_hidden_items.value == 1


def include_secret_bosses_items_requirement(world: "DeltaruneWorld") -> bool:
    return world.options.include_secret_bosses_items_requirement.value == 1


def are_secret_bosses_mandatory(world: "DeltaruneWorld"):
    return world.options.randomize_secret_bosses.value == world.options.randomize_secret_bosses.option_mandatory


def include_everybodyweapon(world: "DeltaruneWorld") -> bool:
    return world.options.include_unused_items.value == world.options.include_unused_items.option_true


def randomized_chapters(world: "DeltaruneWorld") -> bool:
    return world.options.randomize_chapters.value == world.options.randomize_chapters.option_randomized


def chapters_in_order(world: "DeltaruneWorld") -> bool:
    return world.options.randomize_chapters.value == world.options.randomize_chapters.option_in_order


def all_chapter_unlocked(world: "DeltaruneWorld") -> bool:
    return world.options.randomize_chapters.value == world.options.randomize_chapters.option_all_unlocked


def normal_route(world: "DeltaruneWorld") -> bool:
    return world.options.chosen_route.value == world.options.chosen_route.option_normal_route


def starting_equipment_removed(world: "DeltaruneWorld"):
    return world.options.remove_starting_equipment.value == 1


def progressive_weapons_kris(world: "DeltaruneWorld"):
    return world.options.progressive_kris_weapons.value == 1


def progressive_weapons_susie(world: "DeltaruneWorld"):
    return world.options.progressive_susie_weapons.value == 1


def progressive_weapons_ralsei(world: "DeltaruneWorld"):
    return world.options.progressive_ralsei_weapons.value == 1


def progressive_weapons_noelle(world: "DeltaruneWorld"):
    return world.options.progressive_noelle_weapons.value == 1


def include_characters(world: "DeltaruneWorld"):
    return world.options.unlock_characters.value in [
        world.options.unlock_characters.option_true,
        world.options.unlock_characters.option_except_kris,
    ]


def include_kris(world: "DeltaruneWorld"):
    return world.options.unlock_characters.value == world.options.unlock_characters.option_true


def include_actions(world: "DeltaruneWorld"):
    return world.options.unlock_fun_gang_actions.value == 1


def include_unused_items(world: "DeltaruneWorld") -> bool:
    return world.options.include_unused_items.value in [
        world.options.include_unused_items.option_true,
        world.options.include_unused_items.option_true_without_everybodyweapon,
    ]


def excluded_t_rank(world: "DeltaruneWorld") -> bool:
    return world.options.exclude_t_rank.value == 1


def excluded_z_rank(world: "DeltaruneWorld") -> bool:
    return world.options.exclude_z_rank.value == 1


# endregion

# region Fusion Access


def can_access_fusion(world: "DeltaruneWorld"):
    return any_included_chapter(world, [2, 4, 5])


def can_access_fusion_post_chapter_5(world: "DeltaruneWorld"):
    return any_included_chapter(world, [5])


# endregion


# region Chapter Inclusion


def included_chapter(world: "DeltaruneWorld", chapter: int) -> bool:
    return chapter in world.included_chapters


def any_included_chapter(world: "DeltaruneWorld", chapters: list[int]):
    return any(chapter in world.included_chapters for chapter in chapters)


def all_included_chapter(world: "DeltaruneWorld", chapters: list[int]):
    return all(chapter in world.included_chapters for chapter in chapters)


# endregion
