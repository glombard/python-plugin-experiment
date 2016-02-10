from app.plugin import Command


class LowerCommand(Command):
    @property
    def names(self):
        return ['lower', 'l']

    def handle(self, input_obj):
        return super().handle(input_obj).lower()
