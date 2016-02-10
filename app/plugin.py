class PluginBase(object):
    def handle(self, input_obj):
        """
        Handles the input string or object. Transforms the input as necessary and returns the output object
        to be passed on to the next command in the pipeline.
        :param input_obj: any object or string returned by the previous command or stdin
        :return: the object or string to be handled by the next plugin in the pipeline
        """
        return input_obj


class Command(PluginBase):
    @property
    def names(self):
        """
        Returns the name(s) of this plugin. The name is the command-line argument we understand.
        :return: string or list of strings
        """
        return None


class Hook(object):
    """Handles each command value from the cmdline and its corresponding command plugin."""

    def before_handle(self, input_obj, command):
        return input_obj

    def after_handle(self, input_obj, command):
        return input_obj
