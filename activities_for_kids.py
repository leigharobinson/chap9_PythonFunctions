# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take varying number of children's names as the argument.

# For example, the run function would be defined as follows:
def run(*kids):
    # Loop through all the kids and print that the child performed the activity.
    for kid in kids:
        print(f'{kid} ran like a fool!')


run("Joe", "Jenna")
# Output:
# "Joe ran like a fool!"
# "Jenna ran like a fool!"


def activity(activity, *kids):
    for kid in kids:
        print(f'{kid} {activity} like a champion!')


activity('ran', 'Matt', 'Luke', 'Sarah', 'Hannah')
activity('swung', 'Matt', 'Luke', 'Sarah', 'Hannah')
activity('slid', 'Matt', 'Luke', 'Sarah', 'Hannah')
activity('lept', 'Matt', 'Luke', 'Sarah', 'Hannah')
