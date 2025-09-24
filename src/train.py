# src/train.py

class Train:
    def __init__(self):
        self._cars = []

    def attach_front(self, cid: str):
        """Attach a car to the front (left)."""
        self._cars.insert(0, cid)

    def attach_back(self, cid: str):
        """Attach a car to the back (right)."""
        self._cars.append(cid)

    def detach_front(self):
        """Remove and return the front car, or None if empty."""
        if self._cars:
            return self._cars.pop(0)
        return None

    def detach_back(self):
        """Remove and return the back car, or None if empty."""
        if self._cars:
            return self._cars.pop()
        return None

    def detach(self, cid: str) -> bool:
        """
        Remove the first occurrence of the given car ID.
        Return True if removed, False if not found.
        """
        if cid in self._cars:
            self._cars.remove(cid)
            return True
        return False

    def to_list(self):
        """Return a copy of the current list of car IDs."""
        return list(self._cars)  # ✅ must have return
