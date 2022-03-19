import cx_Freeze

executable = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(name="Snakes",

                options = {
                    "build_exe": {
                        "packages": ["pygame"],
                        "include_files":["apple-removebg-preview (1).png","snake-removebg-preview.png"],
                                }
                         },
                description="Snake Arcade Game",
                executables=executable
                )

