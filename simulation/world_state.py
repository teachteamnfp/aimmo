from client.world_view import WorldView


class WorldState(object):
    def __init__(self, world_map, avatar_manager):
        self.world_map = world_map
        self.avatar_manager = avatar_manager

    def get_state_for(self, avatar):
        return WorldView(avatar, self.world_map, self.avatar_manager)

    # TODO: move to avatar_manager
    def get_avatars_at(self, location):
        return [a for a in self.avatar_manager.avatars if a.location == location]