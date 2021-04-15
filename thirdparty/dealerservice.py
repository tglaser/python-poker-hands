import time
from typing import List


class DealerService:
    hands = [
        ["H2", "PK", "PD", "C10", "H6"],
        ["PA", "H3", "K3", "C3", "CB"],
        ["K3", "CD", "PK", "HA", "K10"],
        ["P7", "H5", "H7", "K9", "KK"],
        ["C9", "C10", "CA", "C4", "CK"],
        ["H10", "K2", "CD", "P3", "PK"],
        ["K6", "KK", "KD", "P9", "PK"],
        ["KA", "CK", "KD", "P10", "C7"],
        ["C8", "K8", "C4", "P8", "H8"]
    ]

    def dealRandomHand(self) -> List[str]:
        index = int(str(self._getTimeStamp())[-1]) - 1
        return DealerService.hands[index]

    @staticmethod
    def _getTimeStamp() -> float:
        return time.time()