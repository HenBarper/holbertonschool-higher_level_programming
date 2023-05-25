#!/usr/bin/python3
def magic_string():
    setattr(magic_string, 'count', getattr(magic_string, 'count', 0) + 1)
    return 'BestSchool' + ', BestSchool' * (magic_string.count - 1)

#Previous implementation
# def magic_string():
#     if not hasattr(magic_string, 'count'):
#         magic_string.count = 1
#     else:
#         magic_string.count += 1
#     return 'BestSchool' + ', BestSchool' * (magic_string.count - 1)