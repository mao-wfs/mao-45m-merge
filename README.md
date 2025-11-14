# mao-45m-merge
MAO data merge for the Nobeyama 45m telescope

## Installation

```shell
pip install mao-45m-merge==0.3.0
```

## Convert raw data to formatted (Zarr) data

### Correlator output

```python
from pathlib import Path
from mao_45m_merge import correlator


path_vdif = Path("/path/to/data.vdif")
path_raw_zarr = correlator.to_zarr(path_vdif)
path_fmt_zarr = correlator.convert(path_raw_zarr)
```

### Accelerometer log

```python
from pathlib import Path
from mao_45m_merge import accelerometer


path_gbd = Path("/path/to/data.gbd")
path_raw_zarr = accelerometer.to_zarr(path_gbd)
path_fmt_zarr = accelerometer.convert(path_raw_zarr)
```

### Accelerometer log (CSV format)

```python
from pathlib import Path
from mao_45m_merge import accelerometer_csv


path_csv = Path("/path/to/data.csv")
path_zarr = accelerometer_csv.convert(path_csv)
```

### Weather log

```python
from pathlib import Path
from mao_45m_merge import weather


path_csv = Path("/path/to/data.csv")
path_zarr = accelerometer.convert(path_csv)
```

### Antenna log (normal 10-sps format)

```python
from pathlib import Path
from mao_45m_merge import antenna


path_log = Path("/path/to/data.txt")
path_zarr = antenna.convert(path_log)
```

### Antenna log (new 50-sps format)

```python
from pathlib import Path
from mao_45m_merge import antenna_50_sps


path_log = Path("/path/to/data.txt")
path_zarr = antenna_50_sps.convert(path_log)
```

### SAM45 log (text dumped by `sldump`)

```python
from pathlib import Path
from mao_45m_merge import sam45


path_log = Path("/path/to/data.txt")
path_zarr = sam45.convert(path_log)
```

## Merge formatted data into a single Zarr file

```python
from pathlib import Path
from mao_45m_merge import merge


path_correlator = Path("/path/to/formatted/correlator.zarr")
path_accelerometer = Path("/path/to/formatted/accelerometer.zarr")
path_weather = Path("/path/to/formatted/weather.zarr")
path_antenna = Path("/path/to/formatted/antenna.zarr")
path_sam45 = Path("/path/to/formatted/sam45.zarr")
path_merged = Path("/path/to/merged.zarr")


merge.merge(
    path_correlator,
    path_merged,
    path_accelerometer_zarr=path_accelerometer,
    path_weather_zarr=path_weather,
    path_antenna_zarr=path_antenna,
    path_sam45_zarr=path_sam45,
)
```
