dic = {'Lara Mullen': ['Burberry S/S 19 Show'], 'Steinberg ': ['Jil Sander F/W 18 Show'], 'Felice Nova Noordhoff': ['Prada F/W 17 Show'], 'Adut Akech': ['Saint Laurent S/S 18 Show', 'Saint Laurent F/W 17 Show', 'Saint Laurent S/S 17 Show'], 'Sora Choi': ['Alexander Wang F/W 18 Show', 'Louis Vuitton S/S 18 Show', 'Louis Vuitton F/W 17 Show', 'Louis Vuitton S/S 17 Show', 'Mulberry S/S 17 Show', 'Louis Vuitton S/S 15 Show']}

with open('prac.csv','w') as f:
    for key, values in dic.items():
        print(values)
        values = str(values)[1:-1]
        values = values.split(',')
        final = []
        for single_value in values:
            final.append(single_value.strip()[1:-1])

        f.write(str(key)+","+','.join(final)+'\n')