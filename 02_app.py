#!/usr/bin/env python

from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout

kb = KeyBindings()


def print_info():
    """
    Display game help/information.
    """
    print("Display game information")
    print("Game is about having winning Kingdom")
    print("Press CTRL-Q to exit application")
    print("Press CTRL-R to return to app")


@kb.add('i')
def _(event):

    print_info()

    @kb.add('c-r')
    def exit_(event):
        """
        """
        print("Return to game")


@kb.add('c-q')
def exit_(event):
    """
    Pressing Ctrl-Q will exit the user interface.

    Setting a return value means: quit the event loop that drives the user
    interface and return this value from the `Application.run()` call.
    """
    event.app.exit()


root_container = Window(content=FormattedTextControl(text="My Game"))
layout = Layout(root_container)

app = Application(layout=layout, key_bindings=kb, full_screen=True)
app.run()
