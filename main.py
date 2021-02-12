import csv


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        a = row[0]
        b = row[3]
        new_file = b.replace('Limited', ' ').replace('Finance',' ')
        # print(new_file)
        da = new_file
        print(da.split())
        # you = set(da)
        #
        # print(you)
        # we ={'Limited','Finance'}
        # ogogo = you - we
        # print(ogogo)



        # print(new_file)

if __name__ == "__main__":
    csv_path = 'mls.csv'
    with open(csv_path, 'r') as f_obj:
        csv_reader(f_obj)





