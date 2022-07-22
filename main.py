from collections import Counter
from itertools import count

from extract_txt_from_pdf import extract_text_from_pdf, read_csv_team_skill

def main(resume_path, csv_path):
    string_array = extract_text_from_pdf(resume_path)
    skills_array = read_csv_team_skill(csv_path)
    # print(skills_array)
    # print(string_array)
    # print(skills_array)
    points = 10;
    counter = Counter()

    for team in skills_array:
        for skill in skills_array[team]:
                for string in string_array:
                    if string != None and string != '' and string.find(skill) != -1:
                        counter[team] += points

    teams_tuple = []
    for team in counter:
        teams_tuple.append((team, counter[team]))

    teams_tuple.sort(key=lambda x: x[1], reverse=True)

    print('Best Reccomendation', teams_tuple[0][0] + ' with ' + str(teams_tuple[0][1]) + ' points')
    print('Alternate 1:', teams_tuple[1][0] + ' with ' + str(teams_tuple[1][1]) + ' points')
    print('Alternate 2:', teams_tuple[2][0] + ' with ' + str(teams_tuple[2][1]) + ' points')
    print('Alternate 3:', teams_tuple[3][0] + ' with ' + str(teams_tuple[3][1]) + ' points')


# def foo(some_array):
#     new_counter = Counter()

#     for element in some_array:
#         new_counter[element] += 1 # or whatever number you want

#     # convert counter to dict

#     new_dict = dict(new_counter)