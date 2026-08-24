"""
Namespace Isolation & Modular Architecture (Imports & Scope)

**Concepts Covered:** Creating Modules, The 5 Structural Import Archetypes (`import module`, `from module import function`, `from module import function as fn`, `import module as m`, and `from module import *`).

- **Task:** Convert your operational code into an external library file and orchestrate it cleanly.
    
    1. Create a brand-new, standalone Python file named `network_utils.py` in the exact same workspace folder. Move your completed `log_incident()` function definition into this file. Save and close it.
        
    2. Create a clean script file named `main_controller.py`.
        
    3. You must write five separate blocks of execution code in `main_controller.py` to systematically test every import variation defined in the chapter:
        
        - Import the module as a whole: `import network_utils`, then execute the function using the dot notation (`network_utils.log_incident(...)`).
            
        - Import the specific function directly: `from network_utils import log_incident`.
            
        - Import the function with an alias: `from network_utils import log_incident as li`.
            
        - Import the module with an alias: `import network_utils as nu`.
            
        - Import all contents simultaneously: `from network_utils import *`.
            
    4. Below the final statement, add a small block comment explaining why using `from module import *` can be dangerous in larger, enterprise-level systems engineering programs (e.g., namespace pollution and unexpected variable/function collisions).
        
"""