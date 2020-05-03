class InvalidSpreadError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'InvalidSpreadError: {0}'.format(self.message)
        else:
            return 'InvalidSpreadError has been raised'