import sys
sys.path.append(r'C:\Users\Robodia\Desktop\Python\python-raspes\ObserverPatterns')
from observer import data

if __name__ == '__main__':
    for i in data.KPI_DATA:
        if i.name == 'open':
            print('Current open ticketss: %s' % i.value)
        elif i.name == 'new':
            print('New tickets in last hour: %s' % i.value)
        elif i.name == 'closed':
            print('Tickets closed in last hour: %s' % i.value)
