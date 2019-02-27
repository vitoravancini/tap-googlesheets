from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import google.oauth2.credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.

def get_sheet_lines(config, stream_schema):
    spreadsheets_api = initialize_google_sheets(config)
    first_row = config['first_row']
    sheet_name = config['sheet_name']
    sheet_id = config['sheet_id']
    number_of_schema_fields = len(stream_schema.to_dict()['properties'].items()) - 1

    first_column = config['first_column']
    last_column = get_last_column(first_column, number_of_schema_fields)
 
    sheet_range = "{sheet_name}!{first_column}{first_row}:{last_column}".format(first_column=first_column, 
                                                                                last_column=last_column, 
                                                                                sheet_name=sheet_name,
                                                                                first_row=first_row
                                                                                )
    
    result = spreadsheets_api.values().get(spreadsheetId=sheet_id,
                                range=sheet_range).execute()
    return result.get('values', [])[1:-1]

def get_last_column(first_column, number_of_fields):
    last_column = ""
    last_char_num = (ord(first_column) + number_of_fields)
    Z_code = 90
    A_code = 65
    if last_char_num > Z_code:
        last_column = "A"
        last_char_num =  A_code + (last_char_num - Z_code) - 1
    
    last_column = last_column + chr(last_char_num)
    return last_column

def initialize_google_sheets(config):
    """Initializes an Sheets API V4 service object.

    Returns:
      An authorized Sheets API V4 service object.
    """
    _GOOGLE_OAUTH2_ENDPOINT = 'https://accounts.google.com/o/oauth2/token'

    creds = google.oauth2.credentials.Credentials(
        config['developer_token'], refresh_token=config['refresh_token'],
        client_id=config['oauth_client_id'],
        client_secret=config['oauth_client_secret'],
        token_uri=_GOOGLE_OAUTH2_ENDPOINT)

    service = build('sheets', 'v4', credentials=creds)
    
    return service.spreadsheets()




