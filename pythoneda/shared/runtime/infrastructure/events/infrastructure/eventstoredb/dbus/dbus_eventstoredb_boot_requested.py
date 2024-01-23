# vim: set fileencoding=utf-8
"""
pythoneda/shared/runtime/events/lifecycle/infrastructure/dbus/dbus_eventstoredb_boot_requested.py

This file defines the DbusEventstoredbBootRequested class.

Copyright (C) 2023-today rydnr's pythoneda-shared-runtime-infrastructure/eventstoredb-events-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import Message
from dbus_next.service import ServiceInterface, signal
import json
from pythoneda.shared import BaseObject
from pythoneda.shared.runtime.infrastructure.events.eventstoredb import (
    EventstoredbEventstoredbBootRequested,
)
from pythoneda.shared.runtime.infrastructure.events.eventstoredb.infrastructure.dbus import (
    DBUS_PATH,
)
from typing import Dic, List


class DbusEventstoredbEventstoredbBootRequested(BaseObject, ServiceInterface):
    """
    D-Bus interface for EventstoredbBootRequested.

    Class name: DbusEventstoredbBootRequested

    Responsibilities:
        - Define the d-bus interface for the EventstoredbBootRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusEventstoredbBootRequested.
        """
        super().__init__(
            "Pythoneda_Shared_Runtime_Infrastructure_Events_Eventstoredb_EventstoredbBootRequested"
        )

    @signal()
    def EventstoredbBootRequested(self, options: "s"):
        """
        Defines the EventstoredbBootRequested d-bus signal.
        :param options: The EventStoreDB options.
        :type options: Dict
        """
        pass

    @classmethod
    def path(cls) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    @classmethod
    def transform(cls, event: EventstoredbBootRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.runtime.infrastructure.events.eventstoredb.EventstoredbBootRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            json.dumps(event.options),
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: EventstoredbBootRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.runtime.infrastructure.events.eventstoredb.EventstoredbBootRequested
        :return: The signature.
        :rtype: str
        """
        return "sss"

    @classmethod
    def parse(cls, message: Message) -> EventstoredbBootRequested:
        """
        Parses given d-bus message containing a EventstoredbBootRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The EventstoredbBootRequested event.
        :rtype: pythoneda.shared.runtime.infrastructure.events.eventstoredb.EventstoredbBootRequested
        """
        options, event_id, prev_event_ids = message.body
        return EventstoredbBootRequested(
            json.loads(options),
            None,
            event_id,
            json.loads(prev_event_ids),
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
