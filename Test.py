for tc in range(int(input())):
    word = list(input())
    word.sort()
    stack = []

    for w in word:
        print("w : ", w)
        print("stack : ", stack)
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)

    if stack:
        print(f'#{tc + 1} {"".join(stack)}')
    else:
        print(f'#{tc + 1} Good')