from rect_save import main as rect_save_main
from font import DialogBox
import settings

class LevelTransition:
    def __init__(self, player):
        self.player = player
        self.other_game_active = True
        self.dialog_box = DialogBox(10, HEIGHT - 200, WIDTH - 20, HEIGHT * (2/9), "../Graphics/test/DialogueBoxSimple.png", "", font)
        self.dialogs = [
            "Greetings, young traveler!",
            "Welcome to the icy regions of Eldoria.",
            "I am the Elder Frog, guardian of this land.",
            "I sense a brave spirit within you, eager to explore and learn.",
            "Are you ready to embark on a journey of discovery?",
            "While the icy terrain holds its own mysteries, there is much more to explore beyond these frosty lands.",
            "Seek out the warmth of the desert sands, where another wise Elder Frog awaits.",
            "Their knowledge may hold the key to unlocking new adventures and challenges.",
            "Venture forth, young adventurer, and may the winds of destiny guide your path!"
        ]
        self.current_dialog_index = 0
        self.showing_dialog = True
        self.dialogs_completed = False

    def check_position_for_different_level(self):
        if (
            1970 <= self.player.rect.centerx <= 2130
            and 960 <= self.player.rect.centery <= 970
        ):
            if self.other_game_active:
                self.start_dialogs()
                self.start_other_game()
                self.player.rect.center = (2100, 1500)

    def start_dialogs(self):
        self.showing_dialog = True

    def start_other_game(self):
        rect_save_main()
        print("Other game started")
        self.other_game_active = False
