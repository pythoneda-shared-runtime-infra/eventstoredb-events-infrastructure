# vim: set fileencoding=utf-8
"""
pythoneda/shared/runtime/infrastructure/events/infrastructure/eventstoredb/dbus/__init__.py

This file ensures pythoneda.shared.runtime.infrastructure.events.infrastructure.eventstoredb.dbus is a namespace.

Copyright (C) 2024-today rydnr's pythoneda-shared-runtime-infrastructure/eventstoredb-events-infrastructure

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
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

DBUS_PATH = "/pythoneda/runtime/infrastructure/eventstoredb"

from .eventstoredb_dbus_booted import EventstoredbDbusBooted
from .eventstoredb_dbus_boot_requested import EventstoredbDbusBootRequested

# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
