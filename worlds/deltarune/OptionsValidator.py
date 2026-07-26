import logging
from typing import TYPE_CHECKING

from Options import OptionError
from worlds.deltarune.Options import ChosenRoute, StartingChapter

if TYPE_CHECKING:
    from . import DeltaruneWorld


def validate_options(world: "DeltaruneWorld"):
    validate_playable_chapters(world)
    validate_starting_chapter(world)
    validate_all_recruits(world)


def validate_playable_chapters(world: "DeltaruneWorld"):
    if len(world.get_playable_chapters()) == 0:
        if world.options.random_safety_chapter_inclusion == True:
            chapter = world.random.randint(1, world.max_deltarune_chapter)
            setattr(world.options, f"include_chapter_{chapter}.value", 1)
            logging.info(
                f"[DELTARUNE] {world.player_name} triggered 'Random Chapter Inclusion Safety'. Chapter {chapter} has been randomly enabled."
            )
        else:
            raise OptionError(
                "You need at least one chapter included. Using all random? Enable 'RANDOM SAFETY : Chapter inclusion' option in your YAML."
            )


def validate_starting_chapter(world: "DeltaruneWorld"):
    if world.is_chapters_randomized() and world.options.starting_chapter != StartingChapter.option_random_chapter:
        if getattr(world.options, f"include_chapter_{world.options.starting_chapter.value}").value == False:
            raise OptionError(
                f"Your random starting chapter is set to {world.options.starting_chapter.value} but it isn't included."
            )


def validate_all_recruits(world: "DeltaruneWorld"):
    if world.options.chosen_route == ChosenRoute.option_all_recruits:
        if not world.recruit_sanity_enabled():
            world.options.recruits_sanity.value = 1
            logging.info(
                f"[DELTARUNE] Recruits Sanity was enabled for {world.player_name} as chosen route is All Recruits."
            )
        if world.lose_recruit_sanity_enabled():
            world.options.lose_recruits_sanity.value = 0
            logging.info(
                f"[DELTARUNE] Lose Recruits Sanity was disabled for {world.player_name} as chosen route is All Recruits."
            )
