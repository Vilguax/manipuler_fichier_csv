import csv

def clean_and_filter_csv(input_file, output_file):
    with open(input_file, 'r') as csv_file, open(output_file, 'w', newline='') as result_file:
        reader = csv.DictReader(csv_file) 
        filtered_headers = ['id', 'Period', 'Data_value', 'Series_title_2'] 
        writer = csv.DictWriter(result_file, fieldnames=filtered_headers) 
        writer.writeheader() 
        id_count = 0

        for row in reader:
            if any(value.strip() == '' for value in row.values()):
                continue

            if not any(filter_word in row['Series_title_2'] for filter_word in ['Credit', 'Debit', 'Services']):
                continue

            filtered_row = {key: value for key, value in row.items() if key in filtered_headers[1:]}

            id_count += 1
            filtered_row['id'] = id_count

            writer.writerow(filtered_row)

clean_and_filter_csv('manipuler_fichier_csv/data.csv', 'manipuler_fichier_csv/result.csv')