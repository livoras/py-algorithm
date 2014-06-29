#-*- coding: utf-8 -*-
class Hash():
    def __init__(self):
        self.size = 20
        self.slots = [None] * 20

    def put(self, key, value):
        slot = self.hash(key)
        data = self.slots[slot]
        if not data or data[0] == key:
            # 0 - to store key, 1 - to store value
            self.slots[slot] = [key, value]
        else:
            next_slot = self.rehash(slot)
            while True:
                if slot == next_slot:
                    raise ValueError("Hashtable is full.")
                data = self.slots[next_slot]
                if not data or data[0] == key:
                    self.slots[next_slot] = [key, value]
                    return True
                next_slot = self.rehash(next_slot)

    def get(self, key):
        return self._get(key)[1] 

    def _get(self, key):
        slot = self.hash(key)
        struct = self.slots[slot]
        if struct and struct[0] == key:
            return slot, struct[1]
        else:
            next_slot = self.rehash(slot)
            while True:
                struct = self.slots[next_slot]
                if next_slot == slot:
                    return -1, None
                if not struct or struct[0] != key:
                    next_slot = self.rehash(next_slot)
                    continue
                return next_slot, struct[1]

    def delete(self, key):
        data = self._get(key)
        if data[0] == -1:
            raise ValueError("Key %s is not found." % key)
        else:
            self.slots[data[0]] = None
            return True

    def hash(self, key):
        return self.stoi(key) % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def stoi(self, key):
        inte = 0
        for c in key:
            inte = inte + ord(c)
        return inte

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


h = Hash()
h["fuck"] = val = {"name": "jerry"}
h["ucfk"] = val2 = {"name": "lucy"}
h["ufck"] = val3 = {"name": "tony"}
h["uckf"] = val4 = {"name": "honey"}

print h["fuck"]
print h["ucfk"]
print h["ufck"]
print h["uckf"]

assert h.slots[h.stoi("fuck") % 20][1] == val
assert h.slots[h.stoi("ucfk") % 20 + 1][1] == val2
assert h.slots[h.stoi("ufck") % 20 + 2][1] == val3
assert h.slots[h.stoi("uckf") % 20 + 3][1] == val4

h.delete("ucfk")
assert h.slots[h.stoi("fuck") % 20 + 1] == None

h.delete("fuck")
assert h.slots[h.stoi("fuck") % 20] == None

iofhello = h.stoi("hello")
h["hello"] = "I am not afraid!"
assert h.slots[iofhello % 20][0] == "hello"

h["oellh"] = "LUC>>>"
assert h.slots[(iofhello + 1) % 20][0] == "oellh"

# Here is a bug, if you delete the one key, then the slot is empty. 
# After that if you insert the key with the same hash value, then there could be duplicated key.
h["hello"] = "I am afraid!"
assert h.slots[iofhello % 20][0] == "hello"
assert h.slots[iofhello % 20][1] == "I am afraid!"

h.delete("hello")
assert h.slots[iofhello % 20] == None

h["oellh"] = "come on!" # --> bug, "oellh" will occur twice in the slots.
assert h.slots[iofhello % 20 + 1][1] == "come on!" # --> assertion fails.
