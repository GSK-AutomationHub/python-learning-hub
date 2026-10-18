"Factory Use Case Example Code"

from chair_factory import ChairFactory

# The Client
CHAIR = ChairFactory.get_chair("MediumChair")
print(CHAIR.get_dimensions())
