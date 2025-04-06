from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class Status(Enum):
    ALLOW = "ALlOW"
    DENY = "DENY"


@dataclass
class RateLimiter:
    capacity: int = 10
    bucket: dict = field(default_factory=dict)
    decision: Status = Status.DENY
    fill_timer: dict = field(default_factory=dict)

    def create_bucket(self, customer_id):
        try:
            if customer_id not in self.bucket:
                self.bucket[customer_id] = 1
                return True
            else:
                print(f"{customer_id} exists in the bucket alread")
                return False
        except Exception as e:
            print(e.__class__)
            return False

    def send_traffic(self, customer_id):
        if customer_id in self.bucket and self.bucket[customer_id] < self.capacity:
            self.bucket[customer_id] += 1
            if self.bucket[customer_id] == self.capacity:
                self.fill_timer[customer_id] = datetime.now.strftime("%Y%m%d%H%M%S")
                return Status.ALLOW
        elif customer_id in self.bucket and self.bucket[customer_id] >= self.capacity:
            current_time = datetime.now.strftime("%Y%m%d%H%M%S")
            time_difference = current_time - self.fill_timer[customer_id]
            time_difference_minutes = time_difference.total_seconds() / 60
            if time_difference_minutes < 60:
                return Status.DENY
            else:
                self.bucket[customer_id] = 0
                self.fill_timer.pop(customer_id)
                return Status.ALLOW
        else:
            self.bucket[customer_id] = 1
            return Status.ALLOW







