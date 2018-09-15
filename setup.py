import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="RoboTirade",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["resources2/soldier1_gun.png","resources2/tile_01.png","resources2/towerDefense_tile205.png","resources2/tile_533.png","resources2/robot1_hold.png","resources2/healthbar.png","resources2/health.png","resources2/gameover.png","resources2/youwin.png","resources2/explode.wav","resources2/enemy.wav","resources2/shoot.wav","resources2/moonlight.wav"]}},
    description = "2D, Top Down Arcade Game",
    executables = executables,
    version = "0.1"
    )
