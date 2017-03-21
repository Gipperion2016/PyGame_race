import cx_Freeze

executables = [cx_Freeze.Executable("Py_Game.py")]

cx_Freeze.setup(
    name = "A bit Racey",
    options = {"build_exe":{"packages":["pygame"],
                            "include_files":["car-2.jpg", "Crash.wav", "NFS.wav"]}},
    executables = executables
    )
