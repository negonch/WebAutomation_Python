#    *
#   ***
#  *****
#    |
#
#     *
#    ***
#   *****
#  *******
# *********
#     |

#
# def make_xmas_tree(height, char):  # for a tree with height = 3
#     spaces = height - 1
#     for layer in range(height):
#         print(' ' * (spaces-layer), char * (1 + 2*layer))
#
#     # print(' '*(2-0), '*'*1)
#     #
#     # print(' '*(2-1), '*'*3)
#     #
#     # print(' '*(2-2), '*'*5)
#
#     print(' ' * spaces, '|')
#
# make_xmas_tree(7, '1')

#    1
#   123
#  12345
# 1234567
#    |
def make_num_xmas_tree(height):
    spaces = height - 1
    for layer in range(height):
        branches = ''
        # char * (1 + 2*layer)
        # '12345'
        for n in range(1 + 2*layer):
            branches += str(n+1)

        print(' ' * (spaces-layer), branches)

    # print(' '*(2-0), '*'*1)
    #
    # print(' '*(2-1), '*'*3)
    #
    # print(' '*(2-2), '*'*5)

    print(' ' * spaces, '|')

make_num_xmas_tree(5)


# For homework:
#    1
#   121
#  12321
# 1234321
#    |


#    @
#   @ @
#  @   @
# @     @
#    |


# end_result = '1234321'
# end_result2 = [1,2,3,4,3,2,1]


def make_palindrome_xmas_tree(height):
    spaces = height - 1
    for layer in range(height):
        branches = ''
        # char * (1 + 2*layer)
        # '12345'
        for i in range(layer + 1):
            # end_result = end_result + str(i)
            branches += str(i + 1)

        # branches += branches[layer-1::-1]
        branches += (branches[0:layer])[::-1]

        print(' ' * (spaces-layer), branches)

    print(' ' * spaces, '|')


make_palindrome_xmas_tree(6)
