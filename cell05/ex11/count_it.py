import sys

params = sys.argv[1:] 
if not params:
    print("none")
else:
    print(f"parameters: {len(params)}")
    for p in params:
        print(f"{p}: {len(p)}")