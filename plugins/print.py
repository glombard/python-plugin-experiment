import logging

from app.plugin import Command


class PrintCommand(Command):
    @property
    def names(self):
        return ['print', 'p']

    def handle(self, input_obj):
        result = super().handle(input_obj)
        logging.debug('Print: ' + result)
        return result
