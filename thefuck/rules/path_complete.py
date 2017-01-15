def match(command):
    stderr = command.stderr.lower().strip('.').split()
    return (("no" in stderr or "not" in stderr)
            and ("file" in stderr or "directory" in stderr))

def get_new_command(command):
    """
    Complete file paths
    1. Identify file / dir name due to which error is occuring
    2. Locate / Find
    3. Substitute and run
    """
    pass

# priority = 1  # Lower first, default is 1000

requires_output = True
