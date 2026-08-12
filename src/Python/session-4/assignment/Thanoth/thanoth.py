import os
import random


class Thanos:
    """
    Thanos class creates random files, deletes half of them randomly,
    and displays the results.

    Attributes:
        folder_path (str): Path to the folder where files will be created.
    """

    def __init__(self, folder_path: str):
        """
        Initializes the Thanos object.

        Parameters
        ----------
        folder_path : str
            Path to the folder where files will be created.
        """
        self.folder_path = folder_path

    def thanos(self) -> None:
        """
        Creates random files, deletes half of them randomly,
        and displays the results.

        Returns
        -------
        None
            Creates files, deletes half of them, and prints the results.
        """

        # Delete all existing files in the folder
        for file in os.listdir(self.folder_path):
            os.remove(os.path.join(self.folder_path, file))

        # Generate a random number of files from 1 to 10
        num_files = random.randint(1, 10)

        # Create the files
        for i in range(1, num_files + 1):
            file_name = os.path.join(
                self.folder_path,
                f"file_{i}.txt"
            )

            with open(file_name, "w") as file:
                file.write(f"This is file {i}")

        # Get the files after creation
        files = os.listdir(self.folder_path)

        print(f"Files before deleting: {len(files)}")

        # Calculate half of the files
        delete_count = len(files) // 2

        # Select random files to delete
        files_to_delete = random.sample(files, delete_count)

        # Delete selected files
        for file in files_to_delete:
            os.remove(os.path.join(self.folder_path, file))

        # Get remaining files
        remaining_files = os.listdir(self.folder_path)

        print(f"Deleted files: {delete_count}")
        print(f"Files after deleting: {len(remaining_files)}")


# Create an object
task = Thanos(
    "D:/DEPI/Task/DEPI-BNS5_AIS2_S1/src/Python/session-4/assignment/Thanoth/thanoth-folder"
)

# Call the main method
task.thanos()