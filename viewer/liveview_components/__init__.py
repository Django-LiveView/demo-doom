from . import doom_streamer  # noqa
from liveview import liveview_registry

# Force register handlers
liveview_registry.register("start_doom")(doom_streamer.start_doom)
liveview_registry.register("stop_doom")(doom_streamer.stop_doom)
liveview_registry.register("move_forward")(doom_streamer.move_forward)
liveview_registry.register("turn_left")(doom_streamer.turn_left)
liveview_registry.register("turn_right")(doom_streamer.turn_right)
liveview_registry.register("shoot")(doom_streamer.shoot)
