import pandas as pd




def get_data(input_file):
    print('Importing Data from %s...' % (input_file))
    df = pd.read_csv(input_file)
    df.name = str(input_file)
    return df


def join_data(df_1, df_2):
    #print('Joining Data from %s and %s' % (df_1.name, df_2.name))
    return df_1.join(df_2.set_index('respondent_id'), on ='respondent_id')


def clean_data(df):
    # print('Cleaning Data of %s...' % (df.name))
    df['birthdate'] = pd.to_datetime(df['birthdate'], format='%Y-%m-%d')
    df[['respondent_id', 'name', 'address', 'phone', 'job', 'company', 'birthdate']]
    return df


def export_data(df, output_file):
    #print('Exporting Data to %s...' % (output_file))
    df.to_csv(output_file)
    return 0


if __name__ == '__main__':
    print('Starting script...')
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='Contact Info File')
    parser.add_argument('other_info_file', help='Other Info File')
    parser.add_argument('output_file', help='Output File')
    args = parser.parse_args()

    df_1 = get_data(args.contact_info_file)
    df_2 = get_data(args.other_info_file)

    df = join_data(df_1, df_2)
    df.name = args.output_file
    
    df_clean = clean_data(df)

    export_data(df_clean, args.output_file)

    print('Completed.')




