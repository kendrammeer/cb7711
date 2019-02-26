import random


def fill_global_matrix(seq1, seq2, scoring, gapcost):
    len1 = len(seq1)
    len2 = len(seq2)
    # Create empty matrix
    align_matrix = [[0 for x in range(len2+1)] for y in range(len1+1)]
    # Initialization
    align_matrix[0][0] = 0
    for i in range(1,len1+1):
        align_matrix[i][0] = -i*gapcost
    for j in range(1, len2+1):
        align_matrix[0][j] = - j * gapcost
    # Recursion
    for i in range(1,len1+1):
        for j in range(1, len2 + 1):
            try:
                if seq1[i-1] == seq2[j-1]:
                    match = align_matrix[i-1][j-1] + scoring[0]
                else:
                    match = align_matrix[i-1][j-1] + scoring[1]
                delete = align_matrix[i-1][j] - gapcost
                insert = align_matrix[i][j-1] - gapcost
                align_matrix[i][j] = max(match, delete, insert)
            except IndexError:
                delete = align_matrix[i - 1][j] - gapcost
                insert = align_matrix[i][j - 1] - gapcost
                align_matrix[i][j] = max(delete, insert)
    # Print matrix readably
    for row in align_matrix:
        print(row)
    return align_matrix


def fill_local_matrix():
    x = 2


def traceback_align(seq1,seq2,scoring,gapcost,fmatrix):
    pos1 = len(seq1) # position in seq1, i, initially equal to length of sequence
    pos2 = len(seq2)  # position in seq 2, j
    flen = 0  # length of final sequence
    align1 = ""
    align2 = ""
    while pos1 > 0 or pos2 > 0:
        flen += 1
        if pos1 > 0 and pos2 > 0 and ((fmatrix[pos1][pos2] == fmatrix[pos1-1][pos2-1] + scoring[0]) or (fmatrix[pos1][pos2] == fmatrix[pos1-1][pos2-1] + scoring[1])):
            align1 += seq1[pos1-1]
            align2 += seq2[pos2-1]
            pos1 -= 1
            pos2 -= 1
        elif pos1 > 0 and fmatrix[pos1][pos2] == fmatrix[pos1-1][pos2] - gapcost:
            align1 += seq1[pos1 - 1]
            align2 += "-"
            pos1 -= 1
        elif pos2 > 0 and fmatrix[pos1][pos2] == fmatrix[pos1][pos2-1] - gapcost:
            align1 += "-"
            align2 += seq2[pos2 - 1]
            pos2 -= 1
    # Reverse the alignment sequences
    print(align1)
    print(align2)
    final_align = [align1[::-1], align2[::-1]]
    # Print alignment
    for item in final_align:
        print(item)


def main():
    x = "acbcdb"
    y = "cadbd"
    M = len(x)
    N = len(y)
    seq1 = x
    seq2 = y
    scoring = [2, -1]  # +1 for match, -1 for mismatch
    gapcost = 1  # -1 for gap
    fmatrix = fill_global_matrix(seq1, seq2, scoring, gapcost)
    traceback_align(seq1, seq2, scoring, gapcost, fmatrix)


main()
