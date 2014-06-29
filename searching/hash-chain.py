#-*- coding: utf-8 -*-
class Hash():
    def __init__(self):
        self.size = 20
        self.slots = []
        for i in xrange(0, 20):
            self.slots.append([])

    def __setitem__(self, key, value):
        chain = self.slots[self.hash(key)]
        for data in chain:
            if data[0] == key:
                data[1] = value
                return True
        chain.append([key, value])

    def __getitem__(self, key):
        chain = self.slots[self.hash(key)]
        for data in chain:
            if data[0] == key:
                return data[1]
        return None

    def delete(self, key):
        slot = self.hash(key)
        chain = self.slots[slot]
        for i, data in enumerate(chain):
            if data[0] == key:
                del chain[i]
                return True
        raise ValueError("Key %s if not found." % key)

    def hash(self, key):
        return self.stoi(key) % self.size

    def stoi(self, key):
        inte = 0
        for c in key:
            inte = inte + ord(c)
        return inte

h = Hash()
h["fuck"] = val = {"name": "jerry"}
h["ucfk"] = val2 = {"name": "lucy"}
h["ufck"] = val3 = {"name": "tony"}
h["uckf"] = val4 = {"name": "honey"}

assert h["fuck"] == val
assert h["ucfk"] == val2
assert h["ufck"] == val3
assert h["uckf"] == val4

h["love"] = "you"
h.delete("love")
assert h["love"] == None

h["you"] = "cool"
h["uoy"] = "sucks"
assert h["you"] == "cool"
assert h["uoy"] == "sucks"

h.delete("you")
assert h["you"] == None
h["uoy"] = "Fool"
assert h["uoy"] == "Fool"
