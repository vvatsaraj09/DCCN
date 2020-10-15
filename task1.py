# Vaidehi Vatsaraj 2018130060
#  Jahnvi Shah 2018130053

def even_parity(l):
    return l.count(1) % 2 == 0

def flip_bit(i):
    return [1, 0][i]

Answers = [
    'No correction is necessary',
    'Uncorrectable error is detected',
    'Error Detected and Corrected'
]


def test_correct_errors():
    questions = [[[0, 1, 1, 0], [1, 1, 0, 1], [0, 1], [1, 0, 1, 1]],
                 [[1, 0, 0, 1], [0, 0, 1, 0], [1, 1], [1, 0, 1, 0]],
                 [[0, 1, 1, 1], [1, 1, 1, 0], [1, 1], [1, 0, 0, 0]]]
    for que in questions:
        print("The given Bits are : ", que[:2])
        message_sequence = rect_parity(que, len(que), len(que[1]))
        print(Answers[message_sequence[1]],
              end=" , Hence output of rect_parity is : ")
        print(message_sequence[0], end="\n\n")
    nrows = len(questions[0])-1
    ncols = len(questions[0][0]) + 1
    nrows -= 1
    ncols -= 1
    print(f'({nrows*ncols+nrows+ncols},{nrows*ncols}) rectangular parity code is tested successfully for 1 bit errors')

    
def rect_parity(codeword, nrows, ncols):
    parity_col = codeword[-1]
    parity_row = codeword[-2]
    data = codeword[:-2]
    row, col = -1, -1

    for i in range(len(data)):
        if (int(even_parity(data[i])) == parity_row[i]):
            if (row == -1):
                row = i
            else:
                return data, 1  # untracable error

    for i in range(len(data[1])):
        current_col = []
        for j in range(len(data)):
            current_col.append(data[j][i])
        if (int(even_parity(current_col)) == parity_col[i]):
            if (col == -1):
                col = i
            else:
                return data, 1 
    if (row == -1 and col == -1):
        return data, 0  # no error
    elif (row == -1 or col == -1):

        return data, 1  # untracable error
    else:
        data[row][col] = flip_bit(data[row][col])
        return data, 2  # error

test_correct_errors()