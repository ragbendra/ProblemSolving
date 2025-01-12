import tarfile
from six.moves import urllib
import os
DOWNLOAD_ROOT = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/'
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + 'datasets/housing/housing.tgz' 
def fetch_housing_data(housing_path = HOUSING_PATH, housing_url = HOUSING_URL):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
        tgz_path = os.path.join(housing_path, 'housing.tgz')
        urllib.request.urlretrieve(housing_url, tgz_path)
        housing_tgz = tarfile.open(tgz_path)
        housing_tgz.extractfile(path=tgz_path)
        housing_tgz.close()
fetch_housing_data()