import json
import os
from item.Util import Settings
from item.Item import Item
from item.items.LootTable import make_loot_table


def process_item(item, settings):
    make_loot_table(item, settings)


def open_item_files(directory, settings, lang):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as json_file:
                        data = json.load(json_file)
                        item = Item(file_path, data, settings)
                        process_item(item, settings)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON file {file_path}: {e}")
                except Exception as e:
                    print(f"Error opening file {file_path}: {e}")


def main():
    settings_file = open('settings.json', 'r', encoding='utf-8')
    settings = Settings(json.load(settings_file))
    lang_path = settings.get_lang_path()
    lang_file = json.loads(open(os.path.join(lang_path, settings.lang)).read())
    open_item_files('items', settings, lang_file)
    new_lang = open(os.path.join(lang_path, 'en_us.json'), 'w')
    new_lang.write(json.dumps(lang_file, indent=2))


if __name__ == '__main__':
    main()
