# print('Input the sentence:')

# sentence = 'Roman ya vam ne dam'
# def is_palindrome(sentence):

#     sent = sentence.split(' ')
#     sent1 = sent[::-1]
#     result = ' '.join(sent1)

#     if sentence == result:
#         print('True')
#     else:
#         print('False')
#     return sentence

# print(is_palindrome(sentence))


print('Could you, please, print a palindrome:')
sentence = str(input())
def is_palindrome():

    # sent = sentence.split(' ')
    # sent1 = sent[::-1]
    # result = ' '.join(sent1)

    result = ' '.join(sentence.split(' ')[::-1])

    if sentence == result:
        print('True. This is a palindrome:')
    else:
        print('False. This is not a palindrome:')
    return sentence

print(is_palindrome())
