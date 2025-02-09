class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You must be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Your vaccine is outdated, you must update it"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Your must wear a mask"
