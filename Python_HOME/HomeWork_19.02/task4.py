import os
import json

async def save_json(json_data, directory):

    os.makedirs(directory, exist_ok=True)

    for i, obj in enumerate(json_data, 1):
        filename = os.path.join(directory, f"data_{i}.json")

        with open(filename, "w") as file:
            json.dump(obj, file, indent=4)

            print(f"File {filename} saved.")

if __name__ == "__main__":

    directory = "json_files"
    loop = asyncio.get_event_loop()
    loop.run_until_complete(save_json(json_data, directory))
