import sys


def offer(data_frame):
    print('Type `save` to save data as csv.') 
    result = sys.stdin.readline().rstrip();
    if (result == 'save'):
        print ('Please type filename, data will be saved as {}.csv');
        filename = sys.stdin.readline().rstrip();
        file_name = filename + '.csv';
        data_frame.to_csv(file_name, index=False);
        print('done!');
        print('\n');
    else:
        print('Ok. Data not saved.');