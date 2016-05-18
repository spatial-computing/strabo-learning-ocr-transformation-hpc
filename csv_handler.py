import csv
import classify_gbc
import io


if __name__ == '__main__':
    with io.open('python_input.csv', 'r', newline='', encoding="mbcs") as fp:
        reader = csv.reader(fp)
        count = 0

        for row in reader:
            print(count)
            count += 1
            row_size = len(row)
            iter = row_size / 8

            offset = 0
            for j in range(0, int(iter)):
                offset = j
                map_id = 0 if row[1 + 8 * offset] == '' else int(row[1 + 8 * offset])
                truth = row[2 + 8 * offset].lower()
                dict = row[3 + 8 * offset].lower()
                x = 0 if row[4 + 8 * offset] == '' else int(row[4 + 8 * offset])
                y = 0 if row[5 + 8 * offset] == '' else int(row[5 + 8 * offset])
                w = 0 if row[6 + 8 * offset] == '' else int(row[6 + 8 * offset])
                h = 0 if row[7 + 8 * offset] == '' else int(row[7 + 8 * offset])
                if len(truth) == 0 or len(dict) == 0:
                    continue
                classify_gbc.sequence2(truth, dict, x, y, w, h, map_id)


