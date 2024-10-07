from typing import Dict, List

def filter_by_state(my_list: List[Dict[str, str | int]], state: str = "EXECUTED") -> List[Dict[str, str | int]]:
    return [dictionary for dictionary in my_list if dictionary.get("state") == state]

def sort_by_date(my_list: List[Dict[str, str | int]], reverse: bool = True) -> List[Dict[str, str | int]]:
    return sorted(my_list, key=lambda x: x["date"], reverse=reverse)
