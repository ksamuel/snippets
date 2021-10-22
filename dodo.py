 
from pathlib import Path

import doit
 
# from doit.tools import Interactive, LongRunning
 
BASE_DIR = Path(__file__).absolute().parent

DOIT_CONFIG = {
    "default_tasks": [""],
    "backend": "sqlite3",
    "action_string_formatting": "new",
}

def action(param_name, postitional_argument_list):
  pass


def task_name():
    """Doc"""

    return {
        # "task_dep": [], # strings of task names, without the task_
        # "file_dep": [], # can't be a generator
       
        
        "actions": [action, "ls {param_name}"], 
        'pos_arg': 'postitional_argument_list',
        "params": [{"name": "param_name", "default": "default value", "long": "long-option-name", "short": "-s", "type": str, "inverse": "no-param"}], # also: choices, help 
        # "getargs": { # get values from previous task returned as a dict passed to current task as an argument
        #    "argument_name": ("action_returning_dict", "key_returned"),
        # },
      
        # "targets": [],
        # "verbosity": 2,
    }


 
 

 

 

        "params": [{"name": "db", "default": "bittree", "long": "db"}],
        "getargs": {
            "password": ("generate_password", "password"),
        },
