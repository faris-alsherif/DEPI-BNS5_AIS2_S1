import os
import random


def thanos(folder_path: str) -> None:
    """
    Create random files, delete half of them randomly,
    and display the results.

    Parameters
    ----------
    folder_path : str
        Path to the folder where files will be created.

    Returns
    -------
    None
        Creates files, deletes half of them, and prints the results.
    """

    for file in os.listdir(folder_path):
        os.remove(os.path.join(folder_path, file))

    num_files = random.randint(1, 10)

    for i in range(1, num_files + 1):
        file_name = os.path.join(folder_path, f"file_{i}.txt")
        with open(file_name, "w") as file:
            file.write(f"This is file {i}")

    files = os.listdir(folder_path)
    print(f"Files before deleting: {len(files)}")

    delete_count = len(files) // 2

    files_to_delete = random.sample(files, delete_count)

    for file in files_to_delete:
        os.remove(os.path.join(folder_path, file))

    remaining_files = os.listdir(folder_path)

    print(f"Deleted files: {delete_count}")
    print(f"Files after deleting: {len(remaining_files)}")


thanos("D:/DEPI/Task/DEPI-BNS5_AIS2_S1/src/Python/session-3/assignment/Thanoth/thanoth-folder")