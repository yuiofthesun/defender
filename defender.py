def horizontal_move(position, direction):
    list1=enumerate(position)
    for i in list1:
        if i[1] is "@":
            place=i[0]

    def move(new_place, old_place):
        position[new_place] = "@"
        position[old_place] = "#"
        result= ''.join(position)
        return result

    if direction == "right":
        new_place=place+1
        old_place=new_place-1
        return move(new_place, old_place)

    elif direction == "left":
        new_place=place-1
        old_place=new_place+1
        return move(new_place, old_place)

    else:
        return  (''.join(position))

def main():
    line =list(39*"#"+"@"+40*"#")
    print(''.join(line))
    print(horizontal_move(line, "left"))
    print(horizontal_move(line, "right"))


if __name__ == '__main__':
    main()