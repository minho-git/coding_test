def solution(directory, command):
    directories = directory[:]
    for cmd_line in command:
        parts = cmd_line.split()

        cmd = parts[0]

        if cmd == "mkdir":
            directories.append(parts[1])
        elif cmd == 'rm':
            target = parts[1]
            directories = [d for d in directories if not (d == target or d.startswith(target + "/"))]

        elif cmd == "cp":
            src = parts[1]
            dest = parts[2]

            basename = src.split("/")[-1]

            if dest == "/":
                new_prefix = "/" + basename
            else:
                new_prefix = dest + "/" + basename

            to_add = []
            for d in directories:
                if d == src or d.startswith(src + "/"):
                    new_path = new_prefix + d[len(src):]
                    to_add.append(new_path)

            directories.extend(to_add)

    return sorted(list(directories))