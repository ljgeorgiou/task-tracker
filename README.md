# task-tracker

A simple to-do list app that runs in the terminal.

## What it does

The task-tracker keeps a list of things you need to do, and marks whether each one has been completed. The tasks are stored in a JSON file, so they're saved between runs - you can close the program and pick up where you left off.

When you run it, you get a menu with five options:

1. **Show** your tasks - they're listed line by line, with the task and whether it's been completed.
2. **Add** a task to the list.
3. **Delete** a task from the list.
4. **Complete** a task - this marks it as done (the value next to it changes from `[]` to `["X"]`, where the `X` means completed).
5. **Quit** - stops the program.

The menu keeps looping, so you can do as many things as you like until you choose option 5.

## How it saves your tasks

The tasks are kept in a dictionary, where each task is a key and its value shows whether it's done. After every action (adding, deleting, or completing) the program saves the updated dictionary to a JSON file. So the file always holds your latest list.

When you start the program, it checks whether the JSON file already exists. If it does, it loads it back into a dictionary Python can work with, so your old tasks are still there. If it doesn't exist yet (the first time you run it), the program creates an empty one.

## How to run it


Open a terminal in the project folder and run:

python to_do_app.py

Then follow the menu - type a number and press Enter.

## What I found hard

The trickiest part was the menu loop, especially handling bad input. If someone typed a letter instead of a number, the program used to either crash or quietly do nothing. Getting it to notice bad input and just re-ask the question, instead of breaking, took a few attempts. I ended up using a single loop that reads the menu choice, checks it's a valid number, and only then acts on it, which fixed the mess I had with my earlier two-loop version.