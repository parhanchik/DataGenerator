import csv
import json
import random
import string
import re


"""
Constants, which use in this program
"""
input_filename = 'generate_props'
output_add_filename = '_Table.csv'
types_arr = ('str', 'int', 'timestamp')


"""
Class parse json and print in .csv file all tables, that meet the conditionы
"""
class dateGenerator():

    """
    Get random row with the required cell type and format
    """
    def randomRow(self, types, formats):
        row = []
        for i in range(len(types)):
            if types[i] == 'str':
                row.append(self.randomString(formats[i]))
            elif types[i] == 'int':
                row.append(self.randomInt(formats[i]))
            elif types[i] == 'timestamp':
                row.append(self.randomTimestamp(formats[i]))

        return row



    """
    Get random int with the required number of digits
        string:     format - string satisfying the following regular expression [0-9]*\.[0-9]*
                            where we use only first numb, because INT has no fractional part.
    """
    def randomInt(self, format):
        precision = int(format.split('.')[0])
        return random.randint(10**(precision-1), (10**precision)-1)



    """
    Get random string with the required number of char
        string:     format - string, containing required number of chars, for ex. format == '10'
    """
    def randomString(self, format):
        str_len = int(format)
        return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation + ' ')
                        for i in range (str_len)])



    """
        Get random timestamp
            %Y:     year,
            %m:     month,
            %d:     day,
            %H:     hour,
            %S:     second,
            %%ss:   millisecond
            
    """
    def randomTimestamp(self, format):
        timestamp = format
        timestamp = re.sub('%Y', str(random.randint(1900, 2100)), timestamp)
        timestamp = re.sub('%m', str(random.randint(1, 12)), timestamp)
        timestamp = re.sub('%d', str(random.randint(1, 31)), timestamp)
        timestamp = re.sub('%H', str(random.randint(0, 23)), timestamp)
        timestamp = re.sub('%M', str(random.randint(0, 59)), timestamp)
        timestamp = re.sub('%S', str(random.randint(0, 59)), timestamp)
        timestamp = re.sub('%%ss', str(random.randint(0, 999)), timestamp)
        return timestamp



    def openCSV(self, name):
        output = open(name, 'w', encoding='UTF8', newline='')
        writer = csv.writer(output)
        return writer, output



    def _raiseError(self, e):
        print(e)
        raise SystemExit('Program terminate wit error before')



    def _checkInputData(self, var, format):
        e = f'ERR: Incorrect input data - {var}, expected format - {format}'

        if format == 'int':
            if not re.match(r'[0-9]+', var):
                self._raiseError(e)
        elif format == 'int_input_format':
            if not re.match(r'[0-9]+\.[0-9]+', var):
                self._raiseError(e)
        elif format == 'timestamp':
            if not re.match(r'[\.\: %\d]+', var):
                self._raiseError(e)


    """
    Parse JSON input file:
        (type: var - description)
        
        list:   tables - list of table in input json
        int:    row_numbs - value for field 'row'. If this field not exist, handling
                            raised exception and start processing(parsing) next table.
        
    """
    def runGenData(self, input_filename):
        with open(f'{input_filename}.json') as input_json_file:
            global output_filename

            input_json = json.load(input_json_file)
            input_dict = input_json[0]

            output_filename = input_dict['name_system'] + output_add_filename
            csv, out = self.openCSV(output_filename)
            self._checkInputData(str(input_dict['system_row']), 'int')
            self._checkInputData(input_dict['system_value_timestamp'], 'timestamp')
            self._checkInputData(input_dict['system_value_int'], 'int_input_format')
            self._checkInputData(input_dict['system_value_str'], 'int')
            defaults = {
                'system_row': input_dict['system_row'],
                'system_val_timestamp': input_dict['system_value_timestamp'],
                'system_val_int': input_dict['system_value_int'],
                'system_val_str': input_dict['system_value_str'],
            }

            tables = input_dict['tables']
            for table in tables:
                header = []
                types = []
                formats = []
                if (table['generate_data']):
                    try:
                        row_numbs = table['row']
                        self._checkInputData(str(row_numbs), int)
                    except KeyError:
                        row_numbs = defaults['system_row']
                    columns = table['column']
                    for column in columns:
                        for column_name in column:
                            try:
                                col_type = column[column_name][0]
                            except:
                                continue

                            if col_type in types_arr:
                                types.append(col_type)
                            else:
                                continue
                            header.append(column_name)

                            try:
                                col_format = column[column_name][1]
                                if col_format:
                                    self._checkInputData(col_format, col_type)
                                else:
                                    self._raiseError(f"ERR: NULL format for {col_type} in {column_name}")
                            except:
                                key = f'system_val_{col_type}'
                                col_format = defaults[key]
                            formats.append(col_format)

                    csv.writerow(header)
                    [csv.writerow(self.randomRow(types, formats)) for i in range(row_numbs)]
                    if table != tables[-1]:
                        csv.writerow('\n')
            out.close()



if __name__ == '__main__':
    gendate_instanse = dateGenerator()
    gendate_instanse.runGenData(input_filename)

