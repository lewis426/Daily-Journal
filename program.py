import journal

# title
def print_header():
    print('------------------------------------')
    print('          DAILY JOURNAL')
    print('------------------------------------')
    print()


def run_event_loop():
    print('What would you like to do today?')
    while True:
        try:
            cmd = "EMPTY"
            journal_name = 'default'
            journal_data = journal.load(journal_name)
            while cmd != 'x' and cmd:
                cmd = input('(L)ist, (A)dd, E(x)it: ')
                if cmd.lower().strip() == 'l':
                    list_entries(journal_data)
                elif cmd.lower().strip() == 'a':
                    add_entries(journal_data)
                elif cmd.lower().strip() == 'x':
                    break
                elif cmd:
                    print('Sorry, we don\'t understand {0}.'.format(cmd))

            print('Goodbye!')
            journal.save(journal_name, journal_data)
        except ValueError:
            print('Please enter a valid value.')
            continue
        else:
            break



def list_entries(data):
    print('Fetching list....')
    print('Your Journal entries are: ')
    for idx, entry in enumerate(data):
        print('[{0}] {1}'.format(idx + 1, entry))


def add_entries(data):
    print('Adding to list....')
    entry = input('What do you want to write?: ')
    data.append(entry)


def main():
    print_header()
    run_event_loop()


# avoid running whole program when importing into outside programs
if __name__ == '__main__':
    main()
