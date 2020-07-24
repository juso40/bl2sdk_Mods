import bl2sdk
from bl2sdk import *

from ConsoleGames import snake


class Console(BL2MOD):
    Name = "ConsoleGames"
    Description = "Simple Framework tha allows you to draw stuff to the console :P" \
                  "\nIncludes: Snake"
    Author = "Juso"

    def __init__(self):
        self.draw_buffer = 512  # frames before we need to clear the console
        self.draw_counter = 0
        self.timer = 0.042  # ~24 FPS
        self.clock = 0.0  # counts up every game tick, resets if greater than self.timer
        self.max_width = 250  # max amount of chars displayed horizontically
        self.max_height = 47  # max amount of chars displayed vertically
        self.frame = [
            [
                " " for _x in range(self.max_width)
             ] for _y in range(self.max_height)
        ]  # our canvas
        self.my_game = None  # the currently running game
        self.in_game = False
        self.games = ["Snake"]

    def set_game(self, game_obj):
        self.my_game = game_obj

    def Enable(self):
        def on_tick(caller: UObject, function: UFunction, params: FStruct) -> bool:
            if self.my_game:
                self.draw_counter += 1
                if self.draw_counter >= self.draw_buffer:
                    self.draw_counter = 0
                    caller.ViewportConsole.ClearOutput()
                getattr(self.my_game, "on_tick")(params.DeltaTime)
                # we will call the "on_tick" function of whatever game object we run, passing the DeltaTime
                self.clock = 0.0
            return True

        def input_char(caller: UObject, function: UFunction, params: FStruct) -> bool:
            if params.Text and self.my_game:
                getattr(self.my_game, "on_input")(params.Text)
                return False
            return True

        def command(caller: UObject, function: UFunction, params: FStruct) -> bool:
            return self.commands(params.Command)

        bl2sdk.RegisterHook("WillowGame.WillowGameViewportClient.Tick", "Tick", on_tick)
        bl2sdk.RegisterHook("Engine.Console.SetInputText", "InputChar", input_char)
        bl2sdk.RegisterHook("Engine.PlayerController.ConsoleCommand", "ConsoleCommand", command)

    def Disable(self):
        bl2sdk.RemoveHook("WillowGame.WillowGameViewportClient.Tick", "Tick")
        bl2sdk.RemoveHook("Engine.Console.SetInputText", "InputChar")
        bl2sdk.RemoveHook("Engine.PlayerController.ConsoleCommand", "ConsoleCommand")

    def clear_frame(self):
        self.frame = [
            [
                " " for _x in range(self.max_width)
             ] for _y in range(self.max_height)
        ]  # list of lists of chars, will later be change to flatted list of strings  self.frame[y][x]

    def draw_pixel(self, x, y, char):
        self.frame[y][x] = char

    def draw_line_ver(self, x, char):
        for xy in self.frame:
            xy[x] = char

    def draw_line_hor(self, y, char):
        self.frame[y] = [char for _ in self.frame[y]]

    def draw_frame(self):
        for line in self.frame:
            Log("".join(line))

    def commands(self, text):
        flags = None
        game = text.split("-")[0].strip()
        if len(text.split("-")) == 2:
            flags = text.split("-")[1]

        if flags:
            if "h" in flags:
                Log(snake.Snake.get_controlls())
                return False
        if game in self.games:
            snake.Snake(self)
            return False
        return True


console = Console()

bl2sdk.Mods.append(console)
