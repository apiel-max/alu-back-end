# API

Python scripts that use a REST API to gather, organize, and export employee TODO data.

## Files

| File | Description |
|---|---|
| `0-gather_data_from_an_API.py` | Displays an employee's TODO list progress |
| `1-export_to_CSV.py` | Exports an employee's TODO data to CSV |
| `2-export_to_JSON.py` | Exports an employee's TODO data to JSON |
| `3-dictionary_of_list_of_dictionaries.py` | Exports all employees' TODO data to JSON |

## Usage

```bash
python3 0-gather_data_from_an_API.py <employee_id>
python3 1-export_to_CSV.py <employee_id>
python3 2-export_to_JSON.py <employee_id>
python3 3-dictionary_of_list_of_dictionaries.py
```

## API

Uses [JSONPlaceholder](https://jsonplaceholder.typicode.com) REST API.