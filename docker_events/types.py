from collections.abc import Callable

DockerEvent = dict
DockerEventFilter = Callable[[DockerEvent], bool]
DockerEventCallback = tuple[Callable[..., None], list[DockerEventFilter]]
