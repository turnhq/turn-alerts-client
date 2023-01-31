from enum import Enum


class AlertTagEnum(str, Enum):
    SCREEN = "screening"
    SOURCE = "sourcing"
    BACKGROUND_CHECK = "background_check"
    METRICS = "metrics"
    CANDIDATE_PROGRESS = "candidate_progress"
