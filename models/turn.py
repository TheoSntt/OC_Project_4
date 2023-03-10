"""Define the Turn Object."""


import time


class Turn:
    """Turn objects are nested in the turns_list variable of the Tournament."""
    def __init__(self, name, matches, start_time=time.time(), end_time=None):
        """Has a name, start_time, end_time, and includes a list of matches."""
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = matches

    def __str__(self):
        """Used in print."""
        out_str = ""
        if self.end_time is None:
            out_str += f"{self.name}, débuté à {self.start_time}\nEN COURS\n"
        else:
            out_str += f"{self.name} : {self.start_time} - {self.end_time}\n"
        for match in self.matches:
            out_str += f"{str(match)}\n"
        return out_str

    def to_json(self):
        """Used to write turn to JSON."""
        turn = {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": []
        }
        for match in self.matches:
            turn['matches'].append(match.to_json())

        return turn
