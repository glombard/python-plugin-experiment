import logging

from app.plugin import Hook


class DebugHook(Hook):
    def after_handle(self, input_obj, command):
        """Prints each plugin name and its input value."""
        result = super().before_handle(input_obj, command)
        plugin_type = type(command)
        logging.debug("Debug - value after plugin '{}': {}".format(plugin_type, result))
        return result
