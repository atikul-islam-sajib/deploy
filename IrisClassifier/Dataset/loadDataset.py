import pandas as pd

class loadDataset:
    """
        A class for loading and working with datasets in CSV format using Pandas
        
        Parameters:
        ----------
        dataFrame: str, optional
        The filename or path to CSV dataset to be loaded
        
        Raises:
        ------
        ValueError:
            If the provided dataframe does not have a '.csv' file extensions
        
        Attributes:
        ----------
        dataFrame : str
            The filename or path to be loaded in CSV dataset.
    """
    def __init__(self, dataFrame = None):

        if dataFrame.split()[0][-3:] == 'csv':
            self.dataFrame = dataFrame
            
            self._read_csv(dataset = self.dataFrame)
        else:
            raise "Data Frame should be in the CSV format".title()
    
    def _read_csv(self, dataset = None):
        dataset = pd.read_csv(dataset)
        # Check the dataset in pandas DataFrame or not
        if isinstance(dataset, pd.core.frame.DataFrame):
            self._show_dataset(dataset = dataset)
            
            return dataset
        else:
            raise "Data Frame should be in the pandas format".capitalize()
    
    def _show_dataset(self, dataset = None):
        print(dataset.head())

if __name__ == "__main__":
    dataset = loadDataset(dataFrame = 'D:/IrisClassifier/Iris.csv')