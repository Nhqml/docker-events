from typing import Callable, Optional

import docker
from docker import DockerClient

from .types import DockerEventCallback, DockerEventFilter


class DockerEventListener:
    filters: set[DockerEventFilter] = set()
    callbacks: dict[str, DockerEventCallback] = {}

    def __init__(self, client: Optional[DockerClient] = None):
        self.client = client or docker.client.from_env()
        self._events = None

    def listen(self):
        """Listen for Docker events."""
        self._events = self.client.events(decode=True)
        for event in self._events:
            event_matches: set[DockerEventFilter] = set()
            # Run all registered filters on the event and save the matching ones
            for filter_ in self.filters:
                if filter_(event):
                    event_matches.add(filter_)

            for cb_func, cb_filters in self.callbacks.values():
                # Get filters relevant to the callback and if they all matched, call the callback
                matches = [filter_ in event_matches for filter_ in cb_filters]
                if all(matches):
                    cb_func(client=self.client, event=event)

    def cancel(self):
        """Cancel listening."""
        if self._events:
            self._events.close()

    @classmethod
    def register_filter(cls, func: DockerEventFilter):
        """Register the functions as an event filter.

        Each registered filter will be tested (and will thus slow down the event handling).
        If you don't want to register filters that will possible be unused, only use `register_callback` since it will
        take care of registering every filter the callback uses.

        Args:
            func (DockerEventFilter): the filter to register.
        """
        cls.filters.add(func)
        return func

    @classmethod
    def register_callback(cls, *, filters=None):
        """Register the function as event callback.

        The function will be called everytime a Docker event matches ALL the associated filters.

        Args:
            filters (Optional[list[DockerEventFilter]]): an optional list of event filters.
        """
        filters = filters or []

        def wrapper(func: Callable[..., None]):
            # Register filters if not already registered
            for filter_ in filters:
                if filter_ not in cls.filters:
                    cls.register_filter(filter_)

            cls.callbacks[func.__name__] = (func, filters)
            return func

        return wrapper
