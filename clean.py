import pandas as pd

def clean(input_file1, input_file2):

    df1= pd.read_csv(input_file1)
    df2= pd.read_csv(input_file2)

    #merge
    merge_file = pd.merge(df1,df2,
                       left_on='respondent_id',right_on='id',
                       how='outer').drop('id',axis=1)
    #drop
    df4=merge_file.dropna(axis=0)
    df=df4[df4['job'].str.contains('insurance|Insurance')==False]
    return df


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('respondent_contact', help='Data file(CSV)')
    parser.add_argument('respondent_other', help='Data file(CSV)')
    parser.add_argument('output', help='Cleaned data file(CSV)')
    args = parser.parse_args()

    cleaned = clean(args.respondent_contact,args.respondent_other)
    cleaned.to_csv(args.output, index=False)

