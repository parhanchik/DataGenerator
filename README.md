# DataGenerator


## Данные

Входные данные: _generate_props.json_ (необходимо положить в одну директорию с main.py)

Выходные данные: _{name_system}\_Table.csv_


## Логика

Скрипт на вход получает конфигурационный файл generate_props.json. На основе данных из этого конфигурационного файла создает .csv файл, содержащий таблички, удовлетворяющие условиям.

В json конфиге - Имя системы, значения полей по-умолчанию(формат/кол-во символов/кол-во строк), имя таблицы, условие генерации, кол-во строк, название колонок и их тип. Если произведена ошибка в типе колонки или не указан вовсе тип – колонку пропускаем.



## Пример

Конфигурационный файл:

```
[
  {
    "name_system": "Generate_1",
    "system_value_str": "12",
    "system_value_int": "38.12",
    "system_value_timestamp": "%Y-%m-%d %H:%M:%S",
    "system_row": 12,
    "tables": [
      {
        "name": "Table_1",
        "generate_data": true,
        "row": 10,
        "column": [
          {
            "Col_1": ["str", "12"]
          },
          {
            "Col_2": ["int", "9.0"]
          },
          {
            "Col_3": ["timestamp", "%Y-%m-%d"]
          }
        ]
      },
      {
        "name": "Table_2",
        "generate_data": true,
        "column": [
          {
            "Col_1": ["str"]
          },
          {
            "Col_2": ["int"]
          },
          {
            "Col_3": ["timestamp", "%Y-%m-%d %H:%M:%S:%%ss"]
          }
        ]
      },
      {
        "name": "Table_3",
        "generate_data": false,
        "row": 10,
        "column": [
          {
            "Col_1": ["str"]
          },
          {
            "Col_2": [""]
          },
          {
            "Col_3": ["timestamp"]
          }
        ]
      },
      {
        "name": "Table_4",
        "generate_data": true,
        "row": 10,
        "column": [
          {
            "Col_1": ["str"]
          },
          {
            "Col_2": [""]
          }
        ]
      },
      {
        "name": "Table_5",
        "generate_data": true,
        "row": 10,
        "column": [
          {
            "Col_1": ["str"]
          },
          {
            "Col_2": [""]
          },
          {
            "Col_3": ["timestamp"]
          },
          {
            "Col_4": ["timestamp"]
          },
          {
            "Col_5": ["timestamp"]
          },
          {
            "Col_6": ["string"]
          },
          {
            "Col_7": ["str", "0"]
          }
        ]
      }
    ]
  }
]
```


Полученный csv файл:

<img width="585" alt="image" src="https://user-images.githubusercontent.com/65617360/162841273-5558a3af-5211-406f-8eee-587152afbb84.png">

