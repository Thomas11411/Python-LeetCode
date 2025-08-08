import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    borrowing_records["off"] = [rd == None for rd in borrowing_records.return_date]

    sumdata = borrowing_records.groupby(['book_id']).agg(
            current_borrowers=("off", 'sum'),
        ).reset_index()

    result = pd.merge(library_books, sumdata, on = 'book_id', how = "left")
    result = result.loc[result.total_copies == result.current_borrowers].drop('total_copies', axis=1)
    result = result.sort_values(by=["current_borrowers", 'title'], ascending=[False, True])

    return result