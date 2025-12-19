class Locker:
    def __init__(self, locker_id: str, size: int):
        # your code here
        pass
  
class Package:
    def __init__(self, package_id: str, size: int):
        # your code here
        pass
  
class PickupLocation:
    def __init__(self, lockers: List[Locker]):
        # your code here
        pass
  
    def findAndAllocate(self, package: Package) -> Optional[str]:
        # your code here
        pass
  
    def releaseLocker(self, locker_id: str) -> bool:
        # your code here
        pass

    def checkLockerStatus(self, locker_id: str) -> bool:
        # your code here
        pass
  
  
# Your PickupLocation object will be instantiated and invoked:
# lockers = [Locker("L1", 10), Locker("L2", 20), ...]
# pickup = PickupLocation(lockers)
# allocated_id = pickup.findAndAllocate(Package("P100", 15))
# success = pickup.releaseLocker("L1")
# is_occupied = pickup.checkLockerStatus("L2")

