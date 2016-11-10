# python-plugin-experiment

A sample application that shows one potential way to
implement a simple "plugin architecture" in Python.

The app dynamically loads plugins from a directory.
This makes it easy to drop new plugins into the app
by just copying it to the `plugins` directory.

Two types of plugins are supported: commands and hooks.

A command is mapped to a command-line argument.
A command typically takes text input (stdin) and/or
command-line arguments and provides text output
(stdout).

A hook is an "aspect-oriented" type plugin that
could be used for cross-cutting concerns. I.e.,
a hook could be applied to any number of commands.
An example would be a hook that prints/logs the
input or output of a command for debugging purposes.

TODO: separate commands with some delimiter like
':' to allow passing args to each command.

TODO: allow a hook to specify filters for the
commands it should be applied to, e.g. either
by command name or command-line arguments.

TODO: consider getting rid of the base classes
and just use a convention for the command/hook
interfaces.
