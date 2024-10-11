from src import masks
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card

if __name__ == "__main__":
    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', "date": None}]))