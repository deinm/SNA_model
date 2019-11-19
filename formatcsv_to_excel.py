import pandas as pd

path = '/Users/deinm/Desktop/codeworks/SNA_model/2019SS_ing.xlsx'
data = pd.read_excel(path, names=['model', 'company'])
# print(data)

count_dict = {'Cara Taylor': [0]*122, 'Laurijn Bijnen': [0]*122, 'Roos van Elk': [0]*122,
              'Louise Robert': [0]*122, 'Mayowa Nicholas': [0]*122, 'Naomi Chin Wing': [0]*122,
              'Giedre Dukauskaite': [0]*122, 'Sijia Kang': [0]*122, 'Anyelina Rosa': [0]*122,
              'Chunjie Liu': [0]*122, 'Felice Noordhoff': [0]*122, 'He Cong': [0]*122,
              'Hyunji Shin': [0]*122, 'Heejung Park': [0]*122, 'Sara Grace Wallerstedt': [0]*122,
              'Sarah Dahl': [0]*122, 'Fran Summers': [0]*122, 'Rebecca Leigh Longendyke': [0]*122,
              'Yoon Young Bae': [0]*122, 'Sora Choi': [0]*122}

company_list = ['3.1 Phillip Lim', 'A.P.C.', 'Acne Studios', 'Agnona', 'Akris', 'Alberta Ferretti', 'ALEXACHUNG', 'Alexander McQueen', 'Alexander Wang', 'Altuzarra', 'Anna Sui', 'Atlein', 'Balmain', 'Beautiful People', 'Blumarine', 'Boss', 'Brandon Maxwell', 'Brock', 'Brognano', 'Burberry', 'Byblos', 'Cedric Charlier', 'Calvin Klein', 'Carolina Herrera', 'Celine', 'Chanel', 'Chloe', 'Christian Dior', 'Christopher Kane', 'Coach', 'Courreges', 'Dion Lee', 'Dolce & Gabbana', 'Dries Van Noten', 'Elie Saab', 'Erdem', 'Ermanno Scervino', 'Escada', 'Esteban Cortazar', 'Etro', 'Eudon Choi', 'Fendi', 'Fila', 'Gabriela Hearst', 'Gareth Pugh', 'GCDS', 'Giada', 'Giambattista Valli', 'Givenchy', 'Haider Ackermann', 'Halpern', 'Hermes', 'Isabel Marant', 'J.W. Anderson', 'Jacquemus', 'Jeremy Scott', 'Jil Sander', 'JNBY', 'John Elliott', 'John Galliano', 'Kenzo', 'Koche', "L'Oreal", 'Loewe', 'Longchamp', 'Lou Dallas', 'Louis Vuitton', 'Maison Margiela', 'Marc Jacobs', 'Margaret Howell', 'Marni', 'Mary Katrantzou', 'Matthew Adams Dolan', 'Max Mara', 'Michael Kors', 'Missoni', 'Miu Miu', 'Molly Goddard', 'Monse', 'Moschino', 'MSGM', 'Mugler', 'No. 21', 'Off-White', 'Olivier Theyskens', 'Oscar de la Renta', 'Paco Rabanne', 'Paul & Joe', 'Peter Pilotto', 'Philipp Plein', 'Philosophy di Lorenzo Serafini', 'Poiret', 'Ports 1961', 'Prabal Gurung', 'Prada', 'Preen by Thornton Bregazzi', 'Proenza Scholer', 'R13', 'Ralph Lauren', 'Redemption', 'Rick Owens', 'Roberto Cavalli', 'Rochas', 'Rodarte', 'Roland Mouret', 'Sacai', 'Saint Laurent', 'Salvatore Ferragamo', 'Savage x Fenty', 'Self-Portrait', 'Simone Rocha', 'Sonia Rykiel', 'Sportmax', 'Stella McCartney', 'Supriya Lele', "Tod's", 'Tory Burch', 'Valentino', 'Versace', 'Victoria Beckham', 'Y-3', 'Zimmermann']

for row in data.iterrows():
    modelname = row[1]['model']
    companyname = row[1]['company']
    companyname = companyname.replace('\xa0', '')

    # if companyname not in company_list:
    #     company_list.append(companyname)

    print("@@",modelname,companyname)
    index = company_list.index(companyname)
    cnt_arr = count_dict[modelname]
    print(cnt_arr)
    cnt_arr[index] += 1
    print(cnt_arr)
    count_dict[modelname] = cnt_arr

print(count_dict)

with open('networkdata_2019SS.csv','w') as f:
    for single_company in company_list:
        f.write(', ')
        f.write(single_company)
    f.write("\n")
    for key,values in count_dict.items():
        f.write(key)
        for single_value in values:
            f.write(', ')
            f.write(str(single_value))
        f.write("\n")