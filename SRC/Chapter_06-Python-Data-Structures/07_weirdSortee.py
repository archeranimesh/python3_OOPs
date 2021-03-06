class WierdSortee(object):
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        return "{}:{}".format(self.string, self.number)


if __name__ == "__main__":
    a = WierdSortee("a", 4, True)
    b = WierdSortee("b", 3, True)
    c = WierdSortee("c", 2, True)
    d = WierdSortee("d", 1, True)

    l = [a, b, c, d]
    print(l)
    l.sort()
    print(l)
    for i in l:
        i.sort_num = False

    print(l)
    l.sort()
    print(l)
