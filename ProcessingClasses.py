#------------------------------------------#
# Title: ProcessingClasses.py
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# NWoodward, 2021-Dec-11, Modified to add code to select_cd and add_track methods
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        try:
            cd_idx = int(cd_idx)
        except:
            raise Exception('CD index must be an integer')
        for row in table: # for a cd object in the list
            if row.cd_id == cd_idx: # if the cd object cd_id property equals the cd_idx integer
                return row  # return the cd object that matches the cd_idx integer
        raise Exception('This CD ID does not exist in the list of CDs')

    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:  # cd is a CD object in the DataClasses module
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the track gets added to.

        Raises:
            Exception: Raised in case position is not an integer.

        Returns:
            None.
        """
        pos, ttl, lgth = track_info # Unpack the tuple
        if type(pos) == int:
            track = DC.Track(pos, ttl, lgth) # Create a CD object with variable data from tuple arg
            cd.add_track(track)  # Add track to the specified CD in arg input 
        else: 
            raise Exception('Track position must be an integer!')
            


