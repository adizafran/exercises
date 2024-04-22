from typing import List


def move_cur(movement, input_str):
    if movement < 0:
        return 0
    elif movement > len(input_str):
        return len(input_str)
    else:
        return movement


def editor(actions: List[List]) -> List[str]:
    cur = 0
    statement = ""
    sub_stat = []
    for action in actions:
        func = action[0]
        arg = action[1]
        if func == "Insert":
            statement = statement[:cur] + arg + statement[cur:]
            cur += len(arg)
            print(f"func: {func}, arg: {arg}, statement: {statement}, cur: {cur}")
        elif func == "Left":
            cur = move_cur(cur - int(arg), statement)
            print(f"func: {func}, arg: {arg}, statement: {statement}, cur: {cur}")
        elif func == "Right":
            cur = move_cur(cur + int(arg), statement)
            print(f"func: {func}, arg: {arg}, statement: {statement}, cur: {cur}")
        elif func == "Delete":
            temp_cur = move_cur(cur + int(arg), statement)
            statement = statement[:cur] + statement[temp_cur:]
            #cur = temp_cur
            print(f"func: {func}, arg: {arg}, statement: {statement}, cur: {cur}")
        elif func == "Backspace":
            temp_cur = move_cur(cur - int(arg), statement)
            statement = statement[:temp_cur] + statement[cur:]
            cur = temp_cur
            print(f"func: {func}, arg: {arg}, statement: {statement}, cur: {cur}")
        elif func == "Print":
            temp_cur = move_cur(cur + int(arg), statement)
            temp_stat = statement[cur:temp_cur]
            sub_stat.append(temp_stat)
            print(f"func: {func}, arg: {arg}, statement: {statement}, cur: {cur}")
    return sub_stat


if __name__ == '__main__':
    input = [["Insert", "addthis"],
             ["Left", "4"],
             ["Right", "2"],
             ["Delete", "1"],
             ["Backspace", "2"],
             ["Print", "4"]]
    print(f"expected: '', actual: {editor(input)}")
