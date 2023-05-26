# pleroma.py - pleroma specific endpoints

from .internals import Mastodon as Internals
from .errors import MastodonIllegalArgumentError


class Mastodon(Internals):

    ##
    # Writing data: Notifications
    ##
    def notifications_read(self, id: int = None, max_id: int = None):
        """
        Mark notification(s) as read. Pass one of `id` or `max_id` (mutually
        exclusive)
        """

        key = "id"

        if max_id is not None:
            id = max_id
            key = "max_id"
        elif id is None:
            raise MastodonIllegalArgumentError(
                "Please specify either id or max_id")

        params = {key: id}
        return self.__api_request(
            "POST",
            "/api/v1/pleroma/notifications/read",
            params=params,
        )
