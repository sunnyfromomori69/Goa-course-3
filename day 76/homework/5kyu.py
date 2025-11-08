def dir_reduc(arr):
    opposite = {"NORTH":"SOUTH", "SOUTH":"NORTH", "EAST":"WEST", "WEST":"EAST"}
    stack = []
    for d in arr:
        if stack and stack[-1] == opposite[d]:
            stack.pop()
        else:
            stack.append(d)
    return stack