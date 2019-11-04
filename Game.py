class Game:
    def __init__(self):
        self.gameArr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def playMove(self, move, pos):
        if not (self.gameArr[pos[0]][pos[1]] == 1 or self.gameArr[pos[0]][pos[1]] == -1):
            self.gameArr[pos[0]][pos[1]] = move
            return True
        return False

    def reset(self):
        self.gameArr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def isWin(self, arr, num):
        if self.hasDiagonal(arr, num) or self.hasHorizontal(arr, num) or self.hasVertical(arr, num):
            return True
        return False

    def hasHorizontal(self, arr, num):
        for i in range(3):
            if arr[i][0] == num and arr[i][1] == num and arr[i][2] == num:
                print(arr[i][0], " ", arr[i][1], " ", arr[i][2])
                print("horiz: ", arr)
                return True
        return False

    def hasVertical(self, arr, num):
        for i in range(3):
            if arr[0][i] == num and arr[1][i] == num and arr[2][i] == num:
                print(arr[0][i], " ", arr[1][i], " ", arr[2][i])
                print("ver: ", arr)
                return True
        return False

    def hasDiagonal(self, arr, num):
        if arr[0][0] == num and arr[1][1] == num and arr[2][2] == num:
            print(arr[0][0], " ", arr[1][1], " ", arr[2][2])
            print("dig: ", arr)
            return True
        elif arr[2][0] == arr[1][1] == arr[0][2] == num:
            print(arr[2][0], " ", arr[1][1], " ", arr[0][2])
            print("dig: ", arr)
            return True
        return False