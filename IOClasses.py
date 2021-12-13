#------------------------------------------#
# Title: IOClasses.py
# Desc: A Module for IO Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# NWoodward, 2021-Dec-12, Added code to the save_inventory and load_inventory methods
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

import DataClasses as DC
import ProcessingClasses as PC

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(file_name: list, lst_Inventory: list) -> None:
        """Write data from list of files to 2 text files: one for CD data and one for CD Track data


        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
            lst_Inventory (list): list of CD objects.

        Returns:
            None.

        """
        file_name_CD = file_name[0]
        file_name_track = file_name[1]
        
        try:
            with open(file_name_CD, 'w') as file: # Open file for writing CD object data
                for cd in lst_Inventory:  # for CD objects in a list
                    file.write(cd.get_record())  # Write the CD information according to get_record method for CD Class
            with open(file_name_track, 'w') as file:
                for cd in lst_Inventory:
                    tracks = cd.cd_tracks  #cd_tracks = list of track objects
                    cdID = cd.cd_id
                    for track in tracks:
                        if track is not None:
                            realtrack = '{},{}'.format(cdID, track.get_record())
                            file.write(realtrack)
                        else:
                            pass
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def load_inventory(file_name: list) -> list:
        """Load CD and CD Track data from 2 files contained in the list file_name
        

        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.

        Returns:
            list: list of CD objects.
        """
        lst_Inventory = []  #clear the list of CD objects before loading data from file
        file_name_CD = file_name[0]
        file_name_track = file_name[1]

        try:
            with open(file_name_CD, 'r') as file:
                for line in file:  # for row of CD data in file
                    data = line.strip().split(',')
                    row = DC.CD(data[0], data[1], data[2])  # Create CD object
                    lst_Inventory.append(row)
            with open(file_name_track, 'r') as file:
                for line in file:   # for row of Track Data in file
                    data = line.strip().split(',')
                    cd = PC.DataProcessor.select_cd(lst_Inventory, data[0])
                    track = DC.Track(int(data[0]), data[1], data[2]) # Create Track object
                    cd.add_track(track) # cd = selected CD from list of CD objects + tracks to be added based on track text data
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')
        return lst_Inventory

class ScreenIO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Main Menu\n\n[l] load Inventory from file\n[a] Add CD / Album\n[d] Display Current Inventory')
        print('[c] Choose CD / Album\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, d, c, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def print_CD_menu():
        """Displays a sub menu of choices for CD / Album to the user

        Args:
            None.

        Returns:
            None.
        """

        print('CD Sub Menu\n\n[a] Add track\n[d] Display cd / Album details\n[r] Remove track\n[x] exit to Main Menu')

    @staticmethod
    def menu_CD_choice():
        """Gets user input for CD sub menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices a, d, r or x

        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            choice = input('Which operation would you like to perform? [a, d, r or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def show_tracks(cd):
        """Displays the Tracks on a CD / Album

        Args:
            cd (CD): CD object.

        Returns:
            None.

        """
        print('====== Current CD / Album: ======')
        print(cd)
        print('=================================')
        print(cd.get_tracks())
        print('=================================')

    @staticmethod
    def get_CD_info():
        """function to request CD information from User to add CD to inventory


        Returns:
            cdId (string): Holds the ID of the CD dataset.
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.

        """
        while True:
            try:
                cdId = input('Enter ID: ').strip()
                cdId = int(cdId)
                break
            except:
                print('CD ID must be an integer')
        cdTitle = input('What is the CD\'s title? ').strip()
        cdArtist = input('What is the Artist\'s name? ').strip()
        return cdId, cdTitle, cdArtist

    @staticmethod
    def get_track_info():
        """function to request Track information from User to add Track to CD / Album


        Returns:
            trkId (string): Holds the ID of the Track dataset.
            trkTitle (string): Holds the title of the Track.
            trkLength (string): Holds the length (time) of the Track.

        """
        while True:
            try:
                trkId = input('Enter Position on CD / Album: ').strip()
                trkId = int(trkId)
                break
            except:
                print('Track ID must be an integer')
        trkTitle = input('What is the Track\'s title? ').strip()
        trkLength = input('What is the Track\'s length? ').strip()
        return trkId, trkTitle, trkLength

