import pandas as pd
import datetime
#df = pd.read_csv('data_source.csv')
#df.set_index('date')

db = 'data_source.csv'

DataFrame_header = ['date','amount','type']

def load_dataframe(db = 'data_source.csv'):
    '''
        load database into DataFrame and handle exceptions
    '''
    print('Looking for [' + db + ']...', end = '')
    try:
        open(db, 'r')
        print(' found.')
        df = pd.read_csv(db, index_col = 'index')
        return df
    except IOError as e:
        print(' not found.')
        print(e)
        query = ''
        while query != 'y':
            query = input('Do you want to create a new database? ').lower()
            if query == 'n':
                print('No')
                break
            elif query == 'y':
                print('yes')
                return create_db(db)
            else:
                print('Y/N')

def create_db(db = 'data_source.csv'):
    '''
        create new empty database
        Problem: cannot create empty DataFrame without index
    '''
    df = pd.DataFrame(data=None, index=None, columns = DataFrame_header)
    df.to_csv(db)
    return df

df = load_dataframe()

def save_db(data_frame = df):
    df.to_csv(db, index = False)
    print(df)

def add_entry(date = datetime.datetime.now(), amount = None, type = None):
    date = datetime.datetime.now()
    df.loc[len(df) + 1] = [date, amount, type]
    save_db(df)
