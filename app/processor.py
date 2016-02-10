import logging

from plugins.debug_hook import DebugHook
from plugins.lower import LowerCommand
from plugins.upper import UpperCommand
from plugins.print import PrintCommand


def load_plugins(hooks, command_plugins):
    # TODO: dynamically pick up commands and hooks from the plugins directory...
    # For now we hard-code a fake "hook" and 3 fake "commands":
    hooks.extend([DebugHook()])
    command_plugins.extend([LowerCommand(), UpperCommand(), PrintCommand()])


def process_commands(input_obj, commands):
    logging.debug('Processing commands...')

    hook_plugins = []
    command_plugins = []
    load_plugins(hook_plugins, command_plugins)

    for command_str in commands:
        for plugin in command_plugins:
            if command_str in plugin.names:
                for hook in hook_plugins:
                    hook.before_handle(input_obj, plugin)
                input_obj = plugin.handle(input_obj)
                for hook in hook_plugins:
                    hook.after_handle(input_obj, plugin)
