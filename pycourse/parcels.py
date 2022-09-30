"""
马云飞
2020118092
"""


class Parcel:
    def __init__(self, p_weight, p_dimensions, p_contents, p_breakable):
        self._weight = p_weight  # weight in KG (float)
        self._dimensions = p_dimensions  # dimensions (length, width, height), all in Metres - tuple containing 3 floats
        self._contents = p_contents  # contents (string)
        self._breakable = p_breakable  # breakable (boolean)

    def __str__(self):
        return ('Weight: %fKg, Dimensions(length, width, height): %smeters, Contents: %s, Breakable: %s' % (
            self.weight, self.dimensions, self.contents, self.breakable))

    def __add__(self, other):
        return self.weight + other.weight

    def limit(self):
        return True

    @property
    def weight(self):
        return self._weight

    @property
    def dimensions(self):
        return self._dimensions

    @property
    def contents(self):
        return self._contents

    @property
    def breakable(self):
        return self._breakable

    # ------------------------------------------------------------------------------------------------------

    @weight.setter
    def weight(self, value):
        self._weight = value

    @dimensions.setter
    def dimensions(self, value):
        self._dimensions = value

    @contents.setter
    def contents(self, value):
        self._contents = value

    @breakable.setter
    def breakable(self, value):
        self._breakable = value


# subclasses of Parcel
class Jingdong(Parcel):
    def __init__(self, p_weight, p_dimensions, p_contents, p_breakable):
        super().__init__(p_weight, p_dimensions, p_contents, p_breakable)
        if not self.limit():
            print('Limit Exceeded! length+width+height more than 1.0 meter.')
            del self  # if the instance exceeds the limit,delete it.

    #  if the limits are not complied with,return False
    def limit(self):
        return True if (self.dimensions[0] + self.dimensions[1] + self.dimensions[2] < 1.0) else False

    @Parcel.dimensions.setter
    def dimensions(self, value):
        if value[0] + value[1] + value[2] < 1.0:
            self._dimensions = value
        else:
            print('Dimensions Exceed Limits!')


# subclasses of Parcel
class ChinaPost(Parcel):
    def __init__(self, p_weight, p_dimensions, p_contents, p_breakable):
        super().__init__(p_weight, p_dimensions, p_contents, p_breakable)
        if not self.limit():
            print('Limit Exceeded! Contents is food or are breakable things.')
            del self  # if the instance exceeds the limit,delete it.

    #  if the limits are not complied with,return False
    def limit(self):
        return True if (self.contents != 'food' and self.breakable is False) else False

    @Parcel.contents.setter  # overrides contents' setter from Parcel
    def contents(self, value):
        if value != 'food':
            self._contents = value
        else:
            print('Contents Cannot be Food!')

    @Parcel.breakable.setter  # overrides breakable's setter from Parcel
    def breakable(self, value):
        if not value:
            self._contents = value
        else:
            print('Contents Cannot be Breakable!')


# subclasses of Parcel
class DHL(Parcel):
    def __init__(self, p_weight, p_dimensions, p_contents, p_breakable):
        super().__init__(p_weight, p_dimensions, p_contents, p_breakable)
        if not self.limit():
            print('Limit Exceeded! Weight more than 10kg or length+width+height more than 1.2 meters.')
            del self  # if the instance exceeds the limit,delete it.

    #  if the limits are not complied with,return False
    def limit(self):
        return True if (
                self._weight < 10 and self.dimensions[0] + self.dimensions[1] + self.dimensions[2] < 1.2) else False

    @Parcel.weight.setter  # overrides weight's setter from Parcel
    def weight(self, value):
        if value < 10:
            self._weight = value
        else:
            print('Weight must be less than 10!')

    @Parcel.dimensions.setter  # overrides dimensions' setter from Parcel
    def dimensions(self, value):
        if value[0] + value[1] + value[2] < 1.2:
            self._dimensions = value
        else:
            print('Dimensions Exceed Limits!')


"""
>>> from parcels import *
>>> jd = Jingdong(3, (0.1, 0.1, 0.1), 'food', False)
>>> cp = ChinaPost(4, (0.1, 0.1, 0.1), 'shirt', False)
>>> dhl = DHL(5, (0.1, 0.1, 0.1), 'shirt', False)
>>> print(str(jd), '\n', str(cp), '\n', str(dhl))
Weight: 3.000000Kg, Dimensions(length, width, height): (0.1, 0.1, 0.1)meters, Contents: food, Breakable: False 
Weight: 4.000000Kg, Dimensions(length, width, height): (0.1, 0.1, 0.1)meters, Contents: shirt, Breakable: False 
Weight: 5.000000Kg, Dimensions(length, width, height): (0.1, 0.1, 0.1)meters, Contents: shirt, Breakable: False
>>> jd.dimensions = (1, 1, 1)
Dimensions Exceed Limits!
>>> cp.contents = 'food'
Contents Cannot be Food!
>>> cp.breakable = True
Contents Cannot be Breakable!
>>> dhl.weight = 11
Weight must be less than 10!
>>> dhl.dimensions = (1, 1, 1)
Dimensions Exceed Limits!
>>> print(jd + cp)
7
"""
