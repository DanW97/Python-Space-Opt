def optimser(file: str, new_name: str) -> None:
    """
    Epic spatial complexity optimiser for most python scripts

    Parameters
    ----------
    file : str
        file to convert
    new_name : str
        new filename
    """
    with open(file, "r") as f:
        file = []
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i < len(lines) - 1:
                file.append(line)
            else:
                file.append(line + "\n")
            indent = len(line) - len(line.lstrip())
            line = line.lstrip()
            line = line.split("\n")[0]
            if not line.startswith("#") and not line.startswith("import"):
                if line.endswith(":") or line.startswith("def") or line.startswith("class"):
                    file.append(" "*(indent + 4) + "gc.collect()\n") 
                elif indent % 4 == 0:
                    file.append(" "*(indent) + "gc.collect()\n") 

    with open(new_name, "w") as f:
        f.writelines(file)
        # now make sure it is epically formatted
        from subprocess import Popen, PIPE
        cmd = ["black", f"{new_name}"]
        process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
