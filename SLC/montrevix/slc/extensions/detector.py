def detector(settings,mode="OneForOne"):
    global lines
    lines  = []
    if mode == "OneForOne":
        file = settings.get('file')
        prefix = settings.get('prefix')
        with open(file, 'r') as mfile:
            for line in mfile:
                if prefix in line:
                    print("True")
                else:
                    print("false")
    elif mode == "AllForAll":
        file = settings.get('file')
        prefix = settings.get('prefix')
        with open(file, 'r') as mfile:
            for line in mfile:
                if line in prefix:
                    print(f"{prefix.index(line)}|True")
                else:
                    print(f"{prefix.index(line)}|False")
