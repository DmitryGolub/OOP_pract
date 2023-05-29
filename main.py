class Point:
    def __init__(self, *args):
        self.coords = list(args)
    
    def __getitem__(self, item):
        if 0 <= item < len(self.coords):
            return self.coords[item]
        else:
            raise IndexError("Uncorrect index")
        
    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Index must be integer type")
        if key >= len(self.coords):
            range_off = key - len(self.coords) + 1
            self.coords.extend([None]*range_off)
        
        self.coords[key] = value


class Clock:

    def __init__(self, seconds):
        self.__seconds = seconds
    
    @property
    def seconds(self):
        return self.__seconds
    
    @seconds.setter
    def seconds(self, data):
        self.__seconds = data
    
    @seconds.deleter
    def seconds(self):
        del self.__seconds
    
    def __add__(self, other):
        self.check_type_obeject(other)
        if type(other) == Clock:
            return Clock(self.__seconds + other.__seconds)
        return Clock(self.__seconds + other)
    
    def __radd__(self, other):
        self.check_type_obeject(other)
        if type(other) == Clock:
            return Clock(self.__seconds + other.__seconds)
        return Clock(self.__seconds + other)
    
    def __iadd__(self, other):
        self.check_type_obeject(other)
        if type(other) == Clock:
            return Clock(self.__seconds + other.__seconds)
        return Clock(self.__seconds + other)
    
    def __eq__(self, other):
        self.check_type_obeject(other)
        if type(other) == Clock:
            return self.__seconds == other.__seconds
        return self.__seconds == other
    
    def __lt__(self, other):
        self.check_type_obeject(other)
        if type(other) == Clock:
            return self.__seconds < other.__seconds
        return self.__seconds < other
    
    def __le__(self, other):
        self.check_type_obeject(other)
        if type(other) == Clock:
            return self.__seconds <= other.__seconds
        return self.__seconds <= other
    
    def __hash__(self):
        return hash(self.__seconds)
    
    def get_data(self):
        second = self.__seconds % 60 
        minut = (self.__seconds // 60) % 60 
        hour = (self.__seconds // 3600) % 24
        day = (self.__seconds // 3600) // 24
        if day:
            return f"{self.formated(day)} day {self.formated(hour)}:{self.formated(minut)}:{self.formated(second)}"
        return f"{self.formated(hour)}:{self.formated(minut)}:{self.formated(second)}"

    @classmethod
    def formated(cls, item):
        return str(item).rjust(2, "0")
    
    @classmethod
    def check_type_obeject(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Uncorrect type object")
    
    def __len__(self):
        return len(str(self.__seconds))
    
    def __bool__(self):
        return True if self.__seconds != 0 else False


class FRange:
    
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step
    
    def __iter__(self):
        self.value = self.start - self.step
        return self
    
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

