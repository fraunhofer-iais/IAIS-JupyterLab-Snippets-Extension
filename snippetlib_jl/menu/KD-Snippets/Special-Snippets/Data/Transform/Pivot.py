### Pivot around 'State'

Pivoted_data = data.reset_index().pivot(index='date', columns='State')

level_1_attribute_names = Pivoted_data.columns.get_level_values(0).unique()
level_2_attribute_names = Pivoted_data.columns.get_level_values(1).unique()

print(Pivoted_data[level_1_attribute_names[0]][level_2_attribute_names[0]][:10])
Pivoted_data.head()