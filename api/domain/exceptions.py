class InvalidRollParametersError(ValueError):
    def __init__(self, message: str = "Invalid roll parameters", *, details: dict | None = None) -> None:
        super().__init__(message)
        self.details = details or {}

