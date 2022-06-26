from typing import Dict


class RecognizerResult:
    """
    Recognizer Result represents the findings of the detected entity.

    Result of a recognizer analyzing the text.

    :param entity_type: the type of the entity
    :param start: the start location of the detected entity
    :param end: the end location of the detected entity
    :param score: the score of the detection
    :param analysis_explanation: contains the explanation of why this
                                 entity was identified
    """

    def __init__(
        self,
        entity_type: str,
        start: int,
        end: int
    ):

        self.entity_type = entity_type
        self.start = start
        self.end = end

    def to_dict(self) -> Dict:
        """
        Serialize self to dictionary.

        :return: a dictionary
        """
        return self.__dict__

    @classmethod
    def from_json(cls, data: Dict) -> "RecognizerResult":
        """
        Create RecognizerResult from json.

        :param data: e.g. {
            "start": 24,
            "end": 32,
            "entity_type": "NAME"
        }
        :return: RecognizerResult
        """
        entity_type = data.get("entity_type")
        start = data.get("start")
        end = data.get("end")
        return cls(entity_type, start, end)

    def __repr__(self) -> str:
        """Return a string representation of the instance."""
        return self.__str__()

    def intersects(self, other: "RecognizerResult") -> int:
        """
        Check if self intersects with a different RecognizerResult.

        :return: If intersecting, returns the number of
        intersecting characters.
        If not, returns 0
        """
        # if they do not overlap the intersection is 0
        if self.end < other.start or other.end < self.start:
            return 0

        # otherwise the intersection is min(end) - max(start)
        return min(self.end, other.end) - max(self.start, other.start)

    def contained_in(self, other: "RecognizerResult") -> bool:
        """
        Check if self is contained in a different RecognizerResult.

        :return: true if contained
        """
        return self.start >= other.start and self.end <= other.end

    def contains(self, other: "RecognizerResult") -> bool:
        """
        Check if one result is contained or equal to another result.

        :param other: another RecognizerResult
        :return: bool
        """
        return self.start <= other.start and self.end >= other.end

    def equal_indices(self, other: "RecognizerResult") -> bool:
        """
        Check if the indices are equal between two results.

        :param other: another RecognizerResult
        :return:
        """
        return self.start == other.start and self.end == other.end

    def __gt__(self, other: "RecognizerResult") -> bool:
        """
        Check if one result is greater by using the results indices in the text.

        :param other: another RecognizerResult
        :return: bool
        """
        if self.start == other.start:
            return self.end > other.end
        return self.start > other.start

    def __eq__(self, other: "RecognizerResult") -> bool:
        """
        Check two results are equal by using all class fields.

        :param other: another RecognizerResult
        :return: bool
        """
        equal_type = self.entity_type == other.entity_type
        return self.equal_indices(other) and equal_type

    def __hash__(self):
        """
        Hash the result data by using all class fields.

        :return: int
        """
        return hash(
            f"{str(self.start)} {str(self.end)} {self.entity_type}"
        )

    def __str__(self) -> str:
        """Return a string representation of the instance."""
        return (
            f"type: {self.entity_type}, "
            f"start: {self.start}, "
            f"end: {self.end}"
        )

    def has_conflict(self, other: "RecognizerResult") -> bool:
        """
        Check if two recognizer results are conflicted or not.

        I have a conflict if:
        1. My indices are the same as the other and my score is lower.
        2. If my indices are contained in another.

        :param other: RecognizerResult
        :return:
        """
        return other.contains(self)
