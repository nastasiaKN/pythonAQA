class Diamond:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == 'side_a':
            if value <= 0:
                raise ValueError('Side length must be greater than 0.')
            super().__setattr__(key, value)

        elif key == 'angle_a':
            if not (0 < value < 180):
                raise ValueError('Angle must be greater than 0 and less than 180 degrees.')
            super().__setattr__(key, value)

            super().__setattr__('angle_b', 180 - value)

        elif key == 'angle_b':

            raise AttributeError('Cannot set angle_b directly. It is automatically calculated from angle_a.')

        else:
            super().__setattr__(key, value)

    def __str__(self):
        return (f'Diamond with side a = {self.side_a}, '
                f'angle_a = {self.angle_a}°, '
                f'angle_b = {self.angle_b}°')

diamond_figure = Diamond(10, 60)
print(diamond_figure)