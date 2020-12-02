Morphometry: End-to-end FreeSurfer processing
=============================================
This pipeline implements end-to-end FreeSurfer processing. It will convert 
run the `recon-all` pipeline and secondary analysis tools e.g., `tal_QC_AZS`, 
`mris_anatomical_stats`, and `wm-anat-snr`. Finally, it will parse and reformat 
output into JSON and generate quality assessment snapshots.

## Table of contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Basic usage](#basic-usage)
4. [Advanced usage](#advanced-usage)
5. [Output](#output)
6. [Developers](#developers)

## Requirements
This pipeline has been largely tested with Python 2.7, 3.7, and FreeSurfer 
6.0.0.

## Installation
Just use `pip`

```bash
pip install morphometry
```

## Basic usage
For the most basic functionality, just pass in a NIFTI formatted image using 
the `--input` argument

```bash
surpher.py --input image.nii.gz
```

### dicom
You can also pass in a folder containing a DICOM series

```bash
surpher.py --input /path/to/dicoms ...
```

### xnat
> Note that this section assumes you're familiar with [yaxil](https://github.com/harvard-nrg/yaxil)

You can tell `surpher.py` to download your imaging data from an XNAT 
installation

```bash
surpher.py --input xnat --xnat TheXNAT:TheProject:TheSession:19 ...
```

## Advanced usage
The following section explains more advanced functionality.

### rate limited environments
Within HPC environments, you may be asked to rate limit your FreeSurfer jobs to 
reduce read/write stress on network attached storage. To help with this, you can 
tell `surpher.py` to run the main reconstruction pipeline on a local `--scratch`
partition and move the results to the specified `--output-dir`

```bash
surpher.py --input image.dcm --scratch /scratch --output-dir /path/to/output ...
```

This way you can run as many as you want... within reason.

### logging
Log files for all subprocesses are stored separately within the `logs` 
directory. There should be a `.log` file containing the console output 
and a corresponding `.yml` file that contains provenance information.

### automatic snapshots
For quality assessment, various screenshots are automatically generated. Those 
snapshots are stored in the `morphometrics/snapshots` directory.

> Headless snapshot support requires `xvfb-run`

### laterality plots
For quality assessment, left-hemisphere versus right-hemisphere laterality plots are 
generated and stored under `morphometrics/plots`.

### automatic parsing and re-formatting of (some) output files
Commonly used output files e.g., `aseg.stats`, `*.aparc.stats`, `wmsnr.e3.dat`, are 
automatically parsed and reformatted as JSON and stored under `morphometrics/stats`.

## Developers
For debugging, you may want to run certain steps of the pipeline, which you can 
do using the `--steps` argument

```bash
surpher.py --input image.dcm --steps tal_qc parse snapshots ...
```
