from enum import IntEnum

class GenderType(IntEnum):
  MALE = 1
  FEMALE = 2
  OTHER = 3
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]


class AppointmentStatus(IntEnum):
  SCHEDULED = 1
  COMPLETED = 2
  CANCELLED = 3

  @classmethod
  def choices(cls):
    return [(key.value , key.name) for key in cls]



class DoctorType(IntEnum):
  PRIMARY_CARE = 1
  CONSULTANT = 2
  SPECIALIST = 3

  @classmethod
  def choices(cls):
    return [(key.value , key.name) for key in cls]


class AppointmentType(IntEnum):
  LOW = 1
  MEDIUM = 2
  HIGH = 3

  @classmethod
  def choices(cls):
    return [(key.value , key.name) for key in cls]
  
