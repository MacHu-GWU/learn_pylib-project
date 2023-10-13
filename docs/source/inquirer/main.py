# -*- coding: utf-8 -*-

import re
from pprint import pprint

import inquirer


class Example:
    def text(self):
        questions = [
            inquirer.Text(
                "name",
                message="What's your name",
            ),
            inquirer.Text(
                "surname",
                message="What's your surname",
            ),
            inquirer.Text(
                "phone",
                message="What's your phone number",
                validate=lambda _, x: re.match("\+?\d[\d ]+\d", x),
            ),
        ]
        answers = inquirer.prompt(questions)
        print(answers)

    def text_autocomplete(self):
        suggestions = ["inquirer", "hello", "world", "foo", "bar", "baz", "qux"]

        def autocomplete_fn(_text, state):
            # Every time the user presses TAB, we'll switch to the next suggestion
            # The `state` variable contains the index of the current suggestion
            # We can wrap it around to the first suggestion if we reach the end
            print([_text, state])
            return suggestions[state % len(suggestions)]

        questions = [
            inquirer.Text(
                "name",
                message="Press TAB to cycle through suggestions",
                autocomplete=autocomplete_fn,
            ),
        ]

        answers = inquirer.prompt(questions)

        print(answers)

    def editor(self):
        questions = [inquirer.Editor("long_text", message="Provide long text")]
        answers = inquirer.prompt(questions)
        print(answers)

    def list(self):
        questions = [
            inquirer.List(
                "size",
                message="What size do you need?",
                choices=["Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
            ),
        ]
        answers = inquirer.prompt(questions)
        print(answers)

    def list_carousel(self):
        questions = [
            inquirer.List(
                "size",
                message="What size do you need?",
                choices=["Jumbo", "Large", "Standard"],
                carousel=True,
            ),
        ]
        answers = inquirer.prompt(questions)
        pprint(answers)

    def list_autocomplete(self):
        questions = [
            inquirer.List(
                "size",
                message="What size do you need?",
                choices=["Jumbo", "Large", "Standard"],
                autocomplete=True,
            ),
        ]
        answers = inquirer.prompt(questions)
        pprint(answers)

    def checkbox(self):
        questions = [
            inquirer.Checkbox(
                "interests",
                message="What are you interested in?",
                choices=[
                    "Computers",
                    "Books",
                    "Science",
                    "Nature",
                    "Fantasy",
                    "History",
                ],
            ),
        ]
        answers = inquirer.prompt(questions)
        print(answers)

    def path(self):
        questions = [
            inquirer.Path(
                "log_file",
                message="Where logs should be located?",
                path_type=inquirer.Path.DIRECTORY,
            ),
        ]
        answers = inquirer.prompt(questions)
        print(answers)


example = Example()

example.text()
example.text_autocomplete()
example.editor()
example.list()
example.list_carousel()
example.list_autocomplete()
example.checkbox()
example.path()
