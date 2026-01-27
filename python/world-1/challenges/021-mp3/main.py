import vlc
from pathlib import Path

BASE_DIR = Path(__file__).parent
mp3_file = str(BASE_DIR / "yl.mp3")

player = vlc.MediaPlayer(mp3_file)
player.play()

input("Press Enter to stop...")
player.stop()