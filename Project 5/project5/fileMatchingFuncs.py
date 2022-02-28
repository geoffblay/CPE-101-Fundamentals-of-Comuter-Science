# Project 5
#
# Name: Geoff Blaylock
# Instructor: Turner
# Section: 09

class Entry:

    def __init__(self, account_num, name, balance, phone, city):
        self.account_num = account_num
        self.name = name
        self.balance = balance
        self.phone = phone
        self.city = city

    def __eq__(self, other):
        account_num_equal = self.account_num == other.account_num
        name_equal = self.name == other.name
        balance_equal = self.balance == other.balance
        phone_equal = self.phone == other.phone
        city_equal = self.city == other.city
        return account_num_equal and name_equal and balance_equal and phone_equal and city_equal


def read_file(file_name):
    # input is of type string
    # opens the specified file (oldMaster.dat) and creates a list of values of type Entry with the data
    # return value is of type list
    with open(file_name, 'r') as input_file:
        entry_list = []
        for i in input_file:
            # loops through each line of the input file splitting the data into a list of strings
            line = i.split()
            entry_list.append(Entry(line[0], line[1] + ' ' + line[2], float(line[3]), line[4], line[5]))

    return entry_list


def get_transactions(file_name):
    # input is of type string
    # opens the specified (transactions.dat) file and turns it into a list with each element being another list. The
    # element lists' 0th index corresponds to the transaction's account number while the 1st index corresponds to the
    # amount in $.
    # return value is of type list
    with open(file_name, 'r') as transactions:
        transactions_lists = transactions.readlines()
        transactions_lists_lists = []
        for i in range(0, len(transactions_lists)):
            # loops through each line of the file, splits it, adds it to a 2d list
            transactions_lists_lists.append(transactions_lists[i].split())

    return transactions_lists_lists


def sort_account_nums(file_name):
    # input is of type string
    # uses the read_file function to get the account numbers from each Entry and returns them in a sorted list of ints
    # return value is of type list
    list_entries = read_file(file_name)
    list_account_nums = []
    for i in range(0, len(list_entries)):
        # loops through a list of all entries and adds the account number to another list
        list_account_nums.append(int(list_entries[i].account_num))

    list_account_nums.sort()  # we were told we could use the .sort() method by Professor Turner during class on 5/24
    return list_account_nums


def write_sorted_om(account_nums, old):
    # input is of type list, string
    # uses the sorted list of account numbers to rewrite the oldMaster.dat file into a new file with the data sorted by
    # increasing account numbers
    # return value is null
    with open(old, 'r') as old_master:
        all_lines = old_master.readlines()
    list_entries = read_file(old)
    with open('sorted_oldMaster.dat', 'w') as sorted_om:
        for i in range(0, len(account_nums)):
            for j in range(0, len(account_nums)):
                # loops through the sorted list of account numbers matching each to the corresponding name and writes
                # it to the sorted file
                if account_nums[i] == int(list_entries[j].account_num):
                    sorted_om.write(all_lines[j])


def find_unmatched_transactions(sorted_om, transaction):
    # input is of type string
    # loops through the sorted master file and the transaction file and prints a message if there is a transaction with
    # no corresponding entry
    # return value is null
    with open(sorted_om, 'r') as sorted_om_input:
        sorted_om_lines = sorted_om_input.readlines()
    with open(transaction, 'r') as transaction_input:
        transaction_lines = transaction_input.readlines()

    for i in range(0, len(transaction_lines)):
        match = False
        for j in range(0, len(sorted_om_lines)):
            # loops through each file and switches the boolean to true if a match is found. If the boolean remains false
            # after one full iteration of the outside loop, the message is printed
            if sorted_om_lines[j].split()[0] == transaction_lines[i].split()[0]:
                match = True
        if not match:
            print('Unmatched transaction record for account ' + str(transaction_lines[i].split()[0]))


def update_balances(old, sorted_om, transaction):
    # input is of type string
    # updates the balances of all of the Entries based on the data from transactions.dat, then calls the
    # find_unmatched_transactions function
    # return value is null
    account_nums = sort_account_nums(old)
    write_sorted_om(account_nums, old)
    entries = read_file(sorted_om)
    transactions = get_transactions(transaction)

    for i in range(0, len(entries)):
        for j in range(0, len(transactions)):
            # loops through the lines of sorted_oldMaster.dat and applies the corresponding transaction to each Entry's
            # balance
            if transactions[j][0] == entries[i].account_num:
                int_balance = float(entries[i].balance)
                entries[i].balance = str(round(int_balance - float(transactions[j][1]), 2))
                # i understood the directions this way, was the transaction amount meant to be added to the balance?

    find_unmatched_transactions(sorted_om, transaction)
    return entries


def main():
    old = 'oldMaster.dat'
    sorted_om = 'sorted_oldMaster.dat'
    transaction = 'transaction.dat'
    # these string file names would need to be changed if the user wants to run the program for files of the same
    # format but with different names
    entries = update_balances(old, sorted_om, transaction)

    with open('newMaster.dat', 'w') as new_master:
        for i in range(0, len(entries)):
            name = entries[i].name.split()
            spaced_name = name[0] + ' \t' + name[1]
            # splits the name attribute of each entry and adds space in between them
            # writes the each Entry in order with their updated balances to a new file.
            new_master.write(
                str(entries[i].account_num) + '  ' + str(spaced_name) + '  \t' + str(
                    entries[i].balance) + '\t' + str(
                    entries[i].phone) + '\t\t' + str(entries[i].city) + '\n')


if __name__ == '__main__':
    main()
