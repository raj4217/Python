pnr, cnf, rac, wait, canc = 1, [], [], [], []


def book():
    global pnr
    if len(cnf) < 2:
        cnf.append(pnr)
        pnr += 1
        return f'CNF available:{2-len(cnf)} PNR: {pnr-1}'
    elif len(rac) < 2:
        rac.append(pnr)
        pnr += 1
        return f'RAC available:{2-len(rac)}  PNR:{pnr-1}'
    elif len(wait) < 2:
        wait.append(pnr)
        pnr += 1
        return f'WAIT available:{2-len(wait)}  PNR:{pnr-1}'
    else:
        return 'Regret!'


def cancel(pnr_no):
    tkts = [cnf, rac, wait]
    for i, j in enumerate(tkts):
        if pnr_no in j:
            canc.append(pnr_no)
            j.remove(pnr_no)
            if len(tkts[i + 1]) > 0:
                j.append(tkts[i + 1][0])
                del tkts[i + 1][0]
            if i == 0 and len(tkts[i + 2]) > 0:
                tkts[i + 1].append(tkts[i + 2][0])
                del tkts[i + 2][0]
            return f'PNR: {pnr_no} cancelled'


def status(pnr_no):
    if pnr_no in cnf:
        return f'CNF {len(cnf)}'
    if pnr_no in rac:
        return f'RAC {len(rac)}'
    if pnr_no in wait:
        return f'WAIT {len(wait)}'
    return 'Invalid!'


def lst(n):
    return n


def screen():
    print('Select one of the following option:')
    print('a. Booking \t b. Cancellation \t c. PNR Status \t d. List checking \t e. Exit')
    return input()


if __name__ == '__main__':
    print('Welcome to the reservation System! \n')
    val = 0
    d = {'a': book, 'b': cancel, 'c': status, 'CNF': cnf, 'RAC': rac, 'WAIT': wait, 'CANC': canc}
    while 1:
        inp = screen()
        if inp in ['Null', 'e']:
            exit(0)
        if inp in ['b', 'c']:
            val = input('Enter PNR: ')
            print(d[inp](int(val)))
        elif inp == 'd':
            val = input('Which list: CNF, RAC, WAIT, CANC \n')
            if val not in ['CNF', 'RAC', 'WAIT', 'CANC']:
                print('Invalid!')
            else:
                print(', '.join(str(x) for x in d[val]))
        else:
            print(d[inp]())