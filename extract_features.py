PATH = os.listdir('data/')


def extract_features(PATH):
    emotions_list=[]
    gender_list = []
    files_list = []

    for item in PATH:
        if item[6:8]=='01':
            emotions_list.append('neutral')
        elif item[6:8]=='02':
            emotions_list.append('calm')
        elif item[6:8]=='03':
            emotions_list.append('happy')
        elif item[6:8]=='04':
            emotions_list.append('sad')
        elif item[6:8]=='05':
            emotions_list.append('angry')
        elif item[6:8]=='06':
            emotions_list.append('fearful')
        elif item[6:8]=='07':
            emotions_list.append('disgusted')
        elif item[6:8]=='08':
            emotions_list.append('surprised')

        if int(item[-6:-4]) % 2 == 0:
            gender_list.append('female')
        elif int(item[-6:-4]) % 2 != 0:
            gender_list.append('male')

        files_list.append(item)

    df = pd.DataFrame(columns=["emotion", "gender"])
    df["emotion"] = emotions_list
    df["gender"] = gender_list
    df["file"] = files_list

    return df