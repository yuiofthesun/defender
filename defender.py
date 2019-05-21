def left(position):
    list1=enumerate(position)
    for i in list1:
        if i[1] is "@":
            place=i[0]

    new_place=place-1

    position[new_place] = "@"
    position[new_place+1] = "#"
    result= ''.join(position)
    return result



def main():
    line =list(39*"#"+"@"+40*"#")
    print(''.join(line))
    print(left(line))


if __name__ == '__main__':
    main()