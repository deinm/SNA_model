import pandas as pd
import operator

# header = None
# df = pd.read_excel('/Users/deinm/Desktop/SNA/2019SS.xlsx',
df = pd.read_excel('/Users/deinm/Desktop/SNA/2019FW.xlsx',sheet_name='Sheet1')

value_dict = {}

for single_row in df.values:
    for single_value in single_row:
        if type(single_value) is not float:
            single_value = single_value.replace('(C)', '')
            single_value = single_value.replace('(O)', '')

            if single_value in value_dict:
                value_dict[single_value] = value_dict[single_value] + 1
            else:
                value_dict[single_value] = 1

sorted_value_dict = sorted(value_dict.items(), key=operator.itemgetter(1))
sorted_value_dict = dict(sorted_value_dict[-20:])
print(sorted_value_dict)

for i in range(318):
    single_column = df.iloc[:,i]
    print(single_column.name,":")
    for model in single_column:
        if model in sorted_value_dict:
            if type(sorted_value_dict[model])==int:
                sorted_value_dict[model] = [single_column.name]
            else:
                sorted_value_dict[model].append(single_column.name)

            print(model)

# with open('format_2019SS.csv','w') as f:
with open('format_2019FW.csv', 'w') as f:
    for key, values in sorted_value_dict.items():
        for single_show in values:
            f.write(key+", ")
            show = single_show.split('S/S')[0].strip()
            f.write(show)
            f.write("\n")
