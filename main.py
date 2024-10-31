from src.masks import get_mask_card_number, get_mask_account
from src.utils import load_transaction

if __name__ == "__main__":
    get_mask_card_number("1234567890123456")
    get_mask_account("12345678901234561234")
    load_transaction("data/operations.json")