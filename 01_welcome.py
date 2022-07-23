#!/usr/bin/env python

from prompt_toolkit.shortcuts import (message_dialog, input_dialog,
                                      button_dialog)


def main():
    message_dialog(
        title="Wars Of Kingdoms",
        text="Welcome to Wars of Kingdoms Game!\n\nPress ENTER to proceed.",
    ).run()

    kingdom_name = input_dialog(
        title="Name of Kingdom",
        text="Please name your kingdom:").run()
    print("Kingdom name:", kingdom_name)

    name_correct = button_dialog(
        title="Confirm name of the Kingdom",
        text="Is kingdom name: \'"+kingdom_name+"\' correct?",
        buttons=[
            ("YES ", True),
            ("NO", False),
            ("EXIT", None)
        ],
    ).run()
    print("Selection:", name_correct)

    name_army = button_dialog(
        title="Select Army",
        text="Select which army you would like to play",
        buttons=[
            ("ŻULE", "zule"),
            ("MONIA", "monia")
        ],
    ).run()
    print("Selection:", name_army)


if __name__ == "__main__":
    main()
