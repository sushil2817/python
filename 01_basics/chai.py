from hello_world import function

function('ginger tea')


# now we got a new folder __pycache__
## python inner working

""" python chai.py
    
    [python coder]  => Byte Code => {python VM}
                           
            mostly hidden ⇫
      
       1. Compil to Byte code
               low level& plateform independent
       2. Byte code runs faster
        .pye -> compile python(frozen Binaries)
        __pycache__

       " Source Chang & Python Version "

         hello_world.cpython-312.pyc
         
         -> Works only for imported files
         -> not for top level files                 

"""

""" 
Python Virtual Machine (PVM)
 
  -> Code loopto iterate byte code
  -> Run time Engine
  -> Also Known as Python interpreter
  
  Byte Code is NOT machine Code

  -> Python specific interpretation
  -> cpython, jpytjon,Iron Python, Stackless, PyPy
       standard implementation
"""