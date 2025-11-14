# standard library
from pathlib import Path
from tempfile import TemporaryDirectory


# third-party packages
import pandas as pd
import xarray as xr
from mao_45m_merge.powermeter import convert


# constants
TEST_CSV = Path("data") / "powermeter_2022144230000Z.csv"


# test function
def test_convert() -> None:
    """Test whether the data of a CSV file is correctly parsed."""
    with TemporaryDirectory() as zarr:
        path_zarr = Path(zarr)
        path_zarr = convert(TEST_CSV, path_zarr, overwrite=True)
        data_ds = xr.open_zarr(path_zarr)

        assert data_ds.time[0] == pd.Timestamp("2022-05-24T22:58:49.000000000")
        assert data_ds.powermeter[0] == -14.161
