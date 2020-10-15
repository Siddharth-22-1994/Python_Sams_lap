# Context managers
# using with statement

# with open('notes.txt', 'w') as files:
#     files.write('Some todooooo....')


# The above code is looks like
file = open('notes.txt', 'w')
try:
    file.write('Some todooo...')
finally:
    file.close()


# Refer URL:https://www.youtube.com/watch?v=LB_95Pfkiws
