from app.plugin import Command


class UpperCommand(Command):
    @property
    def names(self):
        return ['upper', 'u']

    def handle(self, input_obj):
        return super().handle(input_obj).upper()
