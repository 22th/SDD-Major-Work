from cx_Freeze import setup, Executable
 
setup(name = "Logic Puzzler" ,
      version = "1" ,
      description = "" ,
      #packages = ["numpy"],
      options={"build_exe": {"include_files":["gray.jpg","Levels","Scores.csv","Startbutton.png","eztext.py"]}},      
      executables = [Executable("LogicPuzzler.py")])