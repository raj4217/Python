# Raising an exception
# x = 10
# if x > 5:
#     raise Exception('No. greater than 5')


# AssertionError Exception
import sys
# assert ('win32' in sys.platform), 'The code runs in windows only'

# try and except block


def linux_interaction():
    assert ('win32' in sys.platform), 'The code runs in windows only'

# try:
#     with open('file.log', 'r') as file:
#         file.read()
# except:
#     raise Exception('Could not open file.log')


# try:
#     linux_interaction()
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# except AssertionError as error:
#     print(error)
#     print('Linux linux_interaction() function was not executed')


# try:
#     linux_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)


try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')
