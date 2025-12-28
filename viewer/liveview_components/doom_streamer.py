import time
import threading
import numpy as np
import random
import vizdoom
from vizdoom import DoomGame, ScreenResolution, ScreenFormat, Mode
from PIL import Image
from django.template.loader import render_to_string
from liveview import liveview_handler, send

# Global game state
game_instances = {}
game_threads = {}
running_games = {}
width = 100
height = 100


def init_doom():
	"""Initialize ViZDoom game"""
	game = DoomGame()
	game.set_doom_game_path("/tmp/doom1.wad")
	game.set_doom_map("E1M1")
	game.set_screen_resolution(ScreenResolution.RES_320X240)
	game.set_screen_format(ScreenFormat.RGB24)
	game.set_render_hud(False)
	game.set_render_minimal_hud(False)
	game.set_render_crosshair(False)
	game.set_render_weapon(True)
	game.set_render_decals(False)
	game.set_render_particles(False)
	game.set_window_visible(False)
	game.set_mode(Mode.PLAYER)
	game.set_available_buttons([
		vizdoom.Button.MOVE_FORWARD,
		vizdoom.Button.TURN_LEFT,
		vizdoom.Button.TURN_RIGHT,
		vizdoom.Button.ATTACK,
	])
	game.init()
	return game


def game_loop(consumer, room):
	"""Game loop running in background thread"""
	global running_games, game_instances

	game = game_instances.get(room)
	if not game:
		return

	while running_games.get(room, False):
		try:
			if game.is_episode_finished():
				game.new_episode()

			# Execute no action by default
			game.make_action([0, 0, 0, 0], 1)
			state = game.get_state()

			if state:
				# Get screen buffer and resize
				screen_buffer = state.screen_buffer

				# Resize frame
				img = Image.fromarray(screen_buffer)
				img = img.resize((width, height), Image.Resampling.NEAREST)
				frame = np.array(img)

				# Convert frame to pixel colors
				pixels = []
				for y in range(height):
					for x in range(width):
						r, g, b = frame[y, x]
						color = f"rgb({r},{g},{b})"
						pixels.append(color)

				# Render HTML
				html = render_to_string(
					"doom_pixel_component.html",
					{"pixels": pixels, "width": width, "height": height},
				)

				# Broadcast update to all clients
				send(consumer, {"target": "#doom-container", "html": html}, broadcast=True)

			time.sleep(0.0167)  # ~60 FPS

		except Exception as e:
			print(f"Error in game loop: {e}")
			time.sleep(1)

	# Cleanup
	if room in game_instances:
		game_instances[room].close()
		del game_instances[room]


@liveview_handler("start_doom")
def start_doom(consumer, content):
	"""Initialize and start ViZDoom streaming"""
	room = "shared"  # Force all clients to use the same room

	if room not in running_games or not running_games[room]:
		# Initialize game
		game_instances[room] = init_doom()
		running_games[room] = True

		# Start game loop thread
		thread = threading.Thread(target=game_loop, args=(consumer, room), daemon=True)
		game_threads[room] = thread
		thread.start()


@liveview_handler("stop_doom")
def stop_doom(consumer, content):
	"""Stop ViZDoom streaming"""
	room = "shared"
	running_games[room] = False


@liveview_handler("move_forward")
def move_forward(consumer, content):
	"""Move forward in game"""
	room = "shared"
	game = game_instances.get(room)
	if game:
		game.make_action([1, 0, 0, 0], 4)


@liveview_handler("turn_left")
def turn_left(consumer, content):
	"""Turn left in game"""
	room = "shared"
	game = game_instances.get(room)
	if game:
		game.make_action([0, 1, 0, 0], 4)


@liveview_handler("turn_right")
def turn_right(consumer, content):
	"""Turn right in game"""
	room = "shared"
	game = game_instances.get(room)
	if game:
		game.make_action([0, 0, 1, 0], 4)


@liveview_handler("shoot")
def shoot(consumer, content):
	"""Shoot weapon"""
	room = "shared"
	game = game_instances.get(room)
	if game:
		game.make_action([0, 0, 0, 1], 4)
