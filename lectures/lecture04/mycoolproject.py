def my_func():
    """Example function."""

    return "Hello World!"

class example_class:
    """An example class which does nothing much"""

    def __init__(self, *args, **kwargs):
        self.data = args, kwargs

    def do_nothing(self):
        """Function does absolutely nothing."""
        pass

    def do_a_little(self, val):
        """Function does a little.
        
        Parameters
        ----------
        
        val: number
        
        Returns
        number : val**val"""

        return val**val