from enum import IntEnum,Enum

class GenderType(Enum):
  MALE = 'male'
  FEMALE = 'female'
  OTHER = 'other'
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]


class AppointmentStatus(Enum):
  SCHEDULED = 'scheduled'
  COMPLETED = 'completed'
  CANCELLED = 'cancelled'
  MISSED = 'missed'

  @classmethod
  def choices(cls):
    return [(key.value , key.name) for key in cls]



class DoctorType(Enum):
  PRIMARY_CARE = 'primary care'
  CONSULTANT = 'consultant'
  SPECIALIST = 'specialist'

  @classmethod
  def choices(cls):
    return [(key.value , key.name) for key in cls]


class AppointmentType(Enum):
  LOW = 'low'
  MEDIUM = 'medium'
  HIGH = 'high'

  @classmethod
  def choices(cls):
    return [(key.value , key.name) for key in cls]
  
