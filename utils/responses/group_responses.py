from enum import StrEnum


class GroupErrorResponses(StrEnum):
    GROUP_NOT_FOUND = 'Group not found'
    GROUP_IS_TAKEN = 'Group is already created'

class GroupResponses(StrEnum):
    GROUP_DELETED = 'Group deleted'